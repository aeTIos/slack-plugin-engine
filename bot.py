import sys
from slacker import Slacker
import websocket
import ssl
import json
import sloth

import module_import

# init variables to handle messaging and input of the API key
slack_api_key = sys.argv[1]
slack = Slacker(slack_api_key)
weburl = slack.rtm.start().body['url']

# creates websocket connection
socket = websocket.create_connection(weburl, sslopt={"cert_reqs": ssl.CERT_NONE})

# creates module array from python files in the modules directory
module_array, module_names = module_import.loadmodules('modules/')

for i in range(len(module_array)):  # temporary code. In the future, we should read this from a config file.
    module_array[i] = [module_array[i], True]

# Main loop
while True:
    update = socket.recv()
    update = json.JSONDecoder().decode(update)

    # handle own commands

    # !enable !disable !loadmodule

    for i in module_array:
        if i[1] is True:
            try:
                reply = i[0].main(update)
                if reply is not None:
                    socket.send(reply)

            except Exception as e:
                # print('Error:', e)
                # return error and log
                socket.send(sloth.sendmessage(update.get('channel'),"We caught an error and the module has been disabled.\nError: {e}"))
                i[1] = False  # set module to OFF so we don't get further errors
