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
        sides = int(split[1])
        rolled = [random.randint(1, sides)]
        return sloth.sendmessage(update.get('channel'), rolled)
