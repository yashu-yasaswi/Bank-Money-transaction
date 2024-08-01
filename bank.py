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
            amount=0
        if amount:
          self.balance=self.balance-amount
          self.log_transaction_details(f"withdrew :\t\t\t{amount}\t\t\t")
        print("your account balance:",self.balance)

    def deposit(self,amount):
        try:
            amount=float(amount)
        except ValueError:
            amount=0
        if amount:
          self.balance=self.balance+amount
          self.log_transaction_details(f"deposited :\t\t\t{amount}\t\t\t")
        print("your account balance:",account.balance)

account=Bank()
while True:
   try:
     action=input("Deposit or Withdrawl:\t")
   except KeyboardInterrupt:
     print("\n Thankyou\n")
     break

   if action in ["Deposit","withdrawl"]:
      if action=="Deposit":
        amount=input("Enter the Deposit amount:")
        account.deposit(amount)
      else:
        #action=="withdrawl":
        amount=input("Enter the Withdrawl amount:")
        account.withdrawl(amount)
   else:
      print("You have Entered an Invalid input. please try again")
        

      
      
   