import pandas as pd

# read input and remove spurious : at end of count
input1 = pd.read_csv("input1.csv", sep=' ',
         names=["date","time", "tree","count","ID", "info"])
input1["count"] = input1["count"].apply(lambda s:s[:-1])

# read lookup and merge
lookup = pd.read_csv("lookup.csv")
merged = input1.merge(lookup, on="ID")

# collapse time and date to single column
merged["time"] = merged["date"] + " " + merged["time"]
del merged["date"]

# output
print(merged)
merged.to_csv("testme.csv", index=False)