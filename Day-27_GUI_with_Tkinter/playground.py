"""
Docstring for playground

*args ile fonksiyona sınırsız şekilde veri eklenebilmesini sağlayabiliyoruz.
"""

def add(*args):
    result = 0
    for n in args:
        result += n
    return result


print(add(1,2,3,4,5,6,7,8,9,10))

"""
**kwargs - keyword args ile fonksiyonlara sınırsız şekilde keyword verebiliriz.
"""
def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

"""
    Aynı mantıkla **kwargs kullanarak tkinter gibi classlar oluşturabiliriz.
"""

class Car():
    def __init__(self, **kw):
        self.make = kw["make"] # Bu şekilde verdiğimizde eğer bu değere atama yapılmazsa kod hata verecek
        self.model = kw.get("model") # get kullandığımızda değer ataması yapılmazsa hata vermeyim "none" şeklinde dönecek

my_car = Car(make = "Nissan", model= "GT-R")
print(my_car.model)
