class BankAccount:
    bank_name = "MyBank"

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

acc_1 = BankAccount("123456", 1000)
acc_2 = BankAccount("789012", 500)

# Accessing the class __dict__ attribute
print(BankAccount.__dict__)
# {
#     '__module__': '__main__', 'bank_name': 'MyBank', 
#     '__init__': <function BankAccount.__init__ at 0x00000212681E9760>, 
#     '__dict__': <attribute '__dict__' of 'BankAccount' objects>, 
#     '__weakref__': <attribute '__weakref__' of 'BankAccount' objects>, 
#     '__doc__': None
# }


# Accessing the instance __dict__ attribute
print(acc_1.__dict__)
# {
#     'account_number': '123456', 
#     'balance': 1000
# }