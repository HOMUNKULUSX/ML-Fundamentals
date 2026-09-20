import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/housing.csv")

pd.set_option(
    "display.max_columns",
    None
)

print(df.shape)
print(df.dtypes)
print(df.nunique())
print(df.isnull().sum())
print(df.duplicated().sum())

#print(df[df["total_bedrooms"].isna()].describe())

ratio = (
    df["total_bedrooms"] / df["total_rooms"]
).median()

df["total_bedrooms"] = df["total_bedrooms"].fillna(
    df["total_rooms"] * ratio
)

print(df.isnull().sum())
print(df["total_bedrooms"])

df["total_bedrooms"] = df["total_bedrooms"].round().astype(int)
print(df["total_bedrooms"])