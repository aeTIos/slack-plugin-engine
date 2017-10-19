import json


def text(update):
    try:
        return update['text']
    except KeyError:
        return 'No text in update body!'

# sends channel message
#input channel name and text to send
#return Json encoded payload to socks
def sendmessage(channel, text):
    payload = json.JSONEncoder().encode({"id": 1, "type": "message", "channel": channel, "text": text})
    return payload

# sends private message
#input user name and text to send
#return Json encoded payload
#TODO: test function to see if it works
def sendprivmessage(user,text):
    payload = json.JSONEncoder().encode({"id": 1, " type": "message", "channel": user, "text": text})
    return payload


#uploads image
#TODO: STUB
def uploadimage():





