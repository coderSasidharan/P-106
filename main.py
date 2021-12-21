import pandas as pd
import plotly.express as px
import numpy as np

df = pd.read_csv("studentMarks.csv")
marksList = df["Marks In Percentage"].tolist()
daysList = df["Days Present"].tolist()


correlation = np.corrcoef(marksList,daysList)
print("Correlation is : ",correlation[0,1])

fig = px.scatter(df,x ="Days Present",y = "Marks In Percentage")
fig.show()
