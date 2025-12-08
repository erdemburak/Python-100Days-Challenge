print("Hello"[0]) # index numarası neye denk geliyorsa onu çıkarır

# Integer
print(123+345)

# Large integers
print(123_456_789)

# Float - Floating point number
print(3.14159)

# Boolean
print(True)
print(False)

#---------------------------------------------------------------------------
# type kullanarak değişkenlerin türlerini öğrenebiliyorumz.
print(type("123456"))
print(type(123456))
print(type(123456))
print(type(True))


print("Welcome to the tip calculator")
bill_total = float(input("What was the total bill? "))
tip_percentage = int(input("How much tip would you like to give? 10, 12 or 15 "))
total_people = int(input("How many people to split the bill? "))

def each_persons_bill(bill,percent,ppl):
    return (bill + ((bill*percent)/100))/ppl

print(f"Each person should pay: ${each_persons_bill(bill_total,tip_percentage,total_people)}") 