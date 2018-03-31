import websocket
import ssl
import json
import patrick
import globals
import module_import

# init weburl from global slack variable
weburl = globals.slack.rtm.start().body['url']

# creates websocket connection
socket = websocket.create_connection(weburl, sslopt={"cert_reqs": ssl.CERT_NONE})

# creates module array from python files in the modules directory
module_array, module_names = module_import.loadmodules('modules/')

for i in range(len(module_array)):
    # Temporary code.
    # In the future, we should read this from a config file.
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
                socket.send(patrick.sendmessage(update.get('channel'),
                            f"We caught an error and the module has been disabled.\nError: {e}"))
                # set module to OFF so we don't get further errors
                i[1] = False
