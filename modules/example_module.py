import api

#example of module code
#reacts to the the command !example and sends message to the channel that supplied it
def main(update):
    if api.text(update).startswith('!example'):
        return api.sendmessage(update.get('channel'), 'Example response')

