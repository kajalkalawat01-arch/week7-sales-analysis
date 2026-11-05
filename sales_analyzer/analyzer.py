import pandas as pd


def analyze_sales(data):
    if data is None or data.empty:
        return None

    required_columns = ["Sales"]

    for column in required_columns:
        if column not in data.columns:
            raise ValueError(f"Missing column: {column}")

    total_sales = data["Sales"].sum()
    average_sales = data["Sales"].mean()

    result = {
        "total_sales": total_sales,
        "average_sales": average_sales
    }

    if "Product" in data.columns:
        result["top_products"] = (
            data.groupby("Product")["Sales"]
            .sum()
            .sort_values(ascending=False)
            .head(5)
        )

    if "Date" in data.columns:
        data = data.copy()
        data["Date"] = pd.to_datetime(
            data["Date"], errors="coerce"
        )

        data = data.dropna(subset=["Date"])

        result["monthly_sales"] = (
            data.groupby(data["Date"].dt.to_period("M"))["Sales"]
            .sum()
        )

    return result
