import pandas as pd
cars_df = pd.read_csv("CARS1.csv")
commison_df = pd.read_excel("CARS2.xlsx")

merged = pd.merge(cars_df, commison_df,on="Make", how="outer")
merged["commision_pay"] = merged["commision"] * merged["price"]
print(merged)