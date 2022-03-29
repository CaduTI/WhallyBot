import json
import requests
import telebot

class Moeda:
    def __init__(self,nome):
        self.nome = nome
        self.valor= None


moeda_dict = {}
user = {}
api_key = "5191904654:AAFrD8ybCk8N06Xx4yVbSH2r-hsxQ6k7jxE"
bot = telebot.TeleBot(api_key)
@bot.message_handler(commands=["listarmoedas"])
def pegar_moeda(message):#pego a moeda que o usuário deseja
    #try:
        msg= message
        bot.send_message(msg.chat.id,"digite a moeda deseja")
        bot.register_next_step_handler(msg,consultar_cotacao)
    #except Exception as e:
     #   print(e)

def procura_tagmoeda_arquivo(message):#procuro dentro do XML a tag da moeda enviada pelo usuário
    pass
def consultar_cotacao(message):
    # try:
    msg= message
    moedanome= message.text
    moeda = Moeda(moedanome)
    print(moeda)
    request = requests.get('https://economia.awesomeapi.com.br/last/USD-{}'.format(moeda))
    moeda_info = request.json()
    bot.reply_to(msg, "Segue a cotação da moeda:")
    if 'erro' not in moeda_info:
        bot.send_message(format(moeda_info.bid))

    """except Exception as e:
        print(e)"""

@bot.message_handler(commands=['test'])
def teste(message):
    resposta_user= message.text
    print("texto da mensagem:", resposta_user)
    print("id do usuário", message.chat.id)


def verificar(message):
    return True


@bot.message_handler(func=verificar)
def menu_inicial(message):
    menu = """
    /listarmoedas
    /test
    """
    bot.reply_to(message, menu)


bot.polling()
