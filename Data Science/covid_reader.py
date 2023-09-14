import pandas as pd
import plotly.express as px
import os

def gen_data():
    pwd = os.getcwd()
    df = pd.read_csv(pwd + "\\data.csv")
    df = df.drop(columns=["mortality", "mortality_7"])
    df["submission_date"] = pd.to_datetime(df["submission_date"])
    df.sort_values(by=["state", "submission_date"], inplace=True)
    df.reset_index(inplace=True)
    df.drop(columns="index", inplace=True)
    return df

def main():
    gen_data()

if __name__ == "__main__":
    main()
