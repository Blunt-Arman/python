import pandas as pd

calories = {
    "Day1":"420",
    "Day2":"380",
    "Day3":"390",
    }
df = pd.DataFrame(calories,index=["Day1","Day2","Day3"])
print(df.iloc[0])
print(df.iloc[[0,1]])
