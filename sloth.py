import json


def texthandler(handlerfunction):
    def wrapper(update):
        if 'text' in update:
            return handlerfunction(update)

    return wrapper

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





