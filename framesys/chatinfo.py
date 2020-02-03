from termcolor import colored as c
from framesys import log

def msg_filter(update):
    if update.edited_message == None and update.edited_channel_post == None:
        if update.channel_post == None:
            array = update.message
        elif update.channel_post != None:
            array = update.channel_post
        chatType = array.chat.type
        is_edit = False
    elif update.edited_message or update.edited_channel_post != None:
        if update.edited_channel_post == None:
            array = update.edited_message
            chatType = array.chat.type
        elif update.edited_channel_post != None:
            array = update.edited_channel_post
            chatType = array.chat.type
        is_edit = True
    else:
        log.handlerErr('Unknown Chat Type')
        pass
    return array, chatType, is_edit

def content_receiver(array, msg_type):
    if msg_type == 'text' or msg_type == 'command':
        content = array.text
    elif msg_type == 'sticker':
        content = array['sticker']['file_id']
    elif msg_type == 'photo':
        p = array['photo']
        max = 0
        for i in range(1,len(p)):
            if p[i]['width'] > p[max]['width']:
                max = i
        maxFileId = p[max]['file_id']
        try:
            text = '%s %s%s' % (' [Message:',msg['caption'],']')
        except:
            text = ' [No Message]'
        content = maxFileId + text
    elif msg_type == 'video':
        content = array['video']['file_id']
    elif msg_type == 'voice':
        content = array['voice']['file_id']
    elif msg_type == 'audio':
        content = array['audio']['file_id']
    elif msg_type == 'document':
        try:
            text = '%s %s%s' % (' [Message:', msg['caption'], ']')
        except:
            text = ' [No Message]'
        content = array['document']['file_id'] + text
    elif msg_type == 'location':
        latitude = array['location']['latitude']
        longitude = array['location']['longitude']
        location = str(latitude) + ',' + str(longitude)
        content = 'https://www.google.com/maps/search/?api=1&query=' + location
    return content

def checkFullname(firstname, lastname):
    try:
        fullname = firstname + ' ' + lastname
    except TypeError:
        fullname = firstname
    return fullname

def sender(update, msg_type):
    array, chatType, is_edit = msg_filter(update)
    # Check message is edit
    content = content_receiver(array, msg_type)

    # Check chat type
    if chatType == 'channel':
        title = array.chat.title
        chatId = array.chat.id
        chat_info = c('[' + chatType + ']', 'white', 'on_blue') + c(title + '(' + str(chatId) + '):', 'cyan', attrs=['underline'])
    elif chatType == 'private':
        username = array.chat.username
        userId = array.chat.id
        fullname = checkFullname(array.chat.first_name, array.chat.last_name)
        chat_info = c('[' + chatType + ']', 'grey', 'on_white') + c(fullname + '(@' + str(username) + ')' + '(' + str(userId) + '):', 'yellow', attrs=['underline'])
    elif chatType is 'group' or 'supergroup':
        title = array.chat.title
        chatId = array.chat.id
        username = array.from_user.username
        userId = array.from_user.id
        fullname = checkFullname(array.from_user.first_name, array.from_user.last_name)
        chat_info = c('[' + chatType + ']', 'white', 'on_red') + c(title + '(' + str(chatId) + ')', 'green', attrs=['underline']) + '\n                    ' + c(fullname + '(@' + str(username) + ')' + '(' + str(userId) + '):', 'yellow', attrs=['underline'])

    # Log chat message
    if is_edit == False:
        log.chatlog(chat_info, msg_type, content)
    elif is_edit == True:
        log.chatlog(chat_info, msg_type, c('(update) ', 'red') + content)

    return content
