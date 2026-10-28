import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

script_folder = Path(__file__).resolve().parent
input_file = script_folder / "Superstore_Cleaned_Validated.xlsx"
if not input_file.exists():
    input_file = script_folder.parent / "excel" / "Superstore_Cleaned_Validated.xlsx"
df = pd.read_excel(input_file, sheet_name="Cleaned_Data")
df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
df["Ship Date"] = pd.to_datetime(df["Ship Date"], errors="coerce")
df["Order Month"] = df["Order Date"].dt.to_period("M").astype(str)
df["Order Year"] = df["Order Date"].dt.year

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order ID"].nunique()
total_customers = df["Customer ID"].nunique()
total_units = df["Quantity"].sum()
profit_margin = total_profit / total_sales * 100 if total_sales else np.nan

kpis = pd.DataFrame([
    ["Total Sales", total_sales],
    ["Total Profit", total_profit],
    ["Distinct Orders", total_orders],
    ["Distinct Customers", total_customers],
    ["Units Sold", total_units],
    ["Overall Profit Margin (%)", profit_margin],
], columns=["Metric", "Value"])

monthly = df.groupby("Order Month", as_index=False).agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Orders=("Order ID", "nunique"),
    Units=("Quantity", "sum")
)
yearly = df.groupby("Order Year", as_index=False).agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Orders=("Order ID", "nunique"),
    Units=("Quantity", "sum")
)
category = df.groupby("Category", as_index=False).agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Units=("Quantity", "sum")
)
region = df.groupby("Region", as_index=False).agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Units=("Quantity", "sum")
)
sub_category = df.groupby("Sub-Category", as_index=False).agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Units=("Quantity", "sum")
)
product = df.groupby(["Product ID", "Product Name"], as_index=False).agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Units=("Quantity", "sum")
)
loss_analysis = df.groupby(df["Profit"] < 0).agg(
    Rows=("Profit", "size"),
    Total_Profit=("Profit", "sum")
).reset_index(names="Negative_Profit")

with pd.ExcelWriter(script_folder / "Superstore_Python_Analysis.xlsx", engine="openpyxl") as writer:
    kpis.to_excel(writer, index=False, sheet_name="KPI_Summary")
    yearly.to_excel(writer, index=False, sheet_name="Yearly_Trends")
    monthly.to_excel(writer, index=False, sheet_name="Monthly_Trends")
    category.to_excel(writer, index=False, sheet_name="Category_Analysis")
    sub_category.to_excel(writer, index=False, sheet_name="SubCategory_Analysis")
    region.to_excel(writer, index=False, sheet_name="Region_Analysis")
    product.sort_values("Sales", ascending=False).head(10).to_excel(writer, index=False, sheet_name="Top_Products_Sales")
    product.sort_values("Profit", ascending=False).head(10).to_excel(writer, index=False, sheet_name="Top_Products_Profit")
    product.sort_values("Profit", ascending=True).head(10).to_excel(writer, index=False, sheet_name="Lowest_Profit_Products")
    loss_analysis.to_excel(writer, index=False, sheet_name="Loss_Analysis")

monthly.to_csv(script_folder / "monthly_trends.csv", index=False)
category.to_csv(script_folder / "category_analysis.csv", index=False)
region.to_csv(script_folder / "region_analysis.csv", index=False)

plt.figure()
plt.plot(monthly["Order Month"], monthly["Sales"])
plt.xticks(rotation=45, ha="right")
plt.title("Monthly Sales Trend")
plt.xlabel("Order Month")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

print(kpis.to_string(index=False))
print("\\nCategory analysis:\\n", category.to_string(index=False))
print("\\nRegional analysis:\\n", region.to_string(index=False))
