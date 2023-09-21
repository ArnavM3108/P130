import pandas as pd

data = pd.read_csv("project130Finaldata.csv")

del data["Star_name"]

data = data.dropna()

data.to_csv("data.csv")








