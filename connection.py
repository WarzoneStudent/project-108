import pandas as pd

df = pd.read_csv("data.csv")
ratings = df["Avg Rating"].tolist()

import plotly.figure_factory as ff

fig = ff.create_distplot([ratings],["Ratings avg"],show_hist=False)
fig.show()