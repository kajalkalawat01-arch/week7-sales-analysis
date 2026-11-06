from pathlib import Path

from sales_analyzer.data_loader import load_sales_data
from sales_analyzer.data_cleaner import clean_sales_data
from sales_analyzer.analyzer import analyze_sales
from sales_analyzer.visualizer import create_sales_charts


def main():
    file_path = "data/raw/sales_data.csv"

    print("Loading sales data...")
    data = load_sales_data(file_path)

    if data is None:
        print("Error: Could not load sales data.")
        return

    print("Cleaning sales data...")
    data = clean_sales_data(data)

    print("\nAnalyzing sales...")
    results = analyze_sales(data)

    print("\nSales Report")
    print("--------------------")
    print("Total Sales:", results["total_sales"])
    print("Average Sales:", results["average_sales"])

    if "top_products" in results:
        print("Top Products:")
        print(results["top_products"])

    if "monthly_sales" in results:
        print("Monthly Sales:")
        print(results["monthly_sales"])

    Path("data/reports").mkdir(parents=True, exist_ok=True)

    print("\nCreating charts...")
    create_sales_charts(data)

    print("Sales analysis completed successfully!")


if __name__ == "__main__":
    main()
