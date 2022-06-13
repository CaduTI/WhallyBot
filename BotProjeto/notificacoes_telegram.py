import pyodbc
from datetime import datetime
import requests
import builtins
import telebot
import time

api_key = "5191904654:AAFrD8ybCk8N06Xx4yVbSH2r-hsxQ6k7jxE"
bot = telebot.TeleBot(api_key)


conn = pyodbc.connect(Driver='SQL Server', host='DESKTOP-2RPK1J7', database='WhallyBot')
cur = conn.cursor()

now = datetime.now()
current_time = now.strftime("%H:%M")

print(current_time)
cur.execute('USE WhallyBot')
sql = 'SELECT* FROM EnvioEmail'
cur.execute(sql)
result = cur.fetchall()
print(result)
for c in result:
    if current_time =='18:57':
        chat_id = c[3]
        name = c[1]
        tag = c[4]
        moeda = c[5]
        print(chat_id)
        print(name)
        print(tag)
        print(moeda)
        if tag == 'BRL':
            request = requests.get(f'https://economia.awesomeapi.com.br/last/{tag}-USD')
            moeda_info = request.json()
            print(moeda_info)
            nome_tag = tag + 'USD'
            print(nome_tag)
            bid = moeda_info[nome_tag]['bid']
            text = f'Olá {name},Segue a cotação do {moeda}:{bid}'
            bot.send_message(chat_id, text)
        else:
            request = requests.get(f'https://economia.awesomeapi.com.br/last/{tag}')
            moeda_info = request.json()
            print(moeda_info)
            nome_dic = tag + 'BRL'
            print(nome_dic)
            bid = moeda_info[nome_dic]['bid']
            text = f'Olá {name},Segue a cotação do {moeda}:{bid}'
            bot.send_message(chat_id, text)


