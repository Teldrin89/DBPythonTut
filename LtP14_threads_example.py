# example of threads usage: whenever threads are used
# it is possible to block one of the threads - the
# real world script that can utilize this option
# will cover a modeling of bank account: let's say
# that there is 100$ in the account but there are 3
# different people that can withdraw money from that
# account, the script will block the possibility
# of withdrawing money from the account while
# one of the person is taking the money at a time
import threading
import time
import random


# create a class for bank account with threads
class BankAccount(threading.Thread):
    # static variable
    accountBalance = 100
    # initialize a thread with name and amount of
    # money requested
    def __init__(self, name, moneyRequest):
        threading.Thread.__init__(self)
        # assign name of person that want to
        # withdraw money
        self.name = name
        # get the amount of money to be withdrawn
        self.moneyRequest = moneyRequest

    # run property definition
    def run(self):
        # create locking property - not to be able
        # to acquire the money from other threads
        threadLock.acquire()
        # access to get the money from account
        BankAccount.getMoney(self)
        # release the lock for a thread after first
        # withdraw to work
        threadLock.release()

    # create a static method for getting money
    @staticmethod
    def getMoney(customer):
        # printout the msg about who, how much and
        # when wants to withdraw money from account
        print("{} tries to withdraw {}$ at"
              "{}".format(customer.name,
                    customer.moneyRequest,
                    time.strftime("%H:%M:%S",
                    time.gmtime())))
        # what to do in case of enough money in account
        if BankAccount.accountBalance - customer.moneyRequest > 0:
            BankAccount.accountBalance -= customer.moneyRequest
            print("New account balance: "
                  "{}$".format(BankAccount.accountBalance))
        # what to do in case there is not enough money
        else:
            print("Not enough money in account")
            print("Current balance: "
                  "{}$".format(BankAccount.accountBalance))
        # time to sleep after execution - needed to see the
        # difference in execution of next threads
        time.sleep(3)


# thread lock method assigned
threadLock = threading.Lock()
# 3 people wants to take specific amount of money
luke = BankAccount("Luke", 1)
john = BankAccount("John", 100)
jean = BankAccount("Jean", 50)
# start all threads
luke.start()
john.start()
jean.start()
# join all threads
luke.join()
john.join()
jean.join()
# end printout msg
print("Execution Ends")
