import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

df = pd.read_csv('train.csv')
df = df.dropna(subset=['Age', 'Fare'])

media_idade = df['Age'].mean()
mediana_idade = df['Age'].median()
media_fare = df['Fare'].mean()
mediana_fare = df['Fare'].median()
correlacao = df[['Age', 'Fare']].corr().iloc[0,1]

print(f"Média de Idade: {media_idade:.2f}")
print(f"Mediana de Idade: {mediana_idade:.2f}")
print(f"Média de Tarifa: {media_fare:.2f}")
print(f"Mediana de Tarifa: {mediana_fare:.2f}")
print(f"Correlação Idade x Tarifa: {correlacao:.2f}")

app = Dash(__name__)

app.layout = html.Div([
    html.H1('Dashboard Titanic'),

    html.Label('Escolha o tipo de gráfico:'),
    dcc.Dropdown(
        id='tipo-grafico',
        options=[
            {'label': 'Dispersão', 'value': 'dispersao'},
            {'label': 'Histograma', 'value': 'histograma'},
            {'label': 'Boxplot', 'value': 'boxplot'},
            {'label': 'Barras', 'value': 'barras'}
        ],
        value='dispersao'
    ),

    html.Label('Filtro: Idade Máxima'),
    dcc.Slider(
        id='idade-max',
        min=int(df['Age'].min()),
        max=int(df['Age'].max()),
        step=1,
        value=int(df['Age'].max()),
        marks={i: str(i) for i in range(0, int(df['Age'].max())+1, 10)}
    ),

    dcc.Graph(id='grafico')
])

@app.callback(
    Output('grafico', 'figure'),
    Input('tipo-grafico', 'value'),
    Input('idade-max', 'value')
)
def atualizar_grafico(tipo_grafico, idade_max):
    df_filtrado = df[df['Age'] <= idade_max]

    if tipo_grafico == 'dispersao':
        fig = px.scatter(
            df_filtrado, x='Age', y='Fare',
            title='Idade vs Tarifa - Titanic',
            labels={'Age': 'Idade', 'Fare': 'Tarifa'},
            color='Survived'
        )
    elif tipo_grafico == 'histograma':
        fig = px.histogram(
            df_filtrado, x='Age', nbins=30,
            title='Distribuição de Idade',
            labels={'Age': 'Idade'},
            color='Survived'
        )
    elif tipo_grafico == 'boxplot':
        fig = px.box(
            df_filtrado, x='Pclass', y='Fare',
            color='Pclass',
            title='Boxplot - Tarifa por Classe',
            labels={'Pclass': 'Classe', 'Fare': 'Tarifa'}
        )
    elif tipo_grafico == 'barras':
        sobreviventes = df_filtrado.groupby(['Sex', 'Survived']).size().reset_index(name='count')
        fig = px.bar(
            sobreviventes, x='Sex', y='count',
            color='Survived',
            barmode='group',
            title='Sobreviventes por Sexo'
        )
    else:
        fig = px.scatter(df_filtrado, x='Age', y='Fare')

    return fig

if __name__ == '__main__':
    app.run(debug=True)

