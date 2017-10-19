import api


def main(update):
    if api.text(update).startswith('!example'):
        return api.sendmessage(update.get('channel'), 'Example response')

