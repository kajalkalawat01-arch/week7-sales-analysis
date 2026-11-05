import pandas as pd


def clean_sales_data(data):
    if data is None or data.empty:
        return None

    data = data.copy()

    # Remove duplicate rows
    data = data.drop_duplicates()

    # Remove extra spaces from column names
    data.columns = data.columns.str.strip()

    # Handle missing values
    for column in data.columns:

        if pd.api.types.is_numeric_dtype(data[column]):
            data[column] = data[column].fillna(
                data[column].median()
            )

        else:
            data[column] = data[column].fillna("Unknown")

    return data
