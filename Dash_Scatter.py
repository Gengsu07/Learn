from fileinput import filename
from statistics import mode
from matplotlib.pyplot import title
from numpy import size
import pandas as pd
import plotly.graph_objs  as go
import plotly.offline as po
from sympy import symbols

superstore = pd.read_excel('superstore.xls')
superstore = superstore.filter(['Segment', 'Country/Region','Category','Sub-Category', 'Product Name', 'Sales', 'Quantity', 'Discount','Profit'])
# superstore = superstore.groupby(['Segment', 'Country/Region','Category','Sub-Category', 'Product Name']).sum().reset_index()
data_scatter = [go.Scatter(x = superstore['Discount'],
                           y = superstore['Sales'],
                           mode = 'markers',
                           marker = dict(
                               size=9
                            
                           )
)
                ]

layout_scatter = go.Layout(title='Sales vs Discount',
                           xaxis = dict(title='Diskon'),
                           yaxis = dict(title='Sales'),
                           hovermode = 'closest',
                           color = 'rgb(125,210,180)'
                           
                           )

scatter = go.Figure(data=data_scatter,layout=layout_scatter)

po.plot(scatter,filename='scatter.html')
