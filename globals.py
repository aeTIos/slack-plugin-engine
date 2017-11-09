# Global variables go in here
# made on 12:02 21-10-2017
from slacker import Slacker
import sys

# Slacker global variable
# init slacker using API key passed as argument
slack = Slacker(sys.argv[1])

