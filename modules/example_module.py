import sloth


@sloth.texthandler
def main(update):
    if update.get('text').startswith('!example'):
        return sloth.sendmessage(update.get('channel'), 'Example response')

