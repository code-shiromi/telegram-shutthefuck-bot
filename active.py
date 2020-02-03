from telegram.ext import Updater
from framesys import handlers

##############################################
#                   Filter                   #
##############################################
def active(token):
    # Bot = {'id': 305896733, 'username': 'shiromi_bot', 'first_name': 'Ｓｈｉｒ♬ ｍｉ✁*。生命は罰'}
    updater = Updater(token, use_context=True) # Get Bot connection
    handlers.msgs(updater.dispatcher) # Get the dispatcher to register handlers & Get Message handlers
    updater.start_polling() # Start Listening...

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()
