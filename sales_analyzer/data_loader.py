import pandas as pd
from pathlib import Path


def load_sales_data(file_path):
    try:
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError("Sales data file not found.")

        if path.suffix.lower() == ".csv":
            data = pd.read_csv(path)

        elif path.suffix.lower() in [".xlsx", ".xls"]:
            data = pd.read_excel(path)

        else:
            raise ValueError("Unsupported file format.")

        return data

    except Exception as error:
        print("Error loading data:", error)
        return None
