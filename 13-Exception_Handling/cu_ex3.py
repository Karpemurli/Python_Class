# # 4. Custom Exception for Insufficient Balance



class trans(Exception):
    def __init__(self, msg="Insufficient B/C"):
        super().__init__(msg)


class bankBalance:
    def __init__(self,balance):
        self.balance=balance
        
    def withdraw(self,amount):
        if amount > self.balance:
            raise trans("Insufficient....!")
        self.balance -= amount
        return f"Withdraw successful...Balance={self.balance}"
try:
    account=bankBalance(2000)
    amount=int(input("Enter the amount to withdraw: "))
    result=account.withdraw(amount)
    print(result)
except trans as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
finally:
    print("Transaction completed.")


# class Transaction(Exception):
#     def __init__(self, msg="khatam"):
#         super().__init__(msg)


# class BankAccount:
    
#     def __init__(self,balance):
        
#         self.balance = balance
        
#     def  withdraw(self,amount):
#         if amount > self.balance:
#             raise Transaction("Insufficient balance")
#         self.balance -= amount
#         return f"withdraw successful... Balance={self.balance}"

# try:
#     account=BankAccount(2000)
#     amount=int(input("Enter the amount to withdraw: "))
#     result=account.withdraw(amount)
#     print(result)
# except Transaction as e:
#     print(f"Error: {e}")
# except ValueError as e:
#     print("Invalid input. Please enter a valid number.")
# except Exception as e:
#     print(f"Unexpected error: {e}")
# finally:
#     print("Transaction completed.")