"""
Docstring for Day-4 Randomisation - Lists.list_usage

list ile yapılabilecekler
https://docs.python.org/3/tutorial/datastructures.html
"""

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", 
                     "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", 
                     "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", 
                     "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", 
                     "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", 
                     "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", 
                     "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", 
                     "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america[-3])

# states_of_america[1] = "Pencilvania" şeklinde list içerisindeki değerler değiştirilebilir
# states_of_america.append("Ankara") şeklinde yeni ekleme yapılabilir.

# .extend ile iki farklı liste birleştirilebilir.

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery"]
vegetables = ["Spinach", "Kale", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)