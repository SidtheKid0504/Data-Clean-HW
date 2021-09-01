import pandas as pd 
import csv
df = pd.read_csv("./data/data_merged.csv")
print(df.columns)
print(df.shape)
del df ["Luminosity"]
del df ["Star_Name"]
del df ["Distance.1"]
del df ["Mass.1"]
del df ["Radius.1"]
del df ["Unnamed: 0"]
del df ["Unnamed: 6"]
print(df.columns)
df.to_csv("./data/final_data.csv")