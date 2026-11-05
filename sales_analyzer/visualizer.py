import matplotlib.pyplot as plt
from pathlib import Path


def create_sales_charts(data, output_dir="data/reports"):
    if data is None or data.empty:
        print("No data available for charts.")
        return

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    # Bar Chart: Sales by Product
    if "Product" in data.columns and "Sales" in data.columns:
        product_sales = data.groupby("Product")["Sales"].sum()

        product_sales.plot(kind="bar", title="Sales by Product")
        plt.xlabel("Product")
        plt.ylabel("Sales")
        plt.tight_layout()
        plt.savefig(output_path / "product_sales.png")
        plt.close()

    # Line Chart: Monthly Sales
    if "Date" in data.columns and "Sales" in data.columns:
        monthly_sales = data.copy()
        monthly_sales["Date"] = plt.matplotlib.dates.num2date(
            plt.matplotlib.dates.date2num(
                __import__("pandas").to_datetime(
                    monthly_sales["Date"], errors="coerce"
                )
            )
        )
        monthly_sales = monthly_sales.dropna(subset=["Date"])
        monthly_sales = monthly_sales.set_index("Date")
        monthly_sales = monthly_sales["Sales"].resample("ME").sum()

        monthly_sales.plot(kind="line", marker="o", title="Monthly Sales")
        plt.xlabel("Month")
        plt.ylabel("Sales")
        plt.tight_layout()
        plt.savefig(output_path / "monthly_sales.png")
        plt.close()

    # Pie Chart: Sales by Product
    if "Product" in data.columns and "Sales" in data.columns:
        product_sales = data.groupby("Product")["Sales"].sum()

        product_sales.plot(kind="pie", autopct="%1.1f%%",
                           title="Sales Distribution")
        plt.ylabel("")
        plt.tight_layout()
        plt.savefig(output_path / "sales_distribution.png")
        plt.close()
