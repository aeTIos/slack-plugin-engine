
import sys
from slacker import Slacker
import websocket
import ssl
import json
import module_import


slack_api_key = sys.argv[1]
slack = Slacker(slack_api_key)
weburl = slack.rtm.start().body['url']
socket = websocket.create_connection(weburl, sslopt={"cert_reqs": ssl.CERT_NONE})

module_array, module_names = module_import.loadmodules('modules/')


def sendmessage(channel, text, socket):
    payload = json.JSONEncoder().encode({"id": 1, "type": "message", "channel": channel, "text": text})
    socket.send(payload)


while True:
    update = socket.recv()
    update = json.JSONDecoder().decode(update)





