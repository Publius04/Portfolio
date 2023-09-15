import pandas as pd
import plotly.express as px
import os
import json

def data():
    with open("variant.json", "r") as f:
        variants = pd.DataFrame(json.load(f)["USA"])
    variants["week"] = pd.to_datetime(variants["week"], format=r"%Y-%m-%d")

    weeks = variants["week"]
    variant_names = variants.columns[1:]
    
    week = []
    variant = []
    value = []

    for name in variant_names:
        week += list(weeks)
        variant += [name] * len(weeks)
        value += list(variants[name])

    vdf = pd.DataFrame({"week": week, "variant": variant, "value": value})
    return vdf, list(variant_names)

def main():
    print(data())

if __name__ == "__main__":
    main()