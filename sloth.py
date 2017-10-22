import json
import globals
import sys


def texthandler(handlerfunction):
    def wrapper(update):
        if 'text' in update:
            return handlerfunction(update)

    return wrapper


# sends channel message
# input channel name and text to send
# return Json encoded payload to socks
def sendmessage(channel, text):
    payload = json.JSONEncoder().encode({"id": 1, "type": "message", "channel": channel, "text": text})
    return payload


# sends private message
# input real_name(nickname) and text to send
# return None
def sendprivmessage(user,text):
    response = globals.slack.users.list()
    users = response.body["members"]
    for member in users:
        if member["profile"]["real_name"] == user:
            globals.slack.chat.post_message("@" + member["id"], text)
    return None


# uploads image
# TODO: STUB
def uploadimage():
    pass




