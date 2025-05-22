import plotly.express as px
import pandas as pd

df = pd.read_csv('train.csv')

print(df.head())

age = 'Age'
fare = 'Fare'

fig = px.scatter(
    df, 
    x=age, 
    y=fare, 
    title='Idade vs Tarifa - Titanic',
    labels={age: 'Idade', fare: 'Tarifa'} 
)

fig.show()
