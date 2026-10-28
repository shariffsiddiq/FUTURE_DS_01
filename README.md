# Business Sales Performance Analytics

**Future Interns — Task 1**

An end-to-end Superstore sales analysis, organized in the workflow order **Excel → Python → Power BI**. The project includes the source and cleaned data, analysis files, reports, dashboard, and visual exports.

## Project workflow

**Excel → Python → Power BI**

### Phase 1 — Excel: data preparation and initial analysis

Start with the Superstore source data, then use the cleaned and validated workbook for analysis. The data quality report and sales trend/category/region visuals provide supporting checks and summaries.

- Source data: [`data/Sample - Superstore.csv`](data/Sample%20-%20Superstore.csv)
- Cleaned dataset: [`excel/Superstore_Cleaned_Validated.xlsx`](excel/Superstore_Cleaned_Validated.xlsx)
- Duplicate cleaned dataset copy: [`data/Superstore_Cleaned_Validated.xlsx`](data/Superstore_Cleaned_Validated.xlsx)
- Data quality report: [`reports/Data_Quality_Report.xlsx`](reports/Data_Quality_Report.xlsx)
- Project report: [`reports/Business Sales Performance Analytics.pdf`](reports/Business%20Sales%20Performance%20Analytics.pdf) · [editable DOCX](reports/Business%20Sales%20Performance%20Analytics.docx)

**Sales trend**

![Yearly sales trend](visuals/yearly_sales_trend.png)

**Category and regional performance**

| Category performance | Regional performance |
|---|---|
| ![Sales by category](visuals/category_performance.png) | ![Sales by region](visuals/regional_performance.png) |

### Phase 2 — Python: repeatable analysis

The Python script reads the cleaned workbook, calculates overall KPIs and sales/profit summaries by time, category, sub-category, region, and product, then writes a results workbook and CSV summaries.

- Analysis script: [`python/superstore_analysis.py`](python/superstore_analysis.py)
- Run instructions: [`python/Python_Analysis_Readme.txt`](python/Python_Analysis_Readme.txt)
- Results workbook: [`python/Superstore_Python_Analysis.xlsx`](python/Superstore_Python_Analysis.xlsx)
- Monthly summary: [`python/monthly_trends.csv`](python/monthly_trends.csv)
- Category summary: [`python/category_analysis.csv`](python/category_analysis.csv)
- Regional summary: [`python/region_analysis.csv`](python/region_analysis.csv)

To run the analysis from the project root:

```bash
python -m pip install pandas numpy matplotlib openpyxl
python python/superstore_analysis.py
```

The script uses the cleaned workbook in `python/` when present, or falls back to `excel/`. It writes the results workbook and CSV files beside the script and displays a monthly sales chart.

### Phase 3 — Power BI: interactive dashboards

Open the Power BI report to explore sales performance and product profitability. The screenshots below are static previews; use the `.pbix` file for the interactive report.

- Power BI report: [`powerbi/Superstore_Sales_Dashboard.pbix`](powerbi/Superstore_Sales_Dashboard.pbix)

**Sales performance dashboard**

![Superstore sales performance dashboard](visuals/sales_performance_dashboard.png)

**Product and profitability dashboard**

![Product and profitability dashboard](visuals/product_profitability_dashboard.png.png)

## Repository contents

```text
data/
  Sample - Superstore.csv
  Superstore_Cleaned_Validated.xlsx
excel/
  Superstore_Cleaned_Validated.xlsx
powerbi/
  Superstore_Sales_Dashboard.pbix
python/
  category_analysis.csv
  monthly_trends.csv
  Python_Analysis_Readme.txt
  region_analysis.csv
  superstore_analysis.py
  Superstore_Python_Analysis.xlsx
reports/
  Business Sales Performance Analytics.docx
  Business Sales Performance Analytics.pdf
  Data_Quality_Report.xlsx
visuals/
  category_performance.png
  product_profitability_dashboard.png.png
  regional_performance.png
  sales_performance_dashboard.png
  yearly_sales_trend.png
```
