import requests
import telebot
import re
import pyodbc
from datetime import datetime

user_dict = {}
api_key = "5191904654:AAFrD8ybCk8N06Xx4yVbSH2r-hsxQ6k7jxE"
bot = telebot.TeleBot(api_key)

#############SQL CONECTION#############
conn = pyodbc.connect(Driver='SQL Server', host='DESKTOP-2RPK1J7', database='WhallyBot')
cur = conn.cursor()
print("Estamos Conectado em nossa base")


now = datetime.now()
current_time = now.strftime("%H:%M")
print(current_time)

"""def daily_message():
    cur.execute('USE WhallyBot')
    sql = 'SELECT* FROM EnvioEmail'
    #usar o for e if para percorer as lihas do retorno
    request = requests.get('https://economia.awesomeapi.com.br/last/{tag da moeda do cara}')
    text = 'Olá {nome do cliente},Segue a cotação do{nome moeda}:{cotação}'
    telegram = "message.chat.id"
    ret_msg = bot.send_message(telegram, text)
    if currenttime= ='17:30':
        bot.send_message(idchat, "mymessage")
    return ret_msg.message_id
    """

class User:
    def __init__(self, name):
        self.name = name
        self.email = None


@bot.message_handler(commands=['WhallyBot'])
def teste(message):
    whally_text = """
    O WhallyBot é um bot para visualização e recebimento de cotações de moedas em tempo real,
    temos o envio por email(caso deseja se cadastrar),
    caso contrário temos o envio da cotação pelo canal do telegram.
    """
    bot.send_message(message.chat.id, whally_text)


@bot.message_handler(commands=['help', 'start', 'oi', 'ola', 'Ola'])
def menu_inicial(message):
    menu = """
     📢 Seja Bem vindo ao WhallyBot, por favor selecione uma de nossas opções para cotação:
    /Moedas 🤑
    /WhallyBot 🤖

    """
    bot.reply_to(message, menu)


@bot.message_handler(commands=['Moedas'])
def menu_moedas(message):
    moedas = """
    /DolarAmericano
    /RealBrasileiro
    /KwanzaAngolano
    /Euro
    /PesoArgentino
    /Rublo
    /Franco
    /DolarCanadense
    /Dogecoin
    /Bitcoin
    /Ethereum
    """
    bot.send_message(message.chat.id, moedas)


@bot.message_handler(commands=['DolarAmericano'])
def dolar(message):
   try:
       if True:
           box = """
        💸 Segue a cotação da moeda:{}, deseja algo a mais? 
        Gostaria de cadastrar seu email? fácil e prático não demorará nada 😊:

        /Sim
        /Nao"""
           request = requests.get('https://economia.awesomeapi.com.br/last/USD')
           moeda_info = request.json()
           print(moeda_info)
           print(request)

           bot.reply_to(message, box.format(moeda_info['USDBRL']['bid']))
       bot.register_next_step_handler(message, sugestao)
   except Exception as e:
       print(e)


@bot.message_handler(commands=["RealBrasileiro"])
def real(message):
   try:
       if True:
           box = """
            💸 Segue a cotação da moeda:{}, deseja algo a mais? 
            Gostaria de cadastrar seu email? fácil e prático não demorará nada 😊:

            /Sim
            /Nao"""
           request = requests.get('https://economia.awesomeapi.com.br/last/BRL-USD')
           moeda_info = request.json()
           print(moeda_info)
           print(request)

           bot.reply_to(message, box.format(moeda_info['BRLUSD']['bid']))
       bot.register_next_step_handler(message, sugestao)
   except Exception as e:
       print(e)


@bot.message_handler(commands=["KwanzaAngolano"])
def kwanza(message):
   try:
       if True:
           box = """
            💸 Segue a cotação da moeda:{}, deseja algo a mais? 
            Gostaria de cadastrar seu email? fácil e prático não demorará nada 😊:

            /Sim
            /Nao"""
           request = requests.get('https://economia.awesomeapi.com.br/last/AOA')
           moeda_info = request.json()
           print(moeda_info)
           print(request)

           bot.reply_to(message, box.format(moeda_info['AOABRL']['bid']))
       bot.register_next_step_handler(message, sugestao)
   except Exception as e:
       print(e)


@bot.message_handler(commands=["Euro"])
def euro(message):
   try:
       if True:
           box = """
        💸 Segue a cotação da moeda:{}, deseja algo a mais? 
        Gostaria de cadastrar seu email? fácil e prático não demorará nada 😊:

        /Sim
        /Nao"""
           request = requests.get('https://economia.awesomeapi.com.br/last/EUR')
           moeda_info = request.json()
           print(moeda_info)
           print(request)

           bot.reply_to(message, box.format(moeda_info['EURBRL']['bid']))
       bot.register_next_step_handler(message, sugestao)
   except Exception as e:
       print(e)


@bot.message_handler(commands=["PesoArgentino"])
def peso(message):
   try:
       if True:
           box = """
        💸 Segue a cotação da moeda:{}, deseja algo a mais? 
        Gostaria de cadastrar seu email? fácil e prático não demorará nada 😊:

        /Sim
        /Nao"""
           request = requests.get('https://economia.awesomeapi.com.br/last/ARS')
           moeda_info = request.json()
           print(moeda_info)
           print(request)

           bot.reply_to(message, box.format(moeda_info['ARSBRL']['bid']))
       bot.register_next_step_handler(message, sugestao)
   except Exception as e:
       print(e)


@bot.message_handler(commands=["Rublo"])
def rublo(message):
   try:
       if True:
           box = """
        💸 Segue a cotação da moeda:{}, deseja algo a mais? 
        Gostaria de cadastrar seu email? fácil e prático não demorará nada 😊:

        /Sim
        /Nao"""
           request = requests.get('https://economia.awesomeapi.com.br/last/RUB')
           moeda_info = request.json()
           print(moeda_info)
           print(request)

           bot.reply_to(message, box.format(moeda_info['RUBBRL']['bid']))
       bot.register_next_step_handler(message, sugestao)
   except Exception as e:
       print(e)


@bot.message_handler(commands=["Franco"])
def franco(message):
   try:
       if True:
           box = """
        💸 Segue a cotação da moeda:{}, deseja algo a mais? 
        Gostaria de cadastrar seu email? fácil e prático não demorará nada 😊:

        /Sim
        /Nao"""
           request = requests.get('https://economia.awesomeapi.com.br/last/CHF-BRL')
           moeda_info = request.json()
           print(moeda_info)
           print(request)

           bot.reply_to(message, box.format(moeda_info['CHFBRL']['bid']))
       bot.register_next_step_handler(message, sugestao)
   except Exception as e:
       print(e)


@bot.message_handler(commands=["DolarCanadense"])
def dolar_cad(message):
   try:
       if True:
           box = """
        💸 Segue a cotação da moeda:{}, deseja algo a mais? 
        Gostaria de cadastrar seu email? fácil e prático não demorará nada 😊:

        /Sim
        /Nao"""
           request = requests.get('https://economia.awesomeapi.com.br/last/CAD')
           moeda_info = request.json()
           print(moeda_info)
           print(request)

           bot.reply_to(message, box.format(moeda_info['CADBRL']['bid']))
       bot.register_next_step_handler(message, sugestao)
   except Exception as e:
       print(e)


@bot.message_handler(commands=["Dogecoin"])
def dogecoin(message):
   try:
       if True:
           box = """
            💸 Segue a cotação da moeda:{}, deseja algo a mais? 
            Gostaria de cadastrar seu email? fácil e prático não demorará nada 😊:

            /Sim
            /Nao"""
           request = requests.get('https://economia.awesomeapi.com.br/last/DOGE')
           moeda_info = request.json()
           print(moeda_info)
           print(request)

           bot.reply_to(message, box.format(moeda_info['DOGEBRL']['bid']))
       bot.register_next_step_handler(message, sugestao)
   except Exception as e:
       print(e)


@bot.message_handler(commands=["Bitcoin"])
def bitcoin(message):
   try:
       if True:
           box = """
            💸 Segue a cotação da moeda:{}, deseja algo a mais? 
            Gostaria de cadastrar seu email? fácil e prático não demorará nada 😊:

            /Sim
            /Nao"""

           request = requests.get('https://economia.awesomeapi.com.br/last/BTC')
           moeda_info = request.json()
           print(moeda_info)
           print(request)

           bot.reply_to(message, box.format(moeda_info['BTCBRL']['bid']))
       bot.register_next_step_handler(message, sugestao)
   except Exception as e:
       print(e)


@bot.message_handler(commands=["Ethereum"])
def ethereum(message):
   try:
       if True:
           box = """
            💸 Segue a cotação da moeda:{}, deseja algo a mais? 
            Gostaria de cadastrar seu email? fácil e prático não demorará nada 😊:

            /Sim
            /Nao"""
           request = requests.get('https://economia.awesomeapi.com.br/last/ETH')
           moeda_info = request.json()
           print(moeda_info)
           print(request)

           bot.reply_to(message, box.format(moeda_info['ETHBRL']['bid']))

       bot.register_next_step_handler(message, sugestao)
   except Exception as e:
       print(e)


def sugestao(message):
    decision_final = """
    Tem certeza que deseja realizar o cadastro?
    /Sim
    /Nao
    """

    bot.send_message(message.chat.id, decision_final)
    decisao = message.text
    if decisao == 'Sim':
        bot.register_next_step_handler(message, pega_nome)
    if decisao == 'Nao':
        bot.register_next_step_handler(message, recusa)


@bot.message_handler(commands=['Sim'])
def pega_nome(message):
    telegram_id = message.chat.id
    bot.send_message(telegram_id, "Qual o seu nome?")
    bot.register_next_step_handler(message, pega_email)

def pega_email(message):
    telegram_id = message.chat.id
    name = message.text
    user = User(name)
    user_dict[name] = user.name
    user_dict[telegram_id] = user
    bot.send_message(telegram_id, "Por favor, poderia enviar email?  ")
    bot.register_next_step_handler(message, valida_email)


def valida_email(message):
    try:
        email = message.text
        if re.search(r'^([a-z]){1,}([a-z0-9._-]){1,}([@]){1}([a-z]){2,}([.]){1}([a-z]){2,}([.]?){1}([a-z]?){2,}$', email):
            user_dict[email] = email
            User.email = email
            print(User.email)
            telegram_id = message.chat.id
            bot.reply_to(message, "Obrigado por enviar seu email, digite 'Bot' para prosseguirmos")
            bot.register_next_step_handler(message, moeda)
        else:
            bot.reply_to(message, "Ooops, email inválido 😰😰😰")
            bot.register_next_step_handler(message, pega_email)
    except Exception as e:
        print(e)


def moeda(message):
    moedas = """
    Por favor, escolha uma das moedas para receber as notifcações diárias:
    
    /DolarAmericano
    /RealBrasileiro
    /KwanzaAngolano
    /Euro
    /PesoArgentina
    /Rublo
    /Franco
    /DolarCanadense
    /Dogecoin
    /Bitcoin
    /Ethereum
        """
    bot.reply_to(message, moedas)
    bot.register_next_step_handler(message, moeda_insert)


def moeda_insert(message):
    moedas = {
        "/DolarAmericano": "USD",
        "/RealBrasileiro": "BRL",
        "/KwanzaAngolano": "AOA",
        "/Euro": "EUR",
        "/PesoArgentina": "ARG",
        "/Rublo": "RUB",
        "/Franco": "CHF",
        "/DolarCanadense": "CAD",
        "/Dogecoin": "DOGE",
        "/Bitcoin": "BTC",
        "/Ethereum": "ETH"
    }
    #investigar o pq de ir cadastrado na base como / junto do nome da moeda
    telegram_id = message.chat.id
    nome_moeda = message.text
    if nome_moeda in moedas:
        tag = moedas.get(nome_moeda)
    user_dict['nome_moeda'] = nome_moeda
    user_dict['tag'] = tag
    print(user_dict)
    user = user_dict[telegram_id]
    print(user)
    bot.send_message(telegram_id, "Obrigado por se cadastrar, ")
    bot.register_next_step_handler(message, cadastro)


def cadastro(message):
    telegram_id = message.chat.id
    user = user_dict[telegram_id]
    tag = user_dict.get('tag')
    moeda = user_dict.get('nome_moeda')
    cur.execute("USE WhallyBot")
    #realizar um alter table e aumentar o slot das tags
    sql = f"INSERT INTO EnvioEmail(Nome, Email, Id_Telegram,Tag_Moeda, Moeda_Nome) values ('{user.name}', '{user.email}', '{telegram_id}', '{tag}', '{moeda}')"
    cur.execute(sql)
    conn.commit()
    cur.close()
    bot.send_message(telegram_id, "Cadastro efetudo com sucesso, nossas notificações são enviadas no período da manhã 😄😄😄😄")


@bot.message_handler(commands=['Nao'])
def recusa(message):
    bot.reply_to(message, "Agradecemos a preferência 😊😊😊.")
    bot.register_next_step_handler(message, menu_inicial)


bot.polling()
