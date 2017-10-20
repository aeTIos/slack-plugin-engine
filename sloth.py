import json


def texthandler(handlerfunction):
    def wrapper(update):
        if 'text' in update:
            return handlerfunction(update)

    return wrapper


def sendmessage(channel, text):
    payload = json.JSONEncoder().encode({"id": 1, "type": "message", "channel": channel, "text": text})
    return payload

