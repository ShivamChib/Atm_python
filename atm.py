import random 
import numpy

class Account:
    depositFrequency = 4
    transactionMax = 40000
   
    def __init__(self, id, balance = 0, withdrawalDailyMax = 50000,
    withdrawalFrequency=3,withdrwalTransactionMax=20000, depoDailyMax = 150000, 
    depositFrequency = 4, depoTransactionMax = 40000):
        self.id = id
        self.balance = balance
      
        self.withdrawalDailyMax = withdrawalDailyMax
        self.withdrawalFrequency=withdrawalFrequency
        self.withdrwalTransactionMax=withdrwalTransactionMax
       
        self.depoDailyMax=depoDailyMax
        self.depositFrequency = depositFrequency
        self.depoTransactionMax=depoTransactionMax

    def getId(self):
        return self.id

    def getBalance(self):
        return self.balance
   
    def getWithdrawalFrequency(self):
        return self.withdrawalFrequency
    def getWithdrwalTransactionMax(self):
        return self. withdrwalTransactionMax
    def getWithdrawalDailyMax(self):
        return self.withdrawalDailyMax

    def getDepoDailyMax(self):
        return self.depoDailyMax
    def getDepositFrequency(self):
        return self.depositFrequency
    def getDepoTransactionMax(self):
        return self.depoTransactionMax


    def withdraw(self, amount):
    
        self.balance -= amount

    def deposit(self, amount):
 
        self.balance += amount 



def main():
   
    accounts = []
    for i in range(1000, 9999): 
        account = Account(i, 0)
        accounts.append(account)    
    while True:
       
        id = int(input("\n Please Enter Your account pin: "))
        while id < 1000 or id > 9999:
            id = int(input("\nInvalid Pin.. Re-enter your Pin please: "))

        while True:
       
            print("\n1 - Balance \t 2 - Withdraw \t 3 - Deposit \t 4 - Quit ")

            selection = int(input("\nEnter your selection: "))
          
            for acc in accounts:

                if acc.getId() == id:
                    accountObj = acc
                    break
                  
            if selection == 1:
             
                print("Your Balance is:" +  str(accountObj.getBalance())+ " ")
             # Withdraw
            elif selection == 2:
                print("Your Balance is:" + str(accountObj.getBalance()))
               # Reading amount
                amt = float(input("\nPlease Enter amount to withdraw: "))
                ver_withdraw = input("Is this the correct amount, Yes or No ? " + str(amt) + " ")
    
                if ver_withdraw == "Yes":
                    print("Verify withdraw")
                else:
                    break

                if amt < accountObj.getBalance():
                    print("Your Balance is:" +  str(accountObj.getBalance())+ " ")
                    # Calling withdraw method
                    accountObj.withdraw(amt)
                    # Printing updated balance
                    print("\nUpdated Balance: " + str(accountObj.getBalance()) + " \n")
                    print("you have only 2 withdrawal times remaining")
                else:
                    print("\nYou're balance is less than withdrawl amount: " + str(accountObj.getBalance()) + " \n")
                    print("\nPlease make a deposit.")
             # Deposit
            elif selection == 3:
                
                print("Your Balance is:" +  str(accountObj.getBalance())+ " ")
                # Reading amount
                amt = float(input("\nEnter amount to deposit: "))
                ver_deposit = input("Is this the correct amount, Yes, or No ? " + str(amt) + " ")
                if ver_deposit == "Yes":
                    # Calling deposit method
                    accountObj.deposit(amt)
                    # Printing updated balance
                    print("\nUpdated Balance: " + str(accountObj.getBalance()) + " \n")
                    print("you have only 3 deposit times remaining")
                else:
                    exit()
        
            elif selection == 4:
                check = input("Are you sure you want to quit?, Yes, or No:")
                if check == "Yes":
                    print("\nYour Transaction is complete")
                    print("Transaction number: ", random.randint
                            (10000, 1000000))
                    print("Thanks for choosing us as your bank")
                else:
                    main()
              
 
          
            else:
                print("\nThat's an invalid choice.")
                #break;
main()