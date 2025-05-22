import plotly.express as px

dados_x = [1, 2, 3, 4, 5]
dados_y = [10, 15, 13, 17, 20]

fig = px.line(x=dados_x, y=dados_y)

fig.show()
