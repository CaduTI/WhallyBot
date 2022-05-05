import requests
import telebot
import re
from classes import Usuario


user_dict = {}
api_key = "5191904654:AAFrD8ybCk8N06Xx4yVbSH2r-hsxQ6k7jxE"
bot = telebot.TeleBot(api_key)


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
    bot.register_next_step_handler(message, get_bid)


def get_bid(message):
    moedas_dict = {
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
    nome = message.text
    for nome in moedas_dict.keys():
        if nome in moedas_dict:
            tag = moedas_dict.get(nome)
            request = requests.get('https://economia.awesomeapi.com.br/last/{}'.format(tag))
            request_json = request.json()
            print(request_json)
            bot.reply_to(message, " 💸 Segue a cotação da moeda:{}.Deseja algo a mais?".format(request_json[f'{moedas_dict.get(nome)}BRL']['bid']))
            bot.register_next_step_handler(message, sugestao)
        if moedas_dict.get(nome) == 'BRL':
            request = requests.get('https://economia.awesomeUSDapi.com.br/last/-BRL/')
            moeda_info = request.json()
            bot.reply_to(message, " 💸 Segue a cotação da moeda:{}.Deseja algo a mais?".format(moeda_info['USDBRl']['bid']))
            bot.register_next_step_handler(message, sugestao)


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
            tag = moedas.get(contador)
            #adicionar a tag da moeda no dicionário da mesma, após isso registar como atributo na classe usuario
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
