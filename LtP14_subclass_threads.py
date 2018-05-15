import threading
import time
import random


# create a class with subclass threading thread object
class CustomThread(threading.Thread):
    # initialize a class with name variable
    def __init__(self, name):
        # call for thread class to execute
        threading.Thread.__init__(self)
        # store the name
        self.name = name

    # define the run method
    def run(self):
        # call a function "get_time"
        get_time(self.name)
        # printout the name of the thread when ends
        print("Thread", self.name, "Execution Ends")


# create a "get_time" function that is them used in
# class, use a single variable as input - "name"
def get_time(name):
    # printout the thread name and info on whe it went
    # to sleep
    print("Thread {} sleeps at {}".format(name,
                    time.strftime("%H:%M:%S",
                    time.gmtime())))
    # generate random sleep time - same way as before
    rand_sleep_time = random.randint(1, 5)
    # pause thread for number of seconds from random
    time.sleep(rand_sleep_time)

