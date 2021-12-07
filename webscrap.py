"""
Webscrap para obter as notas da competicao atraves de uma requisicao do codigo HTML do site: bajasaebrasil.online utilizando a ferramenta BeutifulSoup

-2017
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd

"""
Obtendo a table que contem os dados de interesse pelo seu codigo HTML
"""

html_text = requests.get('https://resultados.bajasaebrasil.online/17BR/prova.php?id=17BR_GER').text
bs = BeautifulSoup(html_text, 'lxml')
table = bs.find('table', {'id':'myTable'})

"""
Obtendo as labels de cada coluna da tabela com a funcao find_all do BS4
"""
headers = []
for i in table.find_all('th'):
    title = i.text.strip()
    if title == "Total":
        headers.append(title)
        break
    headers.append(title)

"""
Criando o Dataframe com as colunas obtidas e preenchendo com os dados das linhas 
"""
df_2017 = pd.DataFrame(columns = headers)

for row in table.find_all('tr')[1:]:
    data = row.find_all('td')
    row_data = [td.text.strip() for td in data]
    length = len(df_2017) 
    df_2017.loc[length] = row_data
    
"""
Renomeando as colunas para melhor manejamento
"""

df_2017 = df_2017.rename(columns={"":"rank",
                        "Conforto":"conforto",
                        "Projeto":"projeto",
                        "Dinâmicas":"dinamica",
                        "Enduro":"enduro"
                        })

"""
Limpando o simbolo ordinal da classificacao e convertendo os dados em numericos
"""
df_2017['rank'] = df_2017['rank'].apply(lambda rank: rank.replace('º',''))

for column in df_2017:
    df_2017[column] = pd.to_numeric(df_2017[column], errors='coerce')
    
"""
Somando a nota de conforto com projeto por motivos de padronizacao na analise
Removendo colunas inuteis
"""
df_2017['projeto'] = df_2017['conforto'] + df_2017['projeto']
df_2017 = df_2017.drop(columns=['#','EquipeEscola', 'Doc/Seg/Mot', 'Total', 'conforto'])

"""
Repetindo o processo para as outras competicoes: 2018,2019,2020
-2018
"""

html_text2 = requests.get('https://resultados.bajasaebrasil.online/18BR/prova.php?id=18BR_GER').text
bs = BeautifulSoup(html_text2,'lxml')
table2 = bs.find('table',{'id':'myTable'})

headers2 = []

for i in table2.find_all('th'):
    title2 = i.text.strip()
    if title2 == "Total":
        headers2.append(title2)
        break
    headers2.append(title2)
    
df_2018 = pd.DataFrame(columns = headers2)

for row in table2.find_all('tr')[1:]:
    data2 = row.find_all('td')
    row_data2 = [td.text.strip() for td in data2]
    length2 = len(df_2018)
    df_2018.loc[length2] = row_data2

df_2018 = df_2018.rename(columns={"":"rank",
                                  "Projeto":"projeto",
                                  "Dinâmicas":"dinamica",
                                  "Enduro":"enduro"})
df_2018['rank'] = df_2018['rank'].apply(lambda rank: rank.replace('º',''))

for column in df_2018:
    df_2018[column] = pd.to_numeric(df_2018[column],errors='coerce')

df_2018 = df_2018.drop(columns=['#','EquipeEscola', 'Região', 'Segurança', 'Total'])
                         
"""
-2019
"""
html_text3 = requests.get('https://resultados.bajasaebrasil.online/19BR/prova.php?id=19BR_GER').text
bs = BeautifulSoup(html_text3,'lxml')
table3 = bs.find('table',{'id':'myTable'})

headers3 = []

for i in table3.find_all('th'):
    title3 = i.text.strip()
    if title3 == "Total":
        headers3.append(title3)
        break
    headers3.append(title3)
    
df_2019 = pd.DataFrame(columns = headers3)

for row in table3.find_all('tr')[1:]:
    data3 = row.find_all('td')
    row_data3 = [td.text.strip() for td in data3]
    length3 = len(df_2019) 
    df_2019.loc[length3] = row_data3

df_2019 = df_2019.rename(columns={"":"rank",
                                  "Projeto":"projeto",
                                  "Dinâmicas":"dinamica",
                                  "Enduro":"enduro"})
df_2019['rank'] = df_2019['rank'].apply(lambda rank: rank.replace('º',''))

for column in df_2019:
    df_2019[column] = pd.to_numeric(df_2019[column],errors='coerce')

df_2019 = df_2019.drop(columns=['#','EquipeEscola', 'Região', 'Penalidade' ,'Segurança', 'Total'])
    
"""
-2020
"""         
html_text4 = requests.get('https://resultados.bajasaebrasil.online/20BR/prova.php?id=20BR_GER').text
bs = BeautifulSoup(html_text4,'lxml')
table4 = bs.find('table',{'id':'myTable'})

headers4 = []

for i in table4.find_all('th'):
    title4 = i.text.strip()
    if title4 == "Total":
        headers4.append(title4)
        break
    headers4.append(title4)
    
df_2020 = pd.DataFrame(columns = headers4)

for row in table4.find_all('tr')[1:]:
    data4 = row.find_all('td')
    row_data4 = [td.text.strip() for td in data4]
    length4 = len(df_2020) 
    df_2020.loc[length4] = row_data4

df_2020 = df_2020.rename(columns={"":"rank",
                                  "Projeto":"projeto",
                                  "Dinâmicas":"dinamica",
                                  "Enduro":"enduro"})
df_2020['rank'] = df_2020['rank'].apply(lambda rank: rank.replace('º',''))

for column in df_2020:
    df_2020[column] = pd.to_numeric(df_2020[column],errors='coerce')

df_2020 = df_2020.drop(columns=['#','EquipeEscola', 'Região', 'Penalidade' ,'Segurança', 'Total'])   

      