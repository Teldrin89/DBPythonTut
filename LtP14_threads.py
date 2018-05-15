# thread is simply block of code that executes -
# up till this part there have been only single
# thread scripts that were executed

# to show how this works here is a function that will
# work with some delay in time
# import threading, time and random modules
import threading
import time
import random


# define a function that will execute as a thread
def execution_thread(i):
    # function will receive a single value - "i"
    # function will printout the simple msg about time
    # and identification (i)
    # use formatted time method to get time and edit it
    # to look like selected format: HH:MM:SS for GM zone
    print("Thread {} sleeps at {}".format(i,
                    time.strftime("%H:%M:%S",
                    time.gmtime())))

    # generate a random sleep period for thread, to be
    # between 1 and 5
    rand_sleep_time = random.randint(1, 5)
    # method sleep is used to pause a thread for
    # specific amount of seconds
    time.sleep(rand_sleep_time)
    # printout msg after the thread is awoken
    print("Thread {} stops sleeping at {}".format(i,
                    time.strftime("%H:%M:%S",
                    time.gmtime())))


# create some threads and run them - use loop for
# up to 10
for i in range(10):
    # create a thread by use threading module "thread"
    # function; the name has to be put as target, next
    # there is a need of arguments - we put here
    # identification number from "for" loop
    thread = threading.Thread(target=execution_thread,
                              args=(i,))
    # start a thread
    thread.start()
    # printout active threads
    print("Active Threads: ", threading.active_count())
    # printout thread objects
    print("Thread Objects: ", threading.enumerate())

# in results, for first "i" in loop there are already 2
# threads running as the script above will have the part
# from line 38 as single thread and the function above
# as separate thread - hence 2 at the start;
# the list of threads that stopped sleeping at specific
# time is not in order as different threads can stop at
# different time (due to specifing the sleep time as
# random in range 1-4s)
