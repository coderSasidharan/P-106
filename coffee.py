import pandas as pd
import plotly.express as px
import numpy as np

df = pd.read_csv("coffee.csv")

coffeeList = df["Coffee in ml"].tolist()
sleepList = df["sleep in hours"].tolist()

correlation = np.corrcoef(coffeeList,sleepList)
print("correlation is:",correlation[0,1])

fig = px.scatter(df,x = "Coffee in ml",y = "sleep in hours")
fig.show()