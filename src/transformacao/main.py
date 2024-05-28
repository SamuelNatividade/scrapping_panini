import pandas as pd
import sqlite3
import datetime
pd.options.display.max_columns = None

## Lendo dados
df = pd.read_json(r'/Users/samuelnatividade/Desktop/Projetos/amazon_scrapping/data/data.jsonl', lines = True)

## Filtrando dados nao nulos
df = df.dropna()


## Pegando o Volume do manga 
df[['manga','volume']] = df['nome'].str.split('Vol. ', n=1, expand = True)

## transformando a coluna preco para float
df['price'] = df['preco'].str.replace('R$', '')
df['price'] = df['price'].str.replace(',', '.').astype(float)

## dropando colunas 
df.drop(columns=['nome', 'preco'], inplace=True)
#print(df)


# Conectar ao banco de dados SQLite (ou criar um novo)
conn = sqlite3.connect('/Users/samuelnatividade/Desktop/Projetos/amazon_scrapping/data/panini.db')


## salvando dataframe no banco de dados
df.to_sql('panini', conn, if_exists='replace', index=False)

## fechando conexao
conn.close()