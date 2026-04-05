from src.load_data import load_data
from datetime import datetime
import matplotlib.pyplot as plt

# Load dataset
sales_df = load_data("data/sales.csv")


def explore_data(df):
    """Print basic information about the dataset."""

    rows, columns = df.shape

    print("\nDataset Information")
    print("-------------------")
    print(f"Number of rows: {rows}")
    print(f"Number of columns: {columns}")
    print(f"Columns: {list(df.columns)}")
    print("\nData types:")
    print(df.dtypes)

    print("\nFirst 5 rows:")
    print(df.head())

explore_data(sales_df)

# Ask user for a date
date_input = input("\nEnter a date (YYYY-MM-DD): ")

try:
    target_date = datetime.strptime(date_input, "%Y-%m-%d").date()
except ValueError:
    print("Invalid date format")
    exit()

# Vectorized filtering
daily_sales = sales_df[sales_df["date"] == target_date]

if daily_sales.empty:
    print("No sales found for that date")
else:
    # Vectorized metrics
    total_sales = (daily_sales["quantity"] * daily_sales["price"]).sum()
    total_units = daily_sales["quantity"].sum()

    # Best-selling product using groupby
    sales_by_product = daily_sales.groupby("product")["quantity"].sum()

    best_selling_product = sales_by_product.idxmax()
    max_quantity = sales_by_product.max()

    print(f"\nTotal units sold on ({target_date}): {total_units}")
    print(f"Total revenue on ({target_date}): ${total_sales}")
    print(f"Best selling product: {best_selling_product} ({max_quantity} units)")


product_units = sales_df.groupby('product')['quantity'].sum()
product_units_sorted = product_units.sort_values(ascending=False)

product_units_sorted.plot(kind="bar")

plt.title("Units Sold by Product")
plt.xlabel("Product")
plt.ylabel("Units Sold")

plt.show()