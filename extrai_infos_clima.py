import os
import pandas as pd
from datetime import datetime, timedelta
from tabulate import tabulate

#definindo intervalo de datas
data_inicio = datetime.today()
print(data_inicio)
data_fim = data_inicio + timedelta(days=7)
print(data_fim)

#formatando as datas
data_inicio = data_inicio.strftime('%Y-%m-%d')
data_fim = data_fim.strftime('%Y-%m-%d')
print(data_inicio)
print(data_fim)

city = 'Boston'
key = 'NDZWKN7DY6AX2VQFH35HCTP52'

URL = join('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/', 
           f'{city}/{data_inicio}/{data_fim}?unitGroup=metric&include=days&key={key}&contentType=csv')

dados = pd.read_csv(URL)
print(dados.head())


file_path = f'/home/gabriel/Desktop/datapipeline/semana={data_inicio}/'
os.mkdir(file_path)

dados.to_csv(file_path + 'dados_brutos.csv')
dados[['datetime', 'tempmin', 'temp', 'tempmax']].to_csv(file_path + 'temperaturas.csv')
dados[['datetime','description','icon']].to_csv(file_path + 'condicoes.csv')