import streamlit as st
import pandas as pd
import sqlite3

conn = sqlite3.connect('/Users/samuelnatividade/Desktop/Projetos/amazon_scrapping/data/panini.db')


## total de mangas distintos 
contagem_mangas = pd.read_sql_query('''SELECT 
                                        count(DISTINCT manga) AS quantidade_de_mangas
                                    FROM panini p
                                    '''
                                    ,conn)


## contagem de mangas ate a pagina 10
page_10 = pd.read_sql_query('''SELECT 
                        manga 
                        ,count(manga)
                    FROM panini p
                    WHERE p.pagina <= 10
                    GROUP BY 1
                    ORDER BY 2 DESC
                       '''
                    ,conn
                    )

media_global = pd.read_sql_query('''
                                SELECT 
                                        round(avg(price),2) AS media_global
                                    FROM panini p
                                 ''', conn)


media_por_manga = pd.read_sql_query('''
                                SELECT 
                                        manga               AS manga
                                        ,round(avg(price),2) AS media_global
                                    FROM panini p
                                    GROUP BY 1
                                    ORDER BY 2 DESC
                                    ''', conn)


manga_mais_caro = pd.read_sql_query('''SELECT 
                                        manga
                                        ,max(price)
                                    FROM panini p 
                                    GROUP BY 1
                                    LIMIT 1''',conn)

## fechando conexao
conn.close()

## titulo da aplicacao
st.title('Indicadores interessantes da Panini')

col1, col2 = st.columns(2)

col1.metric(label = 'Numero de Mangás diferentes', value = contagem_mangas)
col2.metric(label = 'manga_mais_caro', value = manga_mais_caro)


