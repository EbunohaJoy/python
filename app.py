# name = "Joy"
# age = 89

# print(name.upper())
# print(type(age))



# class Dog:
#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed


#     def bark(self):
#         print("whoof whoof")



# dog1 = Dog("opp","yuti")
# dog1.bark()
# print(dog1.name)

# dog2 = Dog("tup","yret")
# dog2.bark()
# print(dog2.name)


# class Dog:
#     def __init__(self, name, breed,owner):
#         self.name = name
#         self.breed = breed
#         self.owner = owner


#     def bark(self):
#         print("whoof whoof")


# class owner:
#     def __init__(self,name, address,contact):
#         self.name = name
#         self.address = address
#         self.contact = contact
        


# owner1 = owner("Danny", "33 new strret", "94903-333")
# dog1 = Dog("opp","yuti", owner1)
# print(dog1.owner.name)


# owner2 = owner("ally", "43 new strret", "1003-333")
# dog2 = Dog("tup","yret",owner2)
# print(dog2.owner.name)


# class Person:
#     def __init__(self,name, age):
#         self.name = name
#         self.age = age
    
#     def greet(self):
#         print(f"My name is {self.name} i am {self.age} years old")



# person1 = Person("Joy", 78)
# person1.greet()


# person2 = Person("Joy2", 98)
# person2.greet()
# print(person2.name)


# class User:
#     def __init__(self,username,email,password):
#         self.username = username
#         self.email = email
#         self.password = password


#     def say_hi_to_user(self,user):
#         print(f"sending messahe to {user.username}: Hi {user.username}, its {self.username} ")



# user1 = User("Joy","@mail", "13243")

# user2 = User("Betty","@gmail", "abc")

# user1.say_hi_to_user(user2)
# print(user1.email)
# user1.email = "Joy@gmail.com"
# print(user1.email)


# class User:
#     def __init__(self,username,email,password):
#         self.username = username
#         self.__email = email
#         self.password = password

#     def clean_email(self):
#         return self.__email.lower().strip()
    

# user1 = User("Betty"," @gmail ", "abc")
# print(user1.__email)
# print(user1.clean_email())


# the consenting adult phyilosophy
# from datetime import datetime


# class User:
#     def __init__(self,username,email,password):
#         self.username = username
#         self._email = email
#         self.password = password
    
    # def get_email(self):
    #     print(f"email accessed at {datetime.now()}")
    #     return self._email
    
    # @property
    # def email(self):
    #     print("email accessed")
    #     return self._email


    # def set_email(self,new_email):
    #     if "@" in new_email:
    #         self._email = new_email
#     @email.setter
#     def email(self,new_email):
#         if "@" in new_email:
#             self._email = new_email


    

# user1 = User("Ada", "Fit@gmail.com", "123")
# user1.email = "this@is not an email"
# print(user1.email)

# user1.set_email("joy@gmail.com")
# print(user1.get_email())




# static attributes

# class User:
#     user_count = 0

#     def __init__(self,username,email):
#         self.username = username
#         self.email = email
#         User.user_count += 1

#     def display(self):
#         print(f"username: {self.username}, Email: {self.email}")


# user1 = User("Joy", "joy@gmail.com")
# user2 = User("sally", "sally@gmail.com")

# print(User.user_count)
# print(user1.display())

# class BankAccunt:
#     MIN_BALANCE = 100

#     def __init__(self,owner, balance =0):
#         self.owner = owner
#         self.balance = balance

#     def deposit(self,amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"{self.owner}'s new balance: ${self.balance}")
#         else:
#             print("Deposit amount must be positive")

#     @staticmethod
#     def is_valid_interest_rate(rate):
#         return 0<= rate <=5


# account = BankAccunt("Joy", 700)
# account.deposit(200)
# print(BankAccunt.is_valid_interest_rate(70))
# print(BankAccunt.is_valid_interest_rate(2))


# encapsulation

# class BadBankAccount:
#     def __init__(self, balance):
#         self.balance = balance

# account = BadBankAccount(0.0)
# account.balance = -1
# print(account.balance)


# class BankAccount:
#     def __init__(self):
#         self._balance = 0.0

#     @property
#     def balance(self):
#         return self._balance
    
#     def deposit(self,amount):
#         if amount <= 0:
#             raise ValueError("Deposit must be positive")
#         self._balance += amount

#     def withdraw(self,amount):
#         if amount <= 0:
#             raise ValueError("withdraw amount must be positive")
#         if amount >= self._balance:
#             raise ValueError("insufficient funds")
#         self._balance -= amount




# account = BankAccount()
# print(account.balance)
# account.deposit(200)
# print(account.balance)
# account.withdraw(100)
# print(account.balance)
# account.withdraw(500)


# class EmailService:
#     def _connect(self):
#          print("connecting to email server")

#     def _authenticate(self):
#          print("Authenticating")
    
#     def send_email(self):
#          self._connect()
#          self._authenticate()
#          print("sending email")
#          self._disconnect()

#     def _disconnect(self):
#          print("Disconnecting from email server")

    

# send = EmailService()
# send.send_email()


# inheritance

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print("vehicle is starting")

    def stop(self):
        print("vehicle is stopping")


class Car(Vehicle):
    def __init__(self, brand, model, year, number_of_doors, number_of_wheels):
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors
        self.number_of_wheels = number_of_wheels


class Bike(Vehicle):
    def __init__(self, brand, model, year, number_of_wheels):
        super().__init__(brand, model, year)
        self.number_of_wheels = number_of_wheels





car = Car("fors", "focus", 2005, 5, 4)
bike = Bike("hunder", "scoopy", 2018, 2)
print(car.__dict__)
print(bike.__dict__)
car.start()
bike.start()
bike.stop()
        