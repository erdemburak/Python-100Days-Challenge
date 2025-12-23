# file = open("/Users/elessar/Documents/Python/Python-100Days/Day-24_Files_Directories_and_Paths/my_file.txt")

# content = file.read()
# print(content)

# file.close()

"""Bu şekilde bir dosya açıldığında dosyanın kapatılması gerekiyor. Ancak yazılacak kodun uzunluğu değişeceğinden
    kapatma işleminin unutulma ihtimaline karşılık olarak kullanımı aşağıdaki şekilde yapmak daha doğru olabilir."""

with open("Day-24_Files_Directories_and_Paths/my_file.txt") as file:
    content = file.read()
    content = content.replace("Burak", "Armağan")
    print(content)

""" Yukarıdaki şekilde dosyayı açtığımızda read only şeklinde kullanılabilir bunu aşağıdaki gibi mode değiştirerek yapabiliriz
    mode="w" yaptığımızda yazmaya izin verir ama dosya içindekileri sıfırlayarak yazar. a ile append işlemi yapılabilir """

with open("Day-24_Files_Directories_and_Paths/my_file.txt", mode="a") as file:
    file.write("\nNew Text.")


# Eğer açmaya çalıştığımız dosya mevcut değilse. dosyayı oluşturup o şekilde açar