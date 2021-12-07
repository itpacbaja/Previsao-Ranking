# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 03:27:16 2021

@author: lueij
"""
from bs4 import BeautifulSoup 
import requests
import pandas as pd
import numpy as np

#NACIONAL 2017 - NOTA RELATORIO
#extraindo o codigo HTML

html_text = requests.get('https://resultados.bajasaebrasil.online/17BR/prova.php?id=17BR_REL').text
bs = BeautifulSoup(html_text, 'lxml')

#extraindo o header
table = bs.find('table', {'id':'myTable'})

headers = []

for i in table.find_all('th'):
    title = i.text.strip()
    headers.append(title)

headers.remove('Prova FinalizadaÚltima Atualização: 2018-02-21 23:55:56')
df = pd.DataFrame(columns = headers)

#inserindo os dados da tabela no dataframe
for row in table.find_all('tr')[1:]:
    data = row.find_all('td')
    row_data = [td.text.strip() for td in data]
    length = len(df)
    df.loc[length] = row_data

#removendo colunas inuteis
df = df.drop(columns=['EquipeEscola','Nota','Penalizações','Motivo'])
df = df.rename(columns={"":"rank",
                        "#":"num",
                        "Pontos":"nota"
                        })

#removendo caracteres especiais
def corrigir_rank(rank):
    rank = rank.replace('º','')
    return rank

df['rank'] = df['rank'].apply(corrigir_rank)

#NACIONAL 2017 - NOTA APRESENTACAO

html_text2 = requests.get('https://resultados.bajasaebrasil.online/17BR/prova.php?id=17BR_APR').text
bs = BeautifulSoup(html_text2, 'lxml')

#extraindo o header
table2 = bs.find('table', {'id':'myTable'})

headers2 = []

for i in table2.find_all('th'):
    title2 = i.text.strip()
    headers2.append(title2)

headers2.remove('Prova FinalizadaÚltima Atualização: 2018-02-21 23:55:56')
df2 = pd.DataFrame(columns = headers2)

#inserindo os dados da tabela no dataframe 2
for row2 in table2.find_all('tr')[1:]:
    data2 = row2.find_all('td')
    row_data2 = [td.text.strip() for td in data2]
    length2 = len(df2)
    df2.loc[length2] = row_data2

df2 = df2.drop(columns=['EquipeEscola','Powertrain','Eletr.','Freios','Design','Susp/Dir.','Vendas / Mkt','Calculo','Gestão','Presente'])
df2 = df2.rename(columns={"":"rank",
                          "#":"num",
                          "Pontos":"nota"})

df2['rank'] = df2['rank'].apply(corrigir_rank)

#NACIONAL 2017 - NOTA CONFORTO

html_text3 = requests.get('https://resultados.bajasaebrasil.online/17BR/prova.php?id=17BR_CON').text
bs = BeautifulSoup(html_text3, 'lxml')

#extraindo o header
table3 = bs.find('table', {'id':'myTable'})

headers3 = []

for i in table3.find_all('th'):
    title3 = i.text.strip()
    headers3.append(title3)

headers3.remove('Prova FinalizadaÚltima Atualização: 2018-02-21 23:55:56')
df3 = pd.DataFrame(columns = headers3)

#inserindo os dados da tabela no dataframe 2
for row3 in table3.find_all('tr')[1:]:
    data3 = row3.find_all('td')
    row_data3 = [td.text.strip() for td in data3]
    length3 = len(df3)
    df3.loc[length3] = row_data3

df3 = df3.drop(columns=['EquipeEscola','Status'])
df3 = df3.rename(columns={"":"rank",
                          "#":"num",
                          "Pontos":"nota"})

df3['rank'] = df3['rank'].apply(corrigir_rank)

#NOTA PROJETO = APRESENTACAO + CONFORTO + RELATORIO

frames = [df,df2,df3]
df_projeto_2017 = pd.concat(frames)

df_projeto_2017['nota'] = pd.to_numeric(df_projeto_2017['nota'], errors='coerce')
df_projeto_2017['num'] = pd.to_numeric(df_projeto_2017['num'], errors='coerce')
df_projeto_2017 = df_projeto_2017.groupby(['num']).sum()
df_projeto_2017 = df_projeto_2017.sort_values(by=['nota'], ascending=False)


df_projeto_2017.insert(1,"rank", "")
#df_projeto_2017['rank'] = pd.to_numeric(df_projeto_2017['rank'], errors='coerce')

df_projeto_2017['rank'] = df_projeto_2017['nota'].rank(method='min',ascending= False)
#df_projeto_2017 = df_projeto_2017.sort_values(by=['num'], ascending=True)

"""
ja existe uma tabela com todas as informacoes que foram obtidas aqui

"""