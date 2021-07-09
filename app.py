from mega import Mega
from telegram import Bot, ChatAction
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from dotenv import load_dotenv
from os import getenv, rename, remove, path, walk
from time import sleep
load_dotenv()
mega = Mega()
TOKEN = getenv('TOKEN')
bot = Bot(token=TOKEN)
email = getenv('EMAIL')
password = getenv('PASSWORD')


def starter(update, context) -> None:
    update.message.reply_text(f'Hello! {update.effective_user.first_name}, Send me your document which u wanna upload to MEGA')


def mega_uploader(update, context) :
    
    

        
    try:   
        
        message = update.message.reply_text("***Processing...***")
        #downloading file
        file_id = update.message.document.file_id  #getting file id
        newFile = bot.get_file(file_id)
        # print(newFile)
        fileName = update.message.document.file_name   #getting filename
        
        newFile.download()
        #renaming file to same name as getting...
        dir_path = path.dirname(path.realpath(__file__))
  
        for root, dirs, files in walk(dir_path):
            for file in files: 
        
                if file.endswith('.pdf'): 
                    rename(file, fileName)

        #login credintials...
        m = mega.login(email, password)

       
        if "TH" in fileName:
            folder = m.find('The Hindu')
            m.upload(fileName, folder[0])   #upload a required file to a destination folder
        
        elif "HT" in fileName:
            folder = m.find('Hindustan Times')
            m.upload(fileName, folder[0]) 
        elif "IE" in fileName:
            folder = m.find('Indian Exp')
            m.upload(fileName, folder[0]) 
        elif "BRILL" in fileName:
            folder = m.find('Brills')
            m.upload(fileName, folder[0])
        elif "TOI" in fileName:
            folder = m.find('Times Of India')
            m.upload(fileName, folder[0])  
        else:
            print("Something error has happened!")


        context.bot.send_chat_action(chat_id=update.effective_message.chat_id, action=ChatAction.TYPING)
        message_id = message.message_id
        sleep(3)
        bot.delete_message(chat_id=update.effective_message.chat_id, message_id= message_id) 
        update.message.reply_text(f'  Your file has been uploaded to MEGA!')

        remove(fileName)  #removing file...
    except Exception as e:
        print(e)    

       

updater = Updater(TOKEN)
updater.dispatcher.add_handler(CommandHandler('start', starter))

updater.dispatcher.add_handler(MessageHandler(Filters.chat_type.private, mega_uploader))

updater.start_polling()
updater.idle()


