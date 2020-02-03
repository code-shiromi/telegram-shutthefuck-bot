import logging, colorlog
from termcolor import colored as c

##############################################
#                Setup Logging               #
##############################################
# Chat Log
def chatlog(fm, msgType, content):
    # Colored msg
    if msgType == 'text':
        cmt = c('(' + msgType + ')', 'white', attrs=['underline']) + ' '
    elif msgType == 'sticker':
        cmt = c('(' + msgType + ')', 'red', attrs=['underline']) + ' '
    elif msgType == 'location':
        cmt = c('(' + msgType + ')', 'green', attrs=['underline']) + ' '
    elif msgType == 'voice' or msgType == 'audio':
        cmt = c('(' + msgType + ')', 'magenta', attrs=['underline']) + ' '
    else:
        cmt = c('(' + msgType + ')', 'cyan', attrs=['underline']) + ' '

    chatLogger.info(fm + enter + cmt + c(content, 'white'))

# Error log
def error(update, context):
    botLogger.warning(c('Update "%s"\ncaused error "%s"', 'yellow'), update, c(context.error, 'red'))

def handlerErr(errMsg):
	botLogger.error(c('Handler: ', 'red') + errMsg)

##############################################
#               Active Logging               #
##############################################
def log_init(run_mode):
    global botLogger, apiLogger, chatLogger
    # Add Loggers
    apiLogger = logging.getLogger('telegram.ext')
    botLogger = logging.getLogger('BOT')
    chatLogger = logging.getLogger('[CHAT]')

    # Set Format
    time = '%(bg_white)s%(asctime)s%(reset)s '
    level = '%(log_color)s[%(levelname)s]%(reset)s '
    logger = '%(cyan)s%(name)s%(reset)s' + enter
    log_info = '%(white)s%(message)s'
    fmName = '%(thin_yellow)s%(name)s%(reset)s '
    sysfmt = colorlog.ColoredFormatter(time + level + logger + log_info,
                                        datefmt="%Y-%m-%d %H:%M:%S",
                                        reset=True,
                                        log_colors={
                                            'DEBUG':    'bold_cyan',
                                            'INFO':     'bold_white',
                                            'WARNING':  'bold_yellow',
                                            'ERROR':    'bold_red',
                                            'CRITICAL': 'bold_red,bg_white',
                                        },
                                        secondary_log_colors={},
                                        style='%'
                                        )

    chatfmt = colorlog.ColoredFormatter(time + fmName + log_info,
                                            datefmt="%Y-%m-%d %H:%M:%S",
                                            reset=True,
                                            secondary_log_colors={},
                                            style='%'
                                            )

    # Set logging handler
    console = logging.StreamHandler()
    console.setFormatter(sysfmt)
    chatConsole = logging.StreamHandler()
    chatConsole.setFormatter(chatfmt)

    # Initialization
    if run_mode == 'debug': # If argument is 'debug'
        fileHandler = logging.FileHandler(filename='debug.log')
        fileHandler.setFormatter(logging.Formatter('[%(asctime)s]%(name)s - %(levelname)s - %(message)s'))
        apiLogger.setLevel(logging.DEBUG)
        debugStatus = c(' ON ', 'red', attrs=['reverse'])
    else:
        fileHandler = logging.FileHandler(filename='app.log')
        fileHandler.setFormatter(logging.Formatter('[%(asctime)s]%(name)s - %(levelname)s - %(message)s'))
        apiLogger.setLevel(logging.INFO)
        debugStatus = c(' OFF ', 'white', attrs=['reverse'])
    botLogger.setLevel(logging.INFO)
    chatLogger.setLevel(logging.INFO)

    # Handler
    apiLogger.addHandler(console)
    apiLogger.addHandler(fileHandler)
    botLogger.addHandler(console)
    botLogger.addHandler(fileHandler)
    chatLogger.addHandler(chatConsole)

    botLogger.info(c('', 'green') + 
                    c('DEBUG MODE:',
                            attrs=['concealed', 'underline']
                            ) + '  ' + debugStatus + 
                    enter +
                    c('Listening ...',
                            attrs=['concealed', 'underline']
                            ))
enter = '\n                    '
