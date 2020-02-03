################################################
#       ShiroFramework Gen 2.0 (Telegram)      #
#         Author: Shiromi K. Y. Carver         #
#            Email: me@shiromi.info            #
#     Support: shiromi.works/shiroframework    #
################################################
import sys, time, argparse
from termcolor import colored as c

import config, active
from framesys import log


##############################################
#                    App                     #
##############################################
class app:
    def __init__(self):
        self.run_mode = vars(args)['mode'] # Set Parser mode
        log.log_init(self.run_mode)

    # Run bot
    def run(self):
        active.active(config.botcfg['token'])

##############################################
#                   Parser                   #
##############################################
# Create a parser
parser = argparse.ArgumentParser(prog = None,
                                description = 'Telegram Bot - ShiroFramework.',
                                usage = None)
# Add argument
parser.add_argument('mode',
                    nargs = '?',
                    default = 'run',
                    choices = ['run', 'debug', 'test'],
                    help = 'select a mode to run this bot.')

args = parser.parse_args()

##############################################
#                     Run                    #
##############################################
# Print Framework Status
version = '1.0.016ß'
print(c(config.asciiLine1, 'cyan'), c(config.asciiLine2, 'cyan'))
tmp = c('Welcome Back!\n'
        f'Start at {time.strftime("%Y/%m/%d %H:%M:%S %Z")}\n' \
        f'Version: {version}', 'red')
print(tmp)

# Run bot
if __name__ == '__main__':
    app = app()
    try:
        app.run()
    except Exception as e:
        log.apiLogger.exception(e)