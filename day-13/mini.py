from abc import ABC,abstractmethod
class bank_account(ABC):
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


class savings_accounts(bank_account):
    def withdraw_money(self, amount):
        if amount<=self.get_balance():
            self._bank_account__balance-=amount
            print("withdraw is successfull from savings account")
        else:
            print("insufficient balance")
    def add_intest(self):
        interest=self.get_balance()*0.05
        self.deposit_money(interest)
        print("interest added")

class current_accounts(bank_account):
    def __init__(self,name,balance,limit):
        super().__init__(name,balance)
        self.limit=limit
    def withdraw_money(self, amount):
        if amount<=self.limit and amount<=self.get_balance:
            self._bank_account__balance-=amount
            print("with drawal successfully done from current account") 
        else:
            print("withdrawal exceeds limit or insufficient balance")
s1=savings_accounts("vijay",10000)
c1=current_accounts("riya",2000,5000)
s1.deposit_money(2000)
s1.withdraw_money(3000)
s1.add_intest()
print("Saving account",s1.get_balance())
c1.withdraw_money(6000)
c1.withdraw_money(4000)
print("current balance",c1.get_balance())