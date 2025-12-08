"""
Docstring for Day-3 Conditional - Logic.challange-of-day3
"""

if True and not False: # and, or, not işlemleri birden fazla sorguda kullanılıyor. True olduğunda içine girecek False olduğunda girmeyecek
    print("True")


print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0

if size == "S":
    bill = 15
    print(f"Small pizza is ${bill}")
elif size == "M":
    bill = 20
    print(f"Medium pizza is ${bill}")
elif size == "L":
    bill = 25
    print(f"Medium pizza is ${bill}")
else: 
    print("Wrong size")

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill +=3
    print(f"with pepperoni its: ${bill}")

if extra_cheese == "Y":
    bill += 1
    print(f"With extra cheese the total is : ${bill}")