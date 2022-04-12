import requests
import telebot


moeda_dict = {}
user = {}
api_key = "5191904654:AAFrD8ybCk8N06Xx4yVbSH2r-hsxQ6k7jxE"
bot = telebot.TeleBot(api_key)


@bot.message_handler(commands=["Euro"])
def pegar_moeda(message):
   try:
       if True:
           request = requests.get('https://economia.awesomeapi.com.br/last/EUR')
           moeda_info = request.json()
           print(moeda_info)
           print(request)

           bot.reply_to(message, "Segue a cotação da moeda:{}".format(moeda_info['EUR']['bid']))
       bot.register_next_step_handler(message, sugestao)
   except Exception as e:
       print(e)


def sugestao(message):
    bot.send_message(message.chat.id, "Gostaria de cadastrar seu email? Caso se interesse digite 'Sim', caso contrário digite 'Não'")
    condicao = message.text
    if condicao == 'Sim' or 'sim':
        bot.register_next_step_handler(message, cadastro_email)
    if condicao == 'Não' or "não":
        bot.register_next_step_handler(message, menu_inicial)


def cadastro_email(message):
    print("Caiu aqui")


@bot.message_handler(commands=['WhallyBot'])
def teste(message):
    bot.send_message(message.chat.id, "AMOGUS!")


def verificar(message):
    return True


@bot.message_handler(func=verificar)
def menu_inicial(message):
    menu = """
    Seja Bem vindo ao WhallyBot, por favor selecione uma de nossas opções para cotação:
    /cotações
    /contatos
    /WhallyBot 🤖🤑
    
    
    /Dolar
    /Real Brasileiro
    /Kwanza
    /Euro
    """
    bot.reply_to(message, menu)


bot.polling()
