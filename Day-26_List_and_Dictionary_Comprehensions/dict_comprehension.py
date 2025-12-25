import random

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

students_scores = {student:random.randint(1,100) for student in names}
print(students_scores)

# passed_students = {student:students_scores[student] for student in names if students_scores[student] > 50} # My solution
passed_students = {student:score for (student,score) in students_scores.items() if students_scores[student] > 50} # Course's solution
print(passed_students)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
words = [word for word in sentence.split() if word]
result = {word:len(word) for word in words}
print(result)


weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {days:round((temp_c * (9/5) + 32), 1) for (days,temp_c) in weather_c.items()}
print(weather_f)