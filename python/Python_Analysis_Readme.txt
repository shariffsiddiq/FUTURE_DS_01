FUTURE INTERNS — TASK 1: BUSINESS SALES PERFORMANCE ANALYTICS
Python analysis guide

Files:
- Superstore_Cleaned_Validated.xlsx: cleaned input dataset
- superstore_analysis.py: reproducible Python analysis script
- Superstore_Python_Analysis.xlsx: analysis results workbook, created beside the script
- monthly_trends.csv, category_analysis.csv, region_analysis.csv: summary data, created beside the script

How to run:
1. Put superstore_analysis.py and Superstore_Cleaned_Validated.xlsx in the same folder, or place the input file in the project's excel folder.
2. Install packages in the VS Code terminal:
   pip install pandas openpyxl matplotlib numpy
3. Run:
   python superstore_analysis.py

The script saves the workbook and CSV summaries beside itself, then opens the monthly sales chart in a window. Close the chart window to finish running the script. It does not save a chart image.
