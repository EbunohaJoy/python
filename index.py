x = 2
y = 2
print(x + y)

students_count = 1000
rating = 4.99
is_published = False
print(students_count)
course_name = "python \"programming"
print(course_name)
message = """ 
hi, my name is joy
from enugu nigeria

"""


print(message)
print(len(message))
print(message[3])
print(course_name[0:3])
print(course_name[0:])
print(course_name[:3])
# joy is learning

# first = "Joy"
# last = "Chinaemerem"
# full = f"{first} {last} {3 + 4}"
# print(full)

# print(course_name.upper())
# print(course_name.lower())
# print(course_name.strip())
# print(course_name.lstrip())
# print(course_name.find("pro"))
# print(course_name.replace("p", "J"))
# print("pro" in course_name)
# print("ket" not in course_name)

# numbers
print(round(3.9))
print(abs(-3.9))

temperature = 15
if temperature > 30:
    print("its warm")
elif temperature > 20:
    print("its nice")
else:
    print("its cold")


age = 23
if age >= 18:
    message = "elligible"
else:
    message = "not eligible"
print(message)

agee = 10
joy = "eligible" if agee >= 18 else "not eligible"
print(joy)

# logical operators
# and not or

high_income = True
good_credit = True

if high_income and good_credit:
    print("eligible")
else:
    print("Not eligible")

if high_income or good_credit:
    print("eligible")
else:
    print("Not eligible")


student = True
if not student:
    print("eligible")
else:
    print("not eligible")


if high_income and good_credit and not student:
    print("not eligible")


if 10 == "10":
    print("a")
elif "bag" > "apple" and "bag" > "cat":
    print("b")
else:
    print("c")

# loops
for number in range(3):
    print(number)


for number in range(1, 4):
    print(number)


for number in range(1, 10, 2):
    print(number)

successful = False
for number in range(3):
    print("attempt")
    if successful:
        print("successful")
        break
else:
    print("attempted 3 times and failed")

# nested loops
for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")


print(type(5)
      )
print(type(range(5)))

for x in "pyhton":
    print(x)

for i in ["hoy", 2, 4]:
    print(i)

number = 100
while number > 0:
    print(number)
    number = number // 2


# command = ""
# while command.lower() != "quit":
#     command = input(">")
#     print("echo", command)


# function

def greet():
    print("hi dear")
    print("welcome")


greet()


def greet(firstname, lastname):
    print(f"hi dear {firstname}")
    print("welcome")


greet("joy", "Degirl")

# perform task, return value

round(1.9)


def get_greeting(name):
    return f"hi{name}"


message = get_greeting("joy")


file = open("content.txt", "w")
file.write(message)


def increment(number, by=1):
    return + by


print(increment(2))


def multiply(*numbers):
    print(*numbers)


multiply(2,4,5,6,6,4,3,2)


list = ["joy", "clinton", "kingsley", "lidia"]
print(list)
print(len(list))


tuples = ("ypu", "pop", "adam")
print(tuples)
print(type(tuples))

# y = list(tuples)
# y[1] = "changed"
# tuples = tuple(y)


# print(tuples)


# set

thisset = {1,3,4,5,6,6,3,2}
print(thisset)



thisdict = {
    "brand" : "GLK",
    "model" : "mustang",
    "year" : "2025"

}

print(thisdict)
print(thisdict['brand'])


# lamda
x = lambda a : a + 3
print(x(5))


# python class and objects

class person:
    x = 5

p = person()
print(p.x)



class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

P1 = Person("Joy", 27)

print(P1.name)
print(P1.age)



class Joy:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def myfunc(self):
        print("Hello my name is " + self.name)



J1 = Joy("Degirl", 20)
J1.myfunc()