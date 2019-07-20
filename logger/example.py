import logging


logger = logging.getLogger("our logger")
logger.setLevel(logging.DEBUG)
logger_file = logging.FileHandler("test.log")
logger_file.setFormatter(logging.Formatter("%(levelname)s:%(asctime)s:%(message)s"))
logger.addHandler(logger_file)

# def division(a,b):
#     if(b == 0):
#         logger.info("tried to divide by 0")
#     return a/b
#
# division(10,0)


#don;t import untill transfer to another account implemented
import random


class Client:
    def __init__(self,username):
        logger.info("client with username {} was created".format(username))
        self.username = username
        self.balance = 0

    def get_username(self):
        return self.username

    def get_balance(self):
        return self.balance


    def add_funds(self,amount):
        logger.info("adding amount {} for client {}".format(amount,self.username))
        self.balance+=amount

    def withdraw_funds(self,amount):
        if(amount > self.balance):
            logger.warning("can;t withdraw balancne is {} , withdraw amount is {} for user {}".format(self.balance,amount,self.username))

    def transfer_to_another_account(self,amount,clientTo):
        exists = random.getrandbits(1)
        print(exists)
        if( not exists):
            logger.error("Transfer failed: The user with username {} does not exist".format(clientTo.get_username()))
        if(self.balance < amount):
            logger.error("Transaction failed: The balance {} is less than transaction amount {}".format(self.balance,amount))

        self.withdraw_funds(amount)
        clientTo.add_funds(amount)
        logger.info("Transaction successful: Transferred {} from user {} to {} ".format(amount,self.get_username(),clientTo.get_username()))


client = Client("Mark")
client.add_funds(1000)
client.withdraw_funds(2000)

other_client = Client("Tom")
client.transfer_to_another_account(200,other_client)