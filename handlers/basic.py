from telegram import ReplyKeyboardMarkup
from telegram.ext import Filters, CommandHandler, MessageHandler, ConversationHandler
from pprint import pformat
from framesys import chatinfo, log
from handlers import autoreply

HELP = range(1)

##############################################
#                  Command                   #
##############################################
def start(update, context):
    chatinfo.sender(update, 'command')
    reply_keyboard = [['About', 'Help'],
                    ['Website']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        "Hi! I'm Shiromi's Assistant!\n"
        "Any question please contact @WhiteFish_Shiromi",
        reply_markup=markup)
    return HELP

def about(update, context):
    text = update.message.text
    context.user_data['choice'] = text
    update.message.reply_text('About!')
    return HELP

def help(update, context):
    text = update.message.text
    context.user_data['choice'] = text
    update.message.reply_text('help!')
    return HELP

def website(update, context):
    user_data = context.user_data
    if 'choice' in user_data:
        del user_data['choice']
    update.message.reply_text("https://shiromi.world")

    user_data.clear()
    return ConversationHandler.END

def query(update, context):
    chatinfo.sender(update, 'command')
    query = pformat(str(update.message))
    update.message.reply_text(query)

def syshandler(dp):
    # commands
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("query", query))
    # conversation
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={HELP: [MessageHandler(Filters.regex('^(About)$'),about),
                        MessageHandler(Filters.regex('^(Help)$'), help)
                        ]},
        fallbacks=[MessageHandler(Filters.regex('^Website$'), website)]
    )
    dp.add_handler(conv_handler)