'''
Этот файл содержит пример кода, который читае .csv
и после преобрразования формирует файл .xlsx
'''
from datetime import datetime

import openpyxl
import pandas as pd

today = datetime.now()
cols = ['OrderDate', 'Region', 'Item', 'Units']

df = pd.read_csv('sales.csv', usecols = cols)
print(f'today is', today)

df['OrderDate'] = pd.to_datetime(df['OrderDate'])
df = df.sort_values(by=['OrderDate'])
print(df)
