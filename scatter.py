import pandas as pd
import plotly.express as px
import csv

df = pd.read_csv('data.csv')

print(df.groupby("level")["attempt"].mean())

fig = px.scatter(
    x= df.groupby("level")["attempt"].mean(),
    y= ['Level 1, Level 2, Level 3, Level 4'],
   size = "attempt",
    color = "attempt",
    size_max = 60,
    orientation = 'h'
)

fig.show()