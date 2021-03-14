
'''
class Bank:
    def __init__(self,):
        self.accounts = []

class Account:
    def __init__(self, no, customer):
        self.no = no
        self.customer = customer

class Customer:
    def __init__(self, name):
        self.name = name

b = Bank()
b.accounts.append(Account(123, Customer('Ali')))

print(b.accounts[0].customer.name)

'''

class Bank:
    def __init__(self):
        self.accounts = []

class Account:
    def __init__(self, num, customer):
        self.num = num
        self.customer = customer

class Customer:
    def __init__(self, name):
        self.name = name


bank = Bank();

bank.accounts.append(Account(23, Customer("Bob")))

print(bank.accounts[0].num)


