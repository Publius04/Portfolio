import plotly.graph_objects as go
import numpy as np
import pandas as pd
from scipy.stats import norm

data = [31.4, 41.3, 13.7, 28.3, 13.1, 38.2, 25.1, 34.4, 28.0, 22.4, 16.9, 16.5, 23.5, 17.2, 42.3, 21.3, 19.9, 24.6, 25.1, 19.4]
mu = sum(data)/len(data)
sigma = (sum([(x - mu)**2 for x in data])/(len(data)-1))**0.5


x = np.arange(mu-4*sigma, mu+4*sigma, 0.001)
y = norm.pdf(x, mu, sigma)

fig = go.Figure()
fig.add_trace(go.Histogram(x=data, nbinsx=6, histnorm="probability density", name="Experiment Data"))
fig.add_trace(go.Line(x=x, y=y, name="Normal Distribution")).update_layout(xaxis_title="Distance (cm)", yaxis_title="Probability Density", font_family="Times New Roman", bargap=0.1)
fig.show()