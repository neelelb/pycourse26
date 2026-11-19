from os.path import join as opj
import pandas as pd
from pathlib import Path

def sanitize(data):
    names = data.columns
    clean = [n for n in names if "Unnamed" not in n]
    data = data.dropna(axis=1, how="all")
    data.columns = clean
    return data
    

def fetch_data(data_dir, filename) -> pd.DataFrame:
    data =pd.read_csv(opj(data_dir, filename), sep=r'\s+')

    if len(data.columns) == 1:
        data = pd.read_csv(opj(data_dir, filename), sep=',')

    #breakpoint() 
    sanitize(data)

    return data

# This block will only run when calling `python data.py`
if __name__ == "__main__":
    print("Fetching data")    
    data = fetch_data("data.csv")
    print(data)