import random

def add(n1,n2):
    return n1 + n2


def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1,3)
        new_item = add(new_item, item)
    b_list.append(new_item)
    print(b_list)

mutate([1,2,3,5,8,13])

# Satır başlarına yukarıdaki gibi kırmızı işareti koyup kodu debug modunda çalıştırdığımızda adım adım hareketleri takip edebiliriz.
# Bu şekilde 14. satırdaki append işleminin for döngüsü içinde olmadığı için bu hatanın oluştuğunu görmüş oluruz.