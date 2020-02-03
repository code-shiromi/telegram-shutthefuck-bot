from telegram.ext import Filters, MessageHandler
from framesys import chatinfo, log
from handlers import basic, autoreply

##############################################
#                   Filter                   #
##############################################
def textMsg(update, context):
    content = chatinfo.sender(update, 'text')
    autoreply.flow(content)

def stickerMsg(update, context):
    content = chatinfo.sender(update, 'sticker')

def photoMsg(update, context):
    content = chatinfo.sender(update, 'photo')

def videoMsg(update, context):
    content = chatinfo.sender(update, 'video')

def voiceMsg(update, context):
    content = chatinfo.sender(update, 'voice')

def audioMsg(update, context):
    content = chatinfo.sender(update, 'audio')

def documentMsg(update, context):
    content = chatinfo.sender(update, 'document')

def locationMsg(update, context):
    content = chatinfo.sender(update, 'location')

def fuckguy(update, context):
    array, chatType, is_edit = chatinfo.msg_filter(update)
    serious = array.text.startswith('認真' or 'seriously')
    if array.from_user.id == 880288515:
        if serious == True:
            print('bypassed!')
        else:
            print('fucked!')
            update.message.reply_document("CgACAgQAAx0CQfIFQQACCUReNHZEvEBDdZcAAV5O82BINWNEcpUAAtYBAAI5_6VR3rRah02pAbMYBA")
    else:
        pass


##############################################
#                  Handler                   #
##############################################
def msgs(dp):
    # Message filters
    dp.add_handler(MessageHandler(Filters.all, fuckguy))
    dp.add_handler(MessageHandler(Filters.text, textMsg))
    dp.add_handler(MessageHandler(Filters.sticker, stickerMsg))
    dp.add_handler(MessageHandler(Filters.photo, photoMsg))
    dp.add_handler(MessageHandler(Filters.video, videoMsg))
    dp.add_handler(MessageHandler(Filters.voice, voiceMsg))
    dp.add_handler(MessageHandler(Filters.audio, audioMsg))
    dp.add_handler(MessageHandler(Filters.document, documentMsg))
    dp.add_handler(MessageHandler(Filters.location, locationMsg))
    # Import system handler
    basic.syshandler(dp)
    # log all errors
    #dp.add_error_handler(log.error)
    ############# Plugins Here
