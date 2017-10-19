import json


def text(update):
    try:
        return update['text']
    except KeyError:
        return 'No text in update body!'


def sendmessage(channel, text):
    payload = json.JSONEncoder().encode({"id": 1, "type": "message", "channel": channel, "text": text})
    return payload

