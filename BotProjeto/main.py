import requests
import telebot
from xml.dom import minidom


class Moeda:
    def __init__(self, nome):
        self.nome = nome
        self.valor = None


moeda_dict = {}
user = {}
api_key = "5191904654:AAFrD8ybCk8N06Xx4yVbSH2r-hsxQ6k7jxE"
bot = telebot.TeleBot(api_key)


@bot.message_handler(commands=["listarmoedas"])
def pegar_moeda(message):
    """pego a moeda que o usuário deseja"""
    try:
        bot.send_message(message.chat.id, "digite a moeda deseja")
        bot.register_next_step_handler(message, procura_tagmoeda_arquivo)
    except Exception as e:
       print(e)


def procura_tagmoeda_arquivo(message):#procuro dentro do XML a tag da moeda enviada pelo usuário
    try:
        moedanome = message.text
        with open('tagmoedas.xml','r', enconding='utf-8') as f:
            xml = minidom.parse(f)
            #moeda_nome = xml.getElementstree(moedanome)

            for tag in xml:
                if f [''] == moedanome:
                    print(f['0'])
    #vai fazer a BUSCA DENTRO DO XML com o nome da moeds ue o cliente digitou, caso ele n ache vai pro except
    except Exception as e:
        print(e)
        #RaiseException("Deu ruim patrão, digita certo ae")
def consultar_cotacao(message):
     try:

        tagmoeda = message.text
        print(tagmoeda)
        if True:
            request = requests.get('https://economia.awesomeapi.com.br/last/USD-{}'.format(tagmoeda))
            moeda_info = request.json()
            print(moeda_info)
            print(request)
            
            bot.reply_to(message, "Segue a cotação da moeda:{}".format(moeda_info['USD']['bid']))
     except Exception as e:
         print(e)


@bot.message_handler(commands=['test'])
def teste(message):
    resposta_user = message.text
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
