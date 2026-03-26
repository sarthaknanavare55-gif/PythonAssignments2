#Experiment 1

class BankAccount:
    def __init__(self,account_number,balance=0.0):
        self.account_number=account_number
        self.balance=balance
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"Deposited:Rs.{amount:.2f}")
        else:
            print(f"Deposit amount must be greater than zero.") 
    def withdraw(self,amount):
        if 0 < amount <= self.balance:
            self.balance-=amount
            print(f"Withdrawn:Rs.{amount:.2f}")
        elif amount > self.balance:
            print(f"Insufficient Balance!")
        else:
            print(f"Withdrawal amount must be greater than zero.")
    def check_balance(self):
        print(f"Account {self.account_number} Balance:Rs.{self.balance:.2f}") 

account=BankAccount("05023028571",10000.00)
account.check_balance()
account.deposit(50000)
account.withdraw(2000)
account.check_balance()

#Experiment 2
class Library:
    def __init__(self,book_name,author,availability_status=True):
        self.book_name=book_name
        self.author=author
        self.availability_status=availability_status
    def check_out(self):
        if self.availability_status:
            self.availability_status=False
            print(f"Book '{self.book_name}' by {self.author} has been checked out.")
        else:
            print(f"Sorry, {self.book_name} is currently not available. ")

    def return_book(self):
        if not self.availability_status:
            self.availability_status=True
            print(f"Book '{self.book_name}' has been returned and is now available. ")
        else:
            print(f" Book '{self.book_name}' was not checked out.")

    def display_book_info(self):
        status="Available" if self.availability_status else "Checked out "
        print(f"Book:{self.book_name}, Author: {self.author}, Status:{status}")

book1=Library("Rich Dad Poor Dad"," Robert Kiyosaki")
book2=Library("Clean Code", "Robert C. Martin")  
book3=Library("The Pragmatic Programmer","Andrew Hunt")      

book1.display_book_info()
book2.display_book_info()
book3.display_book_info()

print("\n Checking out Books...")
book1.check_out()
book2.check_out()
book3.check_out()

print("\n Returning Books...")
book1.return_book()
book2.return_book()

print("\n Final Book Statuse.")
book1.display_book_info()
book2.display_book_info()
book3.display_book_info()

#Experiment 3
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show_person(self):
        print("Name:",self.name)
        print("Age:",self.age)
class Employee:
    def __init__(self,emp_id,salary):
        self.emp_id=emp_id
        self.salary=salary
    def show_employee(self):
        print("Employee Id:",self.emp_id)
        print("Salary:",self.salary)
class Manager(Person,Employee):
    def __init__(self,name,age,emp_id,salary,department):
        Person.__init__(self,name,age)
        Employee.__init__(self,emp_id,salary)
        self.department=department
    def show_manager(self):
        print("Deparment:",self.department)

m1=Manager("Rahul",25,123,75000,"IT")
m1.show_person()
m1.show_employee()
m1.show_manager()

#Experiment 4
class Vehicle:
    def move(self):
        print("The vehicle is moving")
class Car(Vehicle):
    def move(self):
        print("Driving on the road")
class Bicycle(Vehicle):
    def move(self):
        print("Pedaling on the road")

vehicles=[Car(),Bicycle()]

for v in vehicles:
    v.move()
    