"""
{Key: Value}
{
    "Key": "Value"
    "Bug": "An error in a program that prevent the program from running as expected.",
}
"""

programming_dictionary = {
    "Bug": "An error in a program that prevent the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

print(programming_dictionary["Bug"])

# dictionary içine veri ekleme 

programming_dictionary["Loop"] = "The action of doing something oven and over again."

empty_dictionary = {}

# wipe an existing dictionary

# programming_dictionary = {}
# print(programming_dictionary)


# Edit
programming_dictionary["Bug"] = "Edited value for 'Bug'"

print(programming_dictionary)

#loop through a dictionary
for key in programming_dictionary:
    print(key + ": " + programming_dictionary[key])