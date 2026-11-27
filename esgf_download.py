"""
Downloads CMIP6 files from ESGF: search API of an index node, HTTPServer links, every replica tried in turn, checksum
(SHA256) checked. Used for the EC-Earth3 SSPs of the crop application (CROP_REF=w5e5, EC-Earth3 grid):

    python esgf_download.py --out /eos/jeodpp/data/projects/DROUGHTOBS/elisa/Crop_suitability/input_data/EC-Earth3 \
        --experiments ssp126 ssp245 ssp370 ssp585 --years 2041 2100

Files go to <out>/<experiment>/<variable>/<file name of ESGF>. A file already there with the right checksum is
skipped, so the script can be rerun after an interruption; a download is written to <name>.part and renamed once its
checksum is right. --dry-run lists the files and their size without downloading. Standard library and wget only.
"""
import argparse
import hashlib
import json
import re
import subprocess
import urllib.parse
import urllib.request
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

INDEX = "https://esgf.nci.org.au/esg-search/search"   # index node that answered from JEO-lab (27 Nov 2026)


def search(index, source, member, experiment, variable, table):
    """File records of one dataset (all replicas, latest versions)."""
    q = {"project": "CMIP6", "source_id": source, "experiment_id": experiment, "variant_label": member,
         "table_id": table, "variable_id": variable, "type": "File", "latest": "true",
         "format": "application/solr+json", "limit": 10000,
         "fields": "title,url,data_node,checksum,checksum_type,dataset_id,size"}
    with urllib.request.urlopen(f"{index}?{urllib.parse.urlencode(q)}", timeout=180) as r:
        return json.load(r)["response"]["docs"]


def years_of(title):
    m = re.search(r"_(\d{4})\d{4}-(\d{4})\d{4}\.nc$", title)
    return (int(m.group(1)), int(m.group(2))) if m else (None, None)


def dataset_version(doc):
    """vYYYYMMDD of the dataset id ('CMIP6.....v20200310|data_node'); '' if absent."""
    m = re.search(r"\.v(\d{8})\|", doc.get("dataset_id", ""))
    return m.group(1) if m else ""


def files_of(docs, y0, y1):
    """One entry per file name: the latest dataset version, its HTTPServer links (one per replica), checksum, size."""
    by_title = defaultdict(list)
    for d in docs:
        by_title[d["title"]].append(d)
    out = []
    for title, ds in sorted(by_title.items()):
        a, b = years_of(title)
        if a is None or b < y0 or a > y1:
            continue
        v = max(dataset_version(d) for d in ds)
        ds = [d for d in ds if dataset_version(d) == v]
        urls = [u.split("|")[0] for d in ds for u in d.get("url", []) if u.endswith("|HTTPServer")]
        ck = next((d["checksum"][0] for d in ds if d.get("checksum")), None)
        ct = next((d["checksum_type"][0] for d in ds if d.get("checksum_type")), "SHA256")
        out.append({"title": title, "version": v, "urls": urls, "checksum": ck, "checksum_type": ct,
                    "size": int(ds[0].get("size", 0))})
    return out


def checksum_ok(path, f):
    if not f["checksum"]:
        return path.stat().st_size == f["size"]
    h = hashlib.new(f["checksum_type"].lower())
    with open(path, "rb") as fh:
        for block in iter(lambda: fh.read(1 << 24), b""):
            h.update(block)
    return h.hexdigest() == f["checksum"]


def fetch(f, dest):
    path = dest / f["title"]
    if path.exists() and checksum_ok(path, f):
        return f"skip {f['title']}"
    part = path.with_name(path.name + ".part")
    for url in f["urls"]:
        r = subprocess.run(["wget", "-q", "-c", "--timeout=60", "--tries=3", "-O", str(part), url])
        if r.returncode == 0 and part.exists() and checksum_ok(part, f):
            part.rename(path)
            return f"ok {f['title']}"
        part.unlink(missing_ok=True)                     # bad replica or broken transfer: next replica from scratch
    return f"FAILED {f['title']} ({len(f['urls'])} replicas)"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", required=True)
    ap.add_argument("--source", default="EC-Earth3")
    ap.add_argument("--member", default="r1i1p1f1")
    ap.add_argument("--table", default="day")
    ap.add_argument("--experiments", nargs="+", default=["ssp126", "ssp245", "ssp370", "ssp585"])
    ap.add_argument("--variables", nargs="+", default=["tasmax", "tasmin", "pr", "rsds"])
    ap.add_argument("--years", nargs=2, type=int, default=[2041, 2100])
    ap.add_argument("--index", default=INDEX)
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    jobs, total = [], 0
    for e in a.experiments:
        for v in a.variables:
            fs = files_of(search(a.index, a.source, a.member, e, v, a.table), *a.years)
            yrs = sorted({y for f in fs for y in range(*years_of(f["title"])) } | {years_of(f["title"])[1] for f in fs})
            gb = sum(f["size"] for f in fs) / 1e9
            total += gb
            print(f"{e} {v}: {len(fs)} files, {yrs[0] if yrs else '-'}-{yrs[-1] if yrs else '-'}, {gb:.1f} GB, "
                  f"version {sorted({f['version'] for f in fs})}, replicas per file {min((len(f['urls']) for f in fs), default=0)}"
                  f"-{max((len(f['urls']) for f in fs), default=0)}", flush=True)
            dest = Path(a.out) / e / v
            jobs += [(f, dest) for f in fs]
    print(f"total {len(jobs)} files, {total:.1f} GB", flush=True)
    if a.dry_run:
        return
    for _, dest in jobs:
        dest.mkdir(parents=True, exist_ok=True)
    with ThreadPoolExecutor(a.workers) as ex:
        for msg in ex.map(lambda j: fetch(*j), jobs):
            print(msg, flush=True)
    print("DOWNLOAD_DONE", flush=True)


if __name__ == "__main__":
    main()
