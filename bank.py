class Bank:
    def __init__(self,initial_amount=0.00):
      self.balance=initial_amount

    def log_transaction_details(self,details):
       with open("transaction.txt","a") as file:
         file.write(f"{details} balance:\t\t\t{self.balance}\n")


    def withdrawl(self,amount):
        try:
            amount=float(amount)
        except ValueError:
            amount<1
        if amount>self.balance:
          print("You have Insufficient Balance")
        else:
          self.balance-=amount
          self.log_transaction_details(f"withdrew :\t\t\t{amount}\t\t\t")
        print("your account balance:",self.balance)

    def deposit(self,amount):
        try:
            amount=float(amount)
        except ValueError:
            amount<1
        if amount:
          self.balance+=amount
          self.log_transaction_details(f"deposited :\t\t\t{amount}\t\t\t")
        print("your account balance:",self.balance)

        
account=Bank
      
      
   