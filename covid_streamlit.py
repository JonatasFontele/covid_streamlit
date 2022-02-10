import pandas as pd
import streamlit as st
import plotly.express as px

# https://www.kaggle.com/yamqwe/omicron-covid19-variant-daily-cases

# Le o conjunto de dados
df = pd.read_csv('covid-variants.csv')

# Converte coluna de datas para o tipo date com formato ano-mes-dia
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')

# Pega a lista de paises sem repeticao
paises = list(df['location'].unique())

# Pega a lista de variantes sem repeticao
variantes = list(df['variant'].unique())

# Para criar o titulo
tipo = 'Casos diários'
titulo = tipo + ' para '

# Permite o usuario selecionar um pais ou todos
pais = st.sidebar.selectbox('Selecione o país', ['Todos'] + paises)

# Permite o usuario selecionar uma variante
variante = st.sidebar.selectbox('Selecione a variante', ['Todas'] + variantes)

# Seleciona parte do dataframe que corresponde a seleção do usuario
if pais != 'Todos':
    st.header('Mostrando dados para ' + pais)
    df = df[df['location'] == pais]
    titulo = titulo + pais
else:
    st.header('Mostrando dados para todos os países')

if variante != 'Todas':
    st.text('Mostrando dados para a variante ' + variante)
    df = df[df['variant'] == variante]
    titulo = titulo + ' (variante : ' + variante + ')'
else:
    st.text('Mostrando dados para todas as variantes')
    titulo = titulo + '(todas as variantes)'

# Soma valores em outras colunas de acordo com a mesma data
dfShow = df.groupby(by=["date"]).sum()

# Cria figura
fig = px.line(dfShow, x=dfShow.index, y='num_sequences',
              labels={
                  dfShow.index: "Casos",
                  'num_sequences': "Datas"
              })
fig.update_layout(title=titulo)
st.plotly_chart(fig, use_container_width=True)
