from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler ,filters, ContextTypes

TOKEN:Final ='6811133048:AAEZFUMSQSsc7m3vVqcuaMUbLGccjMVIwok'
BOT_UserName: Final = '@gundamzbot'

#Commands
async def start_command(update:Update, context : ContextTypes.DEFAULT_TYPE):
    await update.message.replytext('Hello There what do you need me to remind you of:')
    
async def help_command(update:Update, context : ContextTypes.DEFAULT_TYPE):
    await update.message.replytext('how can i help you')

async def custom_command(update:Update, context : ContextTypes.DEFAULT_TYPE):
    await update.message.replytext('This is a custom command')    
    
#RESPONSES

def handle_responses(text : str) -> str:
    processed:str = text.lower()
    if'hello' in processed:
        return 'Hey There'
    if'how are you' in processed:
        return 'Im fine'
    return 'I d K'
 
 
#MessageHandler

async def handle_message(update:Update, context : ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text : str = update.message.text
    
    
    print(f'User({update.message.chat.id}) in {message_type}:"{text}"')
    
    if message_type == 'group':
        if BOT_UserName in text:
            new_text : str = text.replace(BOT_UserName,'').strip()
            response :str = handle_responses(new_text)
        else:
            return  
        
    else:
        response : str = handle_responses(text)
    
    print('Bot:',response)
    await update.message.reply_text(response)
    
async def error(update:Update, context : ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error{context.error}')
    
    
    
if __name__ == '__main__':
    print('Start')
    app = Application.builder().token(TOKEN).build()
    
    
    #commands
    
    
    app.add_handler(CommandHandler('start',start_command))
    app.add_handler(CommandHandler('help',help_command))
    app.add_handler(CommandHandler('custom',custom_command))
    
    
    
    #messages
    app.add_handler(MessageHandler(filters.TEXT,handle_message))
    
    
    #error
    app.add_error_handler(error)
    print('Polling')
    app.run_polling(poll_interval = 3)
