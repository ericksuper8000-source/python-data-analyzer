import pandas as pd

def load_data(file_path):
    """
    Load sales data from a CSV file.

    :param file_path: Path to the CSV file
    :return: DataFrame with sales data
    """

    df = pd.read_csv(file_path, sep=None, engine="python")

    # Convert date column to datetime.date
    df["date"] = pd.to_datetime(df["date"]).dt.date

    return df