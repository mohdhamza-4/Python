 
from abc import ABC,abstractmethod

class Bankaccount(ABC):
  def __init__(self,name,balance):
    self.name=name
    self.__balance=balance   #ENCAPSULATION

  @abstractmethod
  def calculate_interesrt(self):
    pass
  def deposit(self,amount):
    if amount>0:
      self.__balance+=amount
  def withdraw(self,amount):
    if amount<=self.__balance:
      self.__balance-=amount

  def get_balance(self):
    return self.__balance
  

class Currentaccount(Bankaccount):
  def calculate_interesrt(self):
    return self.get_balance()*0.02
  
class Savingaccount(Bankaccount):
  def calculate_interesrt(self):
    return self.get_balance()*0.04
  
#------------------ POLYMORPHISM -------------
  
account=[Currentaccount('Hamza',25000),Savingaccount('Aman',30000)]
for m in account:
  print(m.name,'Interest',m.calculate_interesrt())


#----------------- INHERITANCE ----------------

acc1=Currentaccount('Hamza',58000)
acc2=Savingaccount('ALice',560000)

print('Hamza Balance : ', acc1.get_balance())
print('Alice Balance : ',acc2.get_balance())


#---------------- OBJECT -------------

acc1.deposit(6000)
acc2.withdraw(9000)

print('Hamza new Balance : ', acc1.get_balance())
print('Alice new 25011Balance : ',acc2.get_balance())


print("Hamza Interest : ",acc1.calculate_interesrt())
print("Alice Interest : ",acc2.calculate_interesrt())


