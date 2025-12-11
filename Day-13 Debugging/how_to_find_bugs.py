def my_function():
    for i in range(1,20):
        if i == 20:
            print("You got it")

my_function()

# Describe the problem - Write your answers as comments:
# 1. What is the for loop doing?
#       1 den 19 a kadar olan sayılarda göngüye giriyor ama 
# 2. When is the function meant to print "You got it"?
#       if sorgusu 20 oldugunda print işlemini yapacak ama hiçbir zaman 20 olmayacak
# 3. What are your assumptions about the value of i?
#       döngüyü 1,20 yerine 1,21 yaparsak sorun çözülür

# --------------------- Another one ------------------------------------------

from random import randint
dice_images = [1,2,3,4,5,6]
dice_num = randint(1,6)
print(dice_num)
print(dice_images[dice_num])

# Rastgele sayı seçimi işleminde 1-6 arasındaki sayılardan çekiyor ama bunu index olarak kullanıyor.
# yani 1 den 5 e kadar sorun yok ancak rastgele sayı olarak 6 geldiğinde index out of range hatası alınıyor.
# çözüm olarak index kullanımlarında rastgele sayıyı 0 dan eleman sayısına kadar şeklinde kullanmak güvenli olur.

# --------------------- Another one ------------------------------------------
# Bilgisayar gibi düşünmeye çalışmalıyım. Her bir satırı bilgisayar nasıl işliyorsa o şekilde adım adım takip ettiğinde
# hatayı bulmak kolaylaşır.

year = int(input("What's your year of birth? "))

if year > 1980 and year < 1994:
    print("You are a Milennial.")
elif year > 1994:
    print("You are a Gen Z.")

# Bu koddaki sorgularda 1994 yılı dışında her şey normal ancak 1994 yılı sorguya dahil değil 
# Yani <= 1994 ile milennial sorgusuna ya da >= 1994 ile Gen Z sorgusuna dahil edilmeli