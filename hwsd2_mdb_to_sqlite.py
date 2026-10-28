"""
hwsd2_mdb_to_sqlite.py - copy of the HWSD v2 attribute database (FAO HWSD2.mdb, Microsoft Access) into SQLite, so that
the soil notebooks (2.a, 2.c) can read it on Linux (BDAP JupyterLab has no Access driver).

Every table is copied as it is (same names, same columns, same rows); the notebooks then run the same SQL queries
through crop_utils.hwsd_connect(). Row counts are checked at the end.

Needs Windows with pyodbc and the Microsoft Access driver (as for reading the .mdb itself).

Usage (from the project root):
  python hwsd2_mdb_to_sqlite.py <HWSD2.mdb> [<HWSD2.sqlite>]      # default: HWSD2.sqlite next to the .mdb
"""
import sqlite3
import sys
from pathlib import Path

import pandas as pd

import crop_utils as cu


def main():
    mdb = Path(sys.argv[1])
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else mdb.with_suffix(".sqlite")
    tmp = out.with_suffix(".sqlite.tmp")
    tmp.unlink(missing_ok=True)
    src = cu.hwsd_connect(mdb)
    tables = [t.table_name for t in src.cursor().tables(tableType="TABLE")]
    dst = sqlite3.connect(tmp)
    counts = {}
    for t in tables:
        df = pd.read_sql(f"SELECT * FROM [{t}]", src)
        # integer columns with empty values come out as float: keep them integer, so that a query returns the same
        # types from SQLite as from Access
        cur = src.cursor()
        cur.execute(f"SELECT TOP 1 * FROM [{t}]")
        ints = [d[0] for d in cur.description if d[1] is int]
        cur.close()
        for c in ints:
            df[c] = df[c].astype("Int64")
        df.to_sql(t, dst, index=False)
        counts[t] = len(df)
        print(f"  {t:28s} {len(df):9d} rows, {df.shape[1]:3d} columns", flush=True)
    dst.close()
    src.close()
    check = sqlite3.connect(tmp)
    for t, n in counts.items():
        m = check.execute(f'SELECT COUNT(*) FROM "{t}"').fetchone()[0]
        if m != n:
            raise ValueError(f"{t}: {m} rows in SQLite, {n} in the .mdb")
    check.close()
    tmp.replace(out)
    print(f"{len(tables)} tables copied -> {out} ({out.stat().st_size / 1e6:.0f} MB)")


if __name__ == "__main__":
    main()
