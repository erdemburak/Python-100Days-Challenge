import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

# My solution for Nato alphabet project
# nato_dictionary = {}

# for (index, row) in data.iterrows():
#     nato_dictionary[row.letter] = row.code

# print(nato_dictionary)

# user_input = "Armagan"

# phonetic_code = [nato_dictionary[letter] for letter in user_input.upper()]
# print(phonetic_code)

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)
