
# Import command for the bots 
from typing import Final
from telegram import Update
from telegram.ext import Application , CommandHandler , MessageHandler , filters , ContextTypes
from qreader import QReader

# Import command for RSA decryption
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes
import base64
# Import command for QR reader and deletes files
import cv2
import os
import base64

TOKEN :Final = '7516319291:AAEoBYJsj8FuPt_LhU_jFMK6wukF7aV5UPo'
BOT_USERNAME:Final  ='@IS_Projectbot'




def decrypt_message(encrypted_message, private_key):
    rsa_private_key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(rsa_private_key)
    decrypted_message = cipher.decrypt(base64.b64decode(encrypted_message))
    return decrypted_message.decode()


#Commands
async def start_command(update : Update , context : ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Starting ... ... ")

async def help_command(update : Update , context : ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Helping ... ..")

async def custom_command(update : Update , context : ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)
    await update.message.reply_text("Custom command")


async def image_send(update : Update , context : ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    await context.bot.send_photo(chat_id= chat_id , photo = open("C:\\Users\\Dell\\Pictures\\Wall.jpg"  , "rb"))
async def image_receive(update : Update , context:ContextTypes.DEFAULT_TYPE):
    print("Starting copying of image")
    if update.message.photo:
        photofile = await update.message.effective_attachment[-1].get_file()
        file = await photofile.download_to_drive("test.png")

        await update.message.reply_text("Image received")



async def passphrase(update:Update , context:ContextTypes.DEFAULT_TYPE):
    #if context.args:
    #        der_private_key = ' '.join(context.args)
    #        await update.message.reply_text(f"Private key is {der_private_key}")
    print("Getting the image of qrcode and decrypting.")

    qreader = QReader()

    image = cv2.cvtColor(cv2.imread("test.png") , cv2.COLOR_BGR2RGB)

    decoded_text= qreader.detect_and_decode(image = image)
    tu :str = decoded_text[0]
    print("Value from qrcode")
    print(tu) 
    private_key = "30820122300d06092a864886f70d01010105000382010f003082010a0282010100bb522a000501b0a728bd75efa742a51f9f9287e8bc12c9769af8d8f98646d1bee204db8742a2b38fd5fb0e9d69595172b81dd7152a66c176e25d3aaf751ad694e7d1ca4e058d5b23ad2a9e57728e33ba0334519bffcc8e10f9cc4cf8ac4e1b7ec32310b66e62fcd55e047d9ad1c8a4f5c2561ebbc60637238a8a38c131c3245cab7bc8ce6c4fc0d266ec7663f3d7cc35f4a8a9e1d33482a9368261600f706d1c42e21e022792f681bfcc7249f1801b3830a59a50b1acb8e9479d42ac69ada0761d0e4c2e2c80dba23601e42a1beaf182153e20ef394a07d8e6cf8f355fc99776a4117a6af4f1e03f8a7855e045816b632531f3e7400a87ce2806b5a543cc90790203010001"
    print("Value of private key")
    print(private_key)
    print("Hex to bytes conversion")
    private_key = bytes.fromhex(private_key)
    print(private_key)
    decrypted_text = decrypt_message(private_key ,tu)    
    print(decrypted_text)
    

    await update.message.reply_text(decrypted_text)
    print("Deleting the test picture")
    os.remove("test.png")

async def get_key(update:Update , context:ContextTypes.DEFAULT_TYPE):
    if context.args:
        private_key = ' '.join(context.args)
        await update.message.reply_text(f"Private key is {private_key}")

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
    app.add_handler(CommandHandler('Custom' , custom_command))
    app.add_handler(CommandHandler('send' , image_send))
    app.add_handler(CommandHandler('pass' , passphrase))
    app.add_handler(CommandHandler('Getkey' ,get_key))
    app.add_handler(MessageHandler(filters.PHOTO , image_receive))




    app.add_handler(MessageHandler(filters.TEXT , handle_message))
    app.add_error_handler(error)

    print("Polling")
    app.run_polling(poll_interval = 3)
