# preprocessing.py
from data import fetch_data
import pandas as pd
from fire import Fire
from pathlib import Path
out_dir = Path(__file__).parent.parent.parent / "out"
data_dir = Path(__file__).parent.parent.parent / "data"

def cast_rewards_col(data):
    data["rewards"] = pd.to_numeric(data["rewards"], errors='coerce')
    return data

def fillna_step(data: pd.DataFrame) -> pd.DataFrame:
    return data.fillna(-100)

def filter_onset_step(data: pd.DataFrame) -> pd.DataFrame:
    return data[data["onset"] > 600]

def filter_trial_type_step(data: pd.DataFrame) -> pd.DataFrame:
    return data[data["trial_type"].str.startswith("decision_")]

def normalize_reward_step(data: pd.DataFrame) -> pd.DataFrame:
    col = data["rewards"]
    data["rewards"] = (col - col.mean()) / col.std()
    return data

def save_data_step(data: pd.DataFrame, out_file) -> None:
    data.to_csv(out_dir / out_file, index=False)

def pipeline(path=data_dir, filename="trials-1.csv", out_file="preprocessed-1.csv") -> pd.DataFrame:
    
    #ipdb.set_trace()   # ipdb breakpoint
    # breakpoint()      # python breakpoint 

    print("Import data...")
    data = fetch_data(data_dir=path, filename=filename)
    data = cast_rewards_col(data)

    print("Running preprocessing...")
    data = fillna_step(data)
    data = filter_onset_step(data)
    data = filter_trial_type_step(data)
    data = normalize_reward_step(data)
    save_data_step(data, out_file)

    return data

def main():
    Fire(pipeline)

if __name__ == "__main__":
    main()