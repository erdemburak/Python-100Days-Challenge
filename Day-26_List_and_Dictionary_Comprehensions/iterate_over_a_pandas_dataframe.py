student_dict = {
    "student": ["Burak", "Armağan", "Erdem"],
    "score": [56,100,90]
}

# # Looping through dictionaries:
# for (key,value) in student_dict.items():
#     print(value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# # Loop through a data frame
# for (key, value) in student_data_frame.items():
#     print(value)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    print(f"{row.student} {row.score}")

# {new_key:new_value for (index, row) in df.iterrows()}

