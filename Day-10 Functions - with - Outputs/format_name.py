"""

def my_function():
    result = 3*2
    return result

output = my_function()    

"""

def format_fname_sname(fname, sname):
    """bu fonksiyon kelimeleri ayrı ayrı alıp ilk harfini büyük yapıyor."""
    return f"{fname.capitalize()} {sname.capitalize()}"

def format_fullname(fname_sname):
    """Bu fonksiyon adı soyadı alıp ilk harflerini büyük yapıyor"""
    return fname_sname.title()

def format_only_first_letter(fname, sname):
    """Bu fonksiyon ad soyad alıp sadece baş harfi büyük yapıyor. diğer harfleri değiştirmiyor"""
    name = fname[0].upper() + fname[1:]
    surname = sname[0].upper() + sname[1:]
    return name + " " + surname

def format_string_with_spaces(str_with_space):
    """Bu fonksiyon önünde boşluk olan stringlerin ilk harfini büyük yapıyor."""
    return str_with_space.lstrip().capitalize()


first_name = input("What is your First Name: ")
second_name = input("What is your Second Name: ")
full_name = input("Enter full name (with a space between): ")

formated_name = format_fname_sname(first_name, second_name)
print(formated_name)

formated_name = format_fullname(full_name)
print(formated_name)

formated_name = format_only_first_letter(first_name,second_name)
print(formated_name)

print("Önünde boşluk olan stringlerde: " + format_string_with_spaces("   burak"))