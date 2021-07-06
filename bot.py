from mega import Mega
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, CallbackContext
from dotenv import load_dotenv
from os import getenv
load_dotenv()
mega = Mega()
TOKEN = getenv('TOKEN')
bot = Bot(token=TOKEN)
email = getenv('EMAIL')
password = getenv('PASSWORD')

m = mega.login(email, password)
# login using a temporary anonymous account



# details = m.get_user()
# print(f"Your MEGA AC name is: {details['name']}")


#checking  MEGA balance
# balance = m.get_balance()
# if  len(balance) != 0:
#     print(f"your Mega A/c balance is: {balance}")
# else:  
#     print("You don't have any paid Mega A/C") 


#get details for disk quota
# quota = m.get_quota()
# print(f"Your total storage quota is: {quota} MB")
# space = m.get_storage_space(giga=True)
# print(f"You have currently used  is: {int(space['used'])} GB out of {int(space['total'])} GB")

# Get account files
# files = m.get_files()

# for key in files.keys():
#         print(f"folders are: {files[key]['a']['n']}")


# Upload a file, and get its public link
# file_path = input("Enter the correct path with file name and extention to upload:")
# file = m.upload(file_path)
# file_shr_link = m.get_upload_link(file)
# print(f"Ur file sharing link is: {file_shr_link}")

# Export a file or folder
# myfile = input("enter the file name with path or folder to get sharing link:")
# public_exported_web_link = m.export(myfile)
# # e.g. https://mega.nz/#F!WlVl1CbZ!M3wmhwZDENMNUJoBsdzFng  ---this is the sharing link..
# print(f"this is the sharing link:{public_exported_web_link}")


# #Find File and folder....
# myfile = input("enter the file name which u wanna find:")
# folder = m.find(myfile)
# if folder > -1:
#   print('file found!')
# else:
#     print('file not found!')
# # Excludes results which are in the Trash folder (i.e. deleted)


# Download a file from URL or file obj, optionally specify destination folder
# myfile= input("Enter ur file name to download")
# file = m.find(myfile)
# if file > -1:
#     m.download(file)
# else: 
#     print("No such file found!")

#download using sharing link:-----
# myshringlink = input("Enter shared download link:")
# m.download_url(myshringlink)

# # Create a folder
# new_folder =input("Enter ur new folder name:")
# m.create_folder(new_folder)


# Rename a file or a folder
file_name = input("Enter the existing name of the file: ")
file = m.find(file_name)
if file > 0:
    m.rename(file, 'my_file.doc')
else:
   print("No such file is present")












































# def start(update: Update, context: CallbackContext) -> None:
#     update.message.reply_text(f'Hello {update.effective_user.first_name}')





# updater = Updater(TOKEN)

# updater.dispatcher.add_handler(CommandHandler('start', start))   #command,  function calling

# updater.start_polling()
# updater.idle()