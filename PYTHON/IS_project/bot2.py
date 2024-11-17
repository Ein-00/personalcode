
#This code works so fix it


# Import command for the bots 
from typing import Final
from telegram import Update
from telegram.ext import Application , CommandHandler , MessageHandler , filters , ContextTypes

#For RSA decryption 

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
# Import command for QR reader and deletes files
#For reading qrcode from and image
from qreader import QReader
import cv2
import os

TOKEN :Final = '7516319291:AAEoBYJsj8FuPt_LhU_jFMK6wukF7aV5UPo'
BOT_USERNAME:Final  ='@IS_Projectbot'


def decrypt_message(key , ciphertext):

    bkey = bytes.fromhex(key)
    private_key = RSA.import_key(bkey)
    cipher = PKCS1_OAEP.new(private_key)
    decrypted_text = cipher.decrypt(ciphertext)
    print(decrypted_text)
    
    return decrypted_text

#Commands



async def start_command(update : Update , context : ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Starting ... ... ")

async def help_command(update : Update , context : ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Helping ... ..")


async def passphrase(update:Update , context:ContextTypes.DEFAULT_TYPE):
    cipher=""
    if context.args:
            cipher = ' '.join(context.args)
            await update.message.reply_text(f"Private key is {cipher}")
    print("Getting the image of qrcode and decrypting.")

    qreader = QReader()

    image = cv2.cvtColor(cv2.imread("test.png") , cv2.COLOR_BGR2RGB)

    decoded_text= qreader.detect_and_decode(image = image)
    tu :str = decoded_text[0]
    print("Value from qrcode")
    print(tu) 
    bc= bytes.fromhex(cipher)
    private_key = RSA.import_key(bc)
    ciphertex = tu
    ciphertext = bytes.fromhex(ciphertex)
    cipher = PKCS1_OAEP.new(private_key)
    
    text = cipher.decrypt(ciphertext)
    print(text)



    await update.message.reply_text(f"Decrypted text {text.decode('utf-8')}")
    print("Deleting the test picture")
    os.remove("test.png")

async def image_receive(update : Update , context:ContextTypes.DEFAULT_TYPE):
    print("Starting copying of image")
    if update.message.photo:
        photofile = await update.message.effective_attachment[-1].get_file()
        file = await photofile.download_to_drive("test.png")

        await update.message.reply_text("Image received")



#Responses

def handle_response(text : str ) -> str:
    return text



async def handle_message(update :Update , context :ContextTypes.DEFAULT_TYPE):
    message: str = update.message.chat.type
    text : str = update.mesasge.text
    print(f"User {update.message.chat.id} in {message}: {text}")
    if message == 'group':
        if BOT_USERNAME in text:
            new_txt :str = text.replace(BOT_USERNAME , '').strip()
            response :str = handle_response(new_txt)
        else :
            return
    else :
        response : str = handle_response(text)
    print('Bot' , response)
    await update.message.reply_text(response)


async def error(update : Update , context : ContextTypes.DEFAULT_TYPE):

    print(f"Update  {update} ,caused error { context.error}")



if __name__ == '__main__':
    print("Starting bot")
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler('start' , start_command))
    app.add_handler(CommandHandler('help' , help_command))
    app.add_handler(CommandHandler('pass' , passphrase))
    app.add_handler(MessageHandler(filters.PHOTO , image_receive))




    app.add_handler(MessageHandler(filters.TEXT , handle_message))
    app.add_error_handler(error)

    print("Polling")
    app.run_polling(poll_interval = 3)
