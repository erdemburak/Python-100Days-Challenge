## hataları bulma amacıyla kod içerisindeki değerlerin olması gerektiği yerde doğru olup olmadığını o adımlarda
## print ile değerine bakarak çözebiliriz

word_per_page = 0
pages = int(input("Number of pages: "))
print(pages)
word_per_page == int(input("Number of words per page: "))
print(word_per_page) # Hata bu satırla bulunacak ve word_per_page değişkeninin == nedeniyle güncellenmediğini göreceğiz
                     # olması gereken bir tane = kullanmak
total_words = pages * word_per_page

print(total_words)