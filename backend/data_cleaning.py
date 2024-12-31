import pandas as pd


def clean_data(file_path):
    df = pd.read_csv(file_path)
    # Example cleaning: remove personal information
    df = df.drop(columns=['PI_info'])
    df.to_csv(file_path, index=False)
