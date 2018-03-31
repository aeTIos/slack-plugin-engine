# example of module code
# reacts to the the command !example and sends message to the channel
# that supplied it
import random
import patrick


@patrick.texthandler
def main(update):
    if update.get('text').startswith('!roll'):
        string = update.get('text')
        split = string.split()
        if string == "":
            rolled = random.randint(1, 6)
            return patrick.sendmessage(update.get('channel'), str(rolled))
        elif split[1].isdigit():
            sides = int(split[1])
            if sides >= 2:
                rolled = random.randint(1, sides)
                return patrick.sendmessage(update.get('channel'), str(rolled))
            else:
                return patrick.sendmessage(update.get('channel'), 'That is impossible in this reality.')
        else:
            return patrick.sendmessage(update.get('channel'), 'Please input a number.')
