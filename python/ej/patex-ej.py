import plotly.plotly as py
from plotly.graph_objs import *
# Fill in with your personal username and API key
# or, use this public demo account
py.sign_in('Python-Demo-Account', 'gwt101uhh0')

trace1 = Scatter(
    x=[1, 2, 3, 4],
    y=[1, 4, 9, 16],
    name='$\\alpha_{1c} = 352 \\pm 11 \\text{ km s}^{-1}$'
)
trace2 = Scatter(
    x=[1, 2, 3, 4],
    y=[0.5, 2, 4.5, 8],
    name='$\\beta_{1c} = 25 \\pm 11 \\text{ km s}^{-1}$'
)
data = Data([trace1, trace2])
layout = Layout(
    xaxis=XAxis(
        title='$\\sqrt{(n_\\text{c}(t|{T_\\text{early}}))}$'
    ),
    yaxis=YAxis(
        title='$d, r \\text{ (solar radius)}$'
    )
)
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='latex')