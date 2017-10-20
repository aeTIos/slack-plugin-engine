# example of module code
# reacts to the the command !example and sends message to the channel
# that supplied it
import sloth


@sloth.texthandler
def main(update):
    if update.get('text').startswith('!example'):
        return sloth.sendmessage(update.get('channel'), 'Example response')

