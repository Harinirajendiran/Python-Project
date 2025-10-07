class BankAccount:
    def __init__(self, account_number, account_holder, balance):
              self. account_number = account_number # Public
              self._account_holder = account_holder # Protected
              self.__balance = balance # Private

    #Public Method
    def deposit(self, amount):
            if amount > 0:
                self.__balance += amount
                print(f"Deposited ₹{amount}. New Balance: ₹{self.__balance}")
            else:
                print("Invalid deposit amount.")

    # Public Method
    def withdraw(self, amount):
            if 0 < amount <= self. __balance:
                self. __balance -= amount
                print(f"Withdrew ₹{amount}. Remaining Balance: ₹{self.__balance}")
            else:
                print("Insufficient funds or invalid amount.")


    # Protected Method
    def _display_holder_info(self):
        print(f"Account Holder: {self._account_holder}")

    # Private Method
    def __apply_bank_charges(self):
    # Private method to deduct charges, used internally only
        self.__balance -= 50
        print("₹50 bank charge applied.")
        
    def bankcharge(self):
        self.__apply_bank_charges()

    # Public Method that uses private method internally
    def month_end_process(self):
            self.__apply_bank_charges()
            print("Month-end processing done.")
            
    def quit(self):
        print("Thank you for finding us to your convin")

#main function
def sub():
    account_number=int(input("Enter your account num:"))
    account_holder=input("Enter account holder name:")
    balance=1000
    
    account = BankAccount(account_number, account_holder, balance)

    while True:
        print("**Indiana Bank web**")
        print("1.Deposit,2.Withdrawal,3.Holder name display,4.Bank Charge,5.Month end process,6.quit")
        
        get=input("Enter num 1 to 6 for futher process:")
        
        if get=='1':
            amount=int(input("Enter amount:"))
            account.deposit(amount)
            
        elif get=='2':
            amount=int(input("Enter amount:"))
            account.withdraw(amount)
        
        elif get=='3':
            self._display_holder_info()
        
        elif get=='4':
            account.bankcharge()
        
        elif get=='5':
            account.month_end_process()
            
        elif get=='6'
        
if __name__=='__main__':
    s=sub()
            
    
    
    


