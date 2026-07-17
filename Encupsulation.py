class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self._balance = initial_balance # Convention for a protected attribute


    def deposit(self,amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited ${amount}. New balance: $ {self._balance}")
        else:
            print("Deposit amount must be positive")

    def withdraw (self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew S{amount}. Nwe balance: $ {self._balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")
    
    def get_balance(self):
        return self._balance
    
    def display_account_info(self):
        print(f"\n-- Account Info")
        print(f"Account Holder: {self.account_holder}")
        print(f"balance: ${self.get_balance()}")


    # creating an instance
my_account = BankAccount("Alice Wonderland", 1000)
my_account.display_account_info()

#using public methods to interact with the balance
my_account.deposit(500)
my_account.withdraw(200)
my_account.display_account_info