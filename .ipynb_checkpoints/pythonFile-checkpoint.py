import pandas as pd

df = pd.DataFrame(columns=["indexxx", "first", "second"])

df.to_csv("testCSV.csv", index=False)