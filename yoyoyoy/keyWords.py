
from webbrowser import get
import telebot


from rutermextract import TermExtractor
from typing import List

def getKeyWords(text: str) -> List[str]:
    term_extractor = TermExtractor()
    definition_list: List[str] = list()
    for term in term_extractor.__call__(text, nested=True):
        definition_list.append(term.normalized)
        #print(str(term.normalized.split(' ')))
    return definition_list


bot = telebot.TeleBot('5226070739:AAFjy7hHRCt6-jHhGi8MFGrc209VAtlj7WM');

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    splitted_text = str(message.text).lower().split()
    if str(message.text).lower() == "привет":
        bot.send_message(message.from_user.id, "Привет это интеллектуальный Бот для извлечения ключевых слов из новостей, чем я могу тебе помочь? Для информации введите /help.")
    elif str(message.text).lower() == "/help":
        bot.send_message(message.from_user.id, "Интеллектуальный Бот для извлечения ключевых слов из новостей. \n Список команд: \n /k - текст для анализа \n ")
    elif splitted_text[0] == "/k":
        str1=""
        for item in splitted_text:
            if item!="/k":
                str1+=" " + item
        bot.send_message(message.from_user.id, getKeyWords(str1))    
    else:
        bot.send_message(message.from_user.id, "Привет это интеллектуальный Бот для извлечения ключевых слов из новостей, чем я могу тебе помочь? Для информации введите /help.")

bot.polling(none_stop=True, interval=0)
