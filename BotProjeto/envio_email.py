
import smtplib as smtp
from email.message import EmailMessage
import requests
import json
import pyodbc
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



now = datetime.now()
current_time = now.strftime("%H:%M")
print(current_time)

conn = pyodbc.connect(Driver='SQL Server', host='DESKTOP-2RPK1J7', database='WhallyBot')
cur = conn.cursor()
# Configurar email, senha
login = "botwally99@gmail.com"
senha = 'bot12345$'
host = "smtp.gmail.com"
port = "587"


server = smtp.SMTP(host, port)
server.ehlo()
server.starttls()
server.login(login, senha)


now = datetime.now()
current_time = now.strftime("%H:%M")

print(current_time)
cur.execute('USE WhallyBot')
sql = 'SELECT* FROM EnvioEmail'
cur.execute(sql)
result = cur.fetchall()
print(result)
#usar o for e if para percorer as lihas do retorno
for c in result:
    if current_time =='18:58':
        email_cliente = c[2]
        name = c[1]
        tag = c[4]
        moeda = c[5]
        print(email_cliente)
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
            text = f"""Olá {name},


                    Segue a cotação do {moeda}:{bid}.


                    Att : Equipe WhallyBot
            """

            email_msg = MIMEMultipart()
            email_msg['From'] = login
            email_msg['To'] = email_cliente
            email_msg['Subject'] = f"Envio diário da cotação do {moeda}"
            email_msg.attach(MIMEText(text, 'Plain'))
            server.sendmail(email_msg['From'], email_cliente, email_msg.as_string())
        else:
            request = requests.get(f'https://economia.awesomeapi.com.br/last/{tag}')
            moeda_info = request.json()
            print(moeda_info)
            nome_dic = tag + 'BRL'
            print(nome_dic)
            bid = moeda_info[nome_dic]['bid']
            text = f"""Olá {name},


                    Segue a cotação do {moeda}:{bid}.


                    Att : Equipe WhallyBot
            """

            email_msg = MIMEMultipart()
            email_msg['From'] = login
            email_msg['To'] = email_cliente
            email_msg['Subject'] = f"Envio diário da cotação do {moeda}"
            email_msg.attach(MIMEText(text, 'Plain'))
            server.sendmail(email_msg['From'], email_cliente, email_msg.as_string())

        #server.quit()
