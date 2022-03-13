import pandas as pd
import plotly.graph_objs  as go
import plotly.offline as po

superstore= pd.read_csv('Global Superstore.xls',usecols=['Order Date','Quantity'],parse_dates=['Order Date'])
superstore.head()
