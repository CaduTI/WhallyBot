import json
import requests
import telebot


class Moeda:
    def __init__(self, nome):
        self.nome = nome
        self.valor = None


moeda_dict = {}
user = {}
api_key = "5191904654:AAFrD8ybCk8N06Xx4yVbSH2r-hsxQ6k7jxE"
bot = telebot.TeleBot(api_key)



@bot.message_handler(commands=["listarmoedas"])
def pegar_moeda(message):#pego a moeda que o usuário deseja
    try:
        msg = message
        bot.send_message(msg.chat.id,"digite a moeda deseja")
        bot.register_next_step_handler(msg,procura_tagmoeda_arquivo)
    except Exception :
       print(Exception)

def procura_tagmoeda_arquivo(message):#procuro dentro do XML a tag da moeda enviada pelo usuário
    #pass
    try:
        pass
    #vai fazer a BUSCA DENTRO DO XML com o nome da moeds ue o cliente digitou, caso ele n ache vai pro except
    except:
        pass
        #RaiseException("Deu ruim patrão, digita certo ae")
def consultar_cotacao(message):
     try:
         msg = message
         moedanome = msg.text
         print(moedanome)
         if True:
            request = requests.get('https://economia.awesomeapi.com.br/last/USD-{}'.format(moedanome))
            moeda_info = request.json()
            print(moeda_info)
            print(request)
            
            bot.reply_to(msg, f"Segue a cotação da moeda:{moeda_info}")
     except:
         print(Exception)



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
