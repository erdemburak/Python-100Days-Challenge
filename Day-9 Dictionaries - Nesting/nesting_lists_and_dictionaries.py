"""
Docstring for Day-9 Dictionaries - Nesting.nesting

dictionary içerisine key value değerleri veriyoruz.
value değeri aynı zamanda bir [List] ya da farklı bir {dictionary} de olabilir.
{
    key: [List],
    key2: {Dict}
}
"""

capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}


print("---------- Printing from nested list in dictionary ----------")
# Nested List in Dictionary

travel_log = {
    "France": ["Paris","Lille","Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}

# Print Lille
print(travel_log["France"][1])

print("------------ Printing from Nested List ------------")
nested_liste = ["A","B", ["C","D"]]
# Print D
print(nested_liste[2][1])

print("------------ Printing from Nested dictionary -------------")
travel_log = {
    "France": {
        "num_times_visited": 8,
        "cities_visited": ["Paris","Lille","Dijon"],
    },
    "Germany": {
        "cities_visited": ["Stuttgart", "Berlin"],
        "total_visits": 5
    },
}

print(travel_log["France"]["cities_visited"][2])