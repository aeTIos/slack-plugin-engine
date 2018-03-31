# example of module code
# reacts to the the command !example and sends message to the channel
# that supplied it
import patrick


@patrick.texthandler
def main(update):
    if update.get('text').startswith('!example'):
        return patrick.sendmessage(update.get('channel'), 'Example response')

