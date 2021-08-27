import pandas as pd
import plotly.express as px

df = pd.read_csv("coviddata.csv")
fig = px.scatter(df,  x="cases", y="date",
	          color="country",
                   size_max=60)
fig.show()