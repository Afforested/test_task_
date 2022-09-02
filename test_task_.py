import numpy as np
import pandas as pd

original_df = pd.read_csv('G:/DataspellProjects/dsProject/dataframes_/test_data.csv')
df = original_df.copy()

#Создаем столбец(и, на всякий случай дополнительный датафрейм), где менеджер поздоровался:
df['greeting'] = (df['text'].str.contains('здравствуйте|добрый день|доброе утро|добрый вечер', case=False)) & (df['role'] == 'manager')
greeting = df[(df['text'].str.contains('здравствуйте|добрый день|доброе утро|добрый вечер', case=False)) & (df['role'] == 'manager')]


#Создаем столбец(и, на всякий случай дополнительный датафрейм), где менеджер представился:
df['present'] = (df['text'].str.contains('меня зовут', case=False)) & (df['role'] == 'manager')
present = df[(df['text'].str.contains('меня зовут', case=False)) & (df['role'] == 'manager')]


#Извлекаем имя менеджера:
manager_name = df[(df['text'].str.contains('меня зовут', case=False))& (df['role'] == 'manager')].drop(['text'], axis=1).join(df[(df['text'].str.contains('меня зовут', case=False))& (df['role'] == 'manager')].text.apply(lambda x: x.lower().split('меня зовут')[1].split()[0]))[['dlg_id', 'line_n', 'text']].rename(columns={'text': 'manager_name'})


#Извлекаем имя компании:
company_name = df[(df['text'].str.contains('зовут', case=False)) & (df['text'].str.contains('компания', case=False)) & (df['role'] == 'manager')].drop(['text'], axis=1).join(df[(df['text'].str.contains('зовут', case=False)) & (df['text'].str.contains('компания', case=False)) & (df['role'] == 'manager')].text.apply(lambda x: ''.join(x.split('компания')[1].partition('бизнес')[:2]).strip()))[['dlg_id', 'line_n', 'text']].rename(columns={'text': 'company_name'})


#Создаем столбец(и, на всякий случай дополнительный датафрейм), где менеджер попрощался:
df['farewell'] = df['text'].str.contains('до свидания|до завтра|до встречи', case=False) & (df['role'] == 'manager')
farewell = df[df['text'].str.contains('до свидания|до завтра|до встречи', case=False) & (df['role'] == 'manager')]

#Извлекаем диалоги, в которых менеджер и поздоровался, и попрощался:
hello_and_goodbye = df[['dlg_id']].join(df[['dlg_id']].isin(greeting[['dlg_id']].merge(farewell[['dlg_id']])['dlg_id'].to_list()).rename({'dlg_id': 'hello_and_goodbye'}, axis=1)).drop_duplicates()




