# 6_test_adaptable_calendar

Test of the static-calendar assumption (sowing / anthesis / maturity fixed at MIRCA2000 values
in every scenario). Not yet implemented; see Section 6 of `Crop_Suitability_SVM_Report.docx`.

Planned:
1. **Sensitivity test** — shift sowing and maturity by +-10 and +-20 days (anthesis stays maturity - 60),
   recompute the BIO variables, and measure how much the suitability maps change (start with Maize_rf).
2. **Temperature-driven phenology** — sowing when a temperature threshold is crossed, anthesis and
   maturity at fixed growing-degree-day sums, computed from each scenario's own climate.
