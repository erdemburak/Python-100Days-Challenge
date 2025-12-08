import random
import my_module

# iki sayı arasındaki değerlerden rastgele integer 
random_integer_between_range = random.randint(5, 25)
print(random_integer_between_range)

# my module dosyasından veri çekildi
print(my_module.my_favorite_random_number)

random_number_0_to_1 = random.random() # değer aralığını değiştirmek için burayı hangi aralığa ihtiyacımız varsa onunla çarpabiliriz.
print(random_number_0_to_1)

random_float = random.uniform(1, 10)
print(random_float)

# 0-1 arasında rastgele seçiyor ve eğer sayı 0 ise "Heads" 1 ise "Tails"
random_coin_flip = random.randint(0,1)
if random_coin_flip == 0:
    print("Heads")
else: 
    print("Tails")