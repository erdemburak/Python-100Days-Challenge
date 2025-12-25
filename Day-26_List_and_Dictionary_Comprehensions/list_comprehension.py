# List comprehension - bir listeyi kullanarak başka bir liste elde etme anlamındadır

# numbers = [1,2,3] # Bu listedeki her bir sayı değerini bir artırmak istediğimizde
# new_list = []
# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)
    # Bu şekilde 4 satır koda ihtiyacımız var. 

# List comprehension ile bu 4 satırı 1 satıra indirebiliyoruz.
# new_list = [new_item for item in List]
# yani bizim örneğimizde uygulama şu şekilde oluyor

# new_list = [n+1 for n in numbers]
# print(new_list)

# name = "Burak"
# letter_list = [letter for letter in name]
# print(letter_list)

# range_list = [num*2 for num in range(1,6)]
# print(range_list)

# List comprehension da if sorgusu kullanımı
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# short_names = [name for name in names if len(name)<5]
# long_uppercase_names = [name.upper() for name in names if len(name)>4]
# print(short_names)
# print(long_uppercase_names)

# Squaring Numbers using list comprehension
# numbers = [1,1,2,3,5,8,13,21,34,55]
# squared_numbers = [(item * item) for item in numbers]
# print(squared_numbers)

# Filtering even numbers using list comprehension
# list_of_strings = ['9','0','32','8','2','8','64','29','42','99']
# numbers = [int(num) for num in list_of_strings]
# result = [num for num in numbers if (num % 2 == 0) and num is not 0]
# print(numbers)
# print(result)

# Finding data that overlap between two files
with open("Day-26_List_and_Dictionary_Comprehensions/file1.txt") as file1:
    file1_numbers = file1.readlines()
    # Aşağıdaki kod ile hem filedan okunan verilerdeki boşlukları sildik hem de string 
    # türünde olan sayıları integer türüne çevirdik
    file1_numbers = [number.strip() and int(number) for number in file1_numbers]
    print(file1_numbers)

with open("Day-26_List_and_Dictionary_Comprehensions/file2.txt") as file2:
    file2_numbers = file2.readlines()
    file2_numbers = [number.strip() and int(number) for number in file2_numbers]
    print(file2_numbers)

result = [number for number in file1_numbers if number in file2_numbers]
print(result)