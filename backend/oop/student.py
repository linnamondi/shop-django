class Student:
    school="AkiraChix"

    def __init__(self,firstname,lastname,age,country):
        self.firstname=firstname
        self.lastname=lastname
        
        self.age=age
        self.country=country
        self.year=2025-age

    def greet_student(self):
        return f"Hello {self.firstname} welcome to {self.school}"
    
    def initials(self):
        
        return f"hello {self.firstname}[0]+ {self.lastname}[0]"

    def add_score(self):
        self.scores.append(score)
        total=0
        for x in self.scores:
            total+=x

        return f"your total score is {total}"

# class Account:
#     def __init__(self,name):
#         self.name=name
#         self.balance=0
#         self.loan_balance = 0
#         self.transaction_history = []
#         self.


#         # self.deposit=[]
#         # self.withdrwal=[]
#     def deposit(self,amount):
#         if amount>0:
#              self.balance += amount
#              self.transaction_history.append((datetime.now(), f"Deposited {amount}"))
#              return f"deposit of {amount},new balance is {self.balance}"

#             # self.deposit.append(amount)
            
#             # return f"deposit of {amount},new balance is {self.balance}"
#             # balance=self.get_balance()
        
#         else:
#             return f"you cannot deposit less  than zero"
        
#     def get_balance(self):
#          self.balance+=amount
#          return self.balance
    

#     def withdrawal(self):

#         # if amount > 0 and amount<=self.balance:
#         #     self.balance-=amount
#         #     return f"withdrawal of {amount} new balance is {self.balance}"

class Account:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.loan_balance = 0
        self.transaction_history = []
        print(f"[{datetime.now()}] Account created for {self.name}.")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append((datetime.now(), f"Deposited {amount}"))
            print(f"[{datetime.now()}] {self.name} deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print(f"[{datetime.now()}] Withdrawal failed. Insufficient funds.")
        else:
            self.balance -= amount
            self.transaction_history.append((datetime.now(), f"Withdrew {amount}"))
            print(f"[{datetime.now()}] {self.name} withdrew {amount}. New balance: {self.balance}")

    def get_loan(self, amount):
        if amount <= 0:
            print("Loan amount must be positive.")
        elif self.loan_balance > 0:
            print(f"[{datetime.now()}] You already have an outstanding loan of {self.loan_balance}")
        else:
            self.loan_balance = amount
            self.balance += amount
            self.transaction_history.append((datetime.now(), f"Loan taken {amount}"))
            print(f"[{datetime.now()}] {self.name} received a loan of {amount}. New balance: {self.balance}")

    def repay_loan(self, amount):
        if amount <= 0:
            print("Repayment must be positive.")
        elif self.loan_balance == 0:
            print("You have no outstanding loan.")
        else:
            if amount >= self.loan_balance:
                overpay = amount - self.loan_balance
                self.loan_balance = 0
                self.balance += overpay
                self.transaction_history.append((datetime.now(), f"Loan repaid {amount}"))
                print(f"[{datetime.now()}] {self.name} repaid the full loan. Overpay of {overpay} added to balance.")
            else:
                self.loan_balance -= amount
                self.transaction_history.append((datetime.now(), f"Loan partially repaid {amount}"))
                print(f"[{datetime.now()}] {self.name} repaid {amount}. Remaining loan: {self.loan_balance}")

    def show_balance(self):
        print(f"[{datetime.now()}] {self.name}'s Balance: {self.balance}, Loan: {self.loan_balance}")

    def transfer(self, amount, recipient_account):
        if not isinstance(recipient_account, Account):
            print("Recipient must be a valid Account.")
        elif amount <= 0:
            print("Transfer amount must be positive.")
        elif amount > self.balance:
            print(f"[{datetime.now()}] Transfer failed. Not enough balance.")
        else:
            self.balance -= amount
            recipient_account.balance += amount
            self.transaction_history.append((datetime.now(), f"Transferred {amount} to {recipient_account.name}"))
            recipient_account.transaction_history.append((datetime.now(), f"Received {amount} from {self.name}"))
            print(f"[{datetime.now()}] {self.name} transferred {amount} to {recipient_account.name}.")

    def show_transaction_history(self):
        print(f"\n--- {self.name}'s Transaction History ---")
        for time, action in self.transaction_history:
            print(f"{time}: {action}")
        print("----------------------------------------\n")

            
    
    



    
        
        
        

        

    




         
   