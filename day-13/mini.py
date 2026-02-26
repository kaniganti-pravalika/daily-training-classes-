from abc import ABC,abstractmethod
class Bank_account(ABC):
    def __init__(self,name,balance,):
        self.name=name
        self.__balance=balance
    def deposit_money(self,amount):
        self.__balance+=amount
        print("deposite amount:",amount)
    @abstractmethod
    def withdraw_money(self,withdraw):
        pass
    def get_balance(self):
        return self.__balance


class Savings_accounts(Bank_account):
    def withdraw_money(self, amount):
        if amount<=self.get_balance():
            self._Bank_account__balance-=amount
            print("withdraw is successfull from savings account")
        else:
            print("insufficient balance")
    def add_intrest(self):
        intrest=self.get_balance()*0.05
        self.deposit_money(intrest)
        print("interest added")

class Current_accounts(Bank_account):
    def __init__(self,name,balance,limit):
        super().__init__(name,balance)
        self.limit=limit
    def withdraw_money(self, amount):
        if amount <= self.limit and amount <= self.get_balance():
            self._Bank_account__balance-=amount
            print("with drawal successfully done from current account") 
        else:
            print("withdrawal exceeds limit or insufficient balance")
s1=Savings_accounts("vijay",10000)
c1=Current_accounts("riya",2000,5000)
s1.deposit_money(2000)
s1.withdraw_money(3000)
s1.add_intrest()
print("Saving account",s1.get_balance())
c1.withdraw_money(600)
c1.withdraw_money(400)
print("current balance",c1.get_balance())