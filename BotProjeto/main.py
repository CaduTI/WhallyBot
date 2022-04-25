import requests
import telebot
import re

moeda_dict = {}
user = {}
api_key = "5191904654:AAFrD8ybCk8N06Xx4yVbSH2r-hsxQ6k7jxE"
bot = telebot.TeleBot(api_key)


@bot.message_handler(commands=['DolarAmericano'])
def dolar(message):
    try:
        request = requests.get('https://economia.awesomeapi.com.br/last/USD')
        moeda_info = request.json()
        print(moeda_info)
        print(request)
        bot.reply_to(message, " 💸 Segue a cotação da moeda:{}.Deseja algo a mais?".format(moeda_info['USDBRl']['bid']))
        bot.register_next_step_handler(message, sugestao)
    except Exception as e:
        print(e)


@bot.message_handler(commands=["RealBrasileiro"])
def real(message):
    try:
        request = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')
        moeda_info = request.json()
        print(moeda_info)
        print(request)
        bot.reply_to(message, " 💸 Segue a cotação da moeda:{}.Deseja algo a mais?".format(moeda_info['USDBRL']['bid']))
        bot.register_next_step_handler(message, sugestao)
    except Exception as e:
        print(e)


@bot.message_handler(commands=["KwanzaAngolano"])
def kwanza(message):
    try:
        request = requests.get('https://economia.awesomeapi.com.br/last/KWA')
        moeda_info = request.json()
        print(moeda_info)
        print(request)

        bot.reply_to(message, " 💸 Segue a cotação da moeda:{}.Deseja algo a mais?".format(moeda_info['AOABRL']['bid']))
        bot.register_next_step_handler(message, sugestao)
    except Exception as e:
        print(e)


@bot.message_handler(commands=["Euro"])
def euro(message):
    try:
        request = requests.get('https://economia.awesomeapi.com.br/last/EUR')
        moeda_info = request.json()
        print(moeda_info)
        print(request)

        bot.reply_to(message, " 💸 Segue a cotação da moeda:{}.Deseja algo a mais?".format(moeda_info['EURBRL']['bid']))
        bot.register_next_step_handler(message, sugestao)
    except Exception as e:
        print(e)


@bot.message_handler(commands=["PesoArgentino"])
def peso_arg(message):
    try:
        request = requests.get('https://economia.awesomeapi.com.br/last/ARS')
        moeda_info = request.json()
        print(moeda_info)
        print(request)

        bot.reply_to(message, " 💸 Segue a cotação da moeda:{}.Deseja algo a mais?".format(moeda_info['ARSBRL']['bid']))
        bot.register_next_step_handler(message, sugestao)
    except Exception as e:
        print(e)


@bot.message_handler(commands=["Rublo"])
def rublo(message):
    try:
        request = requests.get('https://economia.awesomeapi.com.br/last/RUB')
        moeda_info = request.json()
        print(moeda_info)
        print(request)

        bot.reply_to(message, " 💸 Segue a cotação da moeda:{}.Deseja algo a mais?".format(moeda_info['RUBBRL']['bid']))
        bot.register_next_step_handler(message, sugestao)
    except Exception as e:
        print(e)


@bot.message_handler(commands=["FrancoSuico"])
def franco_sui(message):
    try:
        request = requests.get('https://economia.awesomeapi.com.br/last/CHF')
        moeda_info = request.json()
        print(moeda_info)
        print(request)

        bot.reply_to(message, " 💸 Segue a cotação da moeda:{}.Deseja algo a mais?".format(moeda_info['CHFBRL']['bid']))
        bot.register_next_step_handler(message, sugestao)
    except Exception as e:
        print(e)


@bot.message_handler(commands=["DolarCanadense"])
def dolar_canada(message):
    try:

        request = requests.get('https://economia.awesomeapi.com.br/last/CAD')
        moeda_info = request.json()
        print(moeda_info)
        print(request)

        bot.reply_to(message, " 💸 Segue a cotação da moeda:{}.Deseja algo a mais?".format(moeda_info['CADBRL']['bid']))
        bot.register_next_step_handler(message, sugestao)
    except Exception as e:
        print(e)


@bot.message_handler(commands=["Dogecoin"])
def dogecoin(message):
    try:
        request = requests.get('https://economia.awesomeapi.com.br/last/DOGE')
        moeda_info = request.json()
        print(moeda_info)
        print(request)

        bot.reply_to(message, " 💸 Segue a cotação da moeda:{}.Deseja algo a mais?".format(moeda_info['DOGEBRL']['bid']))
        bot.register_next_step_handler(message, sugestao)
    except Exception as e:
        print(e)


@bot.message_handler(commands=["Bitcoin"])
def bitcoin(message):
    try:
        request = requests.get('https://economia.awesomeapi.com.br/last/BTC')
        moeda_info = request.json()
        bot.reply_to(message, " 💸 Segue a cotação da moeda:{}.Deseja algo a mais?".format(moeda_info['BTCBRL']['bid']))
        bot.register_next_step_handler(message, sugestao)
    except Exception as e:
        print(e)


@bot.message_handler(commands=["Ethereum"])
def ethereum(message):
    try:
        request = requests.get('https://economia.awesomeapi.com.br/last/ETH')
        moeda_info = request.json()
        bot.reply_to(message, " 💸 Segue a cotação da moeda:{}.Deseja algo a mais?".format(moeda_info['ETHBRL']['bid']))
        bot.register_next_step_handler(message, sugestao)
    except Exception as e:
        print(e)


def sugestao(message):
    box = """
    Gostaria de cadastrar seu email? fácil e prático não demorará nada 😊:
    
    /Sim
    /Nao
    """
    bot.send_message(message.chat.id, box)
    decisao = message.text
    if decisao == 'Sim':
        bot.register_next_step_handler(message, aceita)
    if decisao == 'Nao':
        bot.register_next_step_handler(message, recusa)


@bot.message_handler(commands=['Sim'])
def aceita(message):
    bot.reply_to(message, "Por favor, poderia enviar email?  ")
    bot.register_next_step_handler(message, valida_email)


def valida_email(message):
    try:
        #regex = '[^a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}'
        email = message.text

        if re.search(r'^[a-z0-9]?[a-z0-9]+[@]\w+[.]\w{2,3}$', email):
            bot.reply_to(message, "Agradecemos a preferência")
            bot.register_next_step_handler(message, moeda)
        else:
            bot.reply_to(message, "Ooops, email inválido 😰😰😰")
            bot.register_next_step_handler(message, aceita)
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
        "DolarAmericano": "USD",
        "RealBrasileiro": "BRL",
        "KwanzaAngolano": "AOA",
        "Euro": "EUR",
        "PesoArgentina": "ARG",
        "Rublo": "RUB",
        "Franco": "CHF",
        "DolarCanadense": "CAD",
        "Dogecoin": "DOGE",
        "Bitcoin": "BTC",
        "Ethereum": "ETH"
    }
    contador = message.text
    for contador in moedas.keys():
        if contador in moedas:
            bot.register_next_step_handler(message, cadastro)


def cadastro(message):
    pass


@bot.message_handler(commands=['Nao'])
def recusa(message):
    bot.reply_to(message, "Agradecemos a preferência 😊😊😊.")
    bot.register_next_step_handler(message, menu_inicial)


@bot.message_handler(commands=['WhallyBot'])
def teste(message):
    whally_text = """
    O WhallyBot é um bot para visualização e recebimento de cotações de moedas em tempo real,
    temos o envio por email(caso deseja se cadastrar),
    caso contrário temos o envio da cotação pelo canal do telegram.
    """
    bot.send_message(message.chat.id, whally_text)


@bot.message_handler(commands=['Moedas'])
def menu_moedas(message):
    moedas = """
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
    bot.send_message(message.chat.id, moedas)


def verificar(message):
    return True


@bot.message_handler(func=verificar)
def menu_inicial(message):
    menu = """
     📢 Seja Bem vindo ao WhallyBot, por favor selecione uma de nossas opções para cotação:
    /Moedas 🤑
    /WhallyBot 🤖

    """
    bot.reply_to(message, menu)
    print(message)

bot.polling()
