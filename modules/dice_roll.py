# example of module code
# reacts to the the command !example and sends message to the channel
# that supplied it
import random
import sloth


@sloth.texthandler
def main(update):
    if update.get('text').startswith('!roll'):
        string = update.get('text')
        split = string.split()
        if split[1].isdigit():
            sides = int(split[1])
            if sides >= 2:
                rolled = random.randint(1, sides)
                return sloth.sendmessage(update.get('channel'), str(rolled))
            else:
                return sloth.sendmessage(update.get('channel'), 'That is impossible in this reality.')
        else:
            return sloth.sendmessage(update.get('channel'), 'Please input a number.')
