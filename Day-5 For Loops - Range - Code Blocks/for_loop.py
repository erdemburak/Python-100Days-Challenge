"""
Docstring for Day-5 For Loops - Range - Code Blocks.for_loop

for item in list_of_items:
    # Do something to each item
"""

fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)
    print(fruit + " pie")

print("------------------------ Another one -------------------------")

student_scores = [150,142,165,139,843,34,176,44,23,68,124,76,95,45,78,23,99,56,74,33]
total_exam_score = sum(student_scores) # sum ile listedeki verilerin toplama işlemini yapabiliriz
print(total_exam_score)
# for döngüsü ile de yapalım
sum = 0
for score in student_scores:
    sum += score

print(sum)

print(max(student_scores)) # listedeki en büyük değeri verir 

# for döngüsü ile
highest_score = 0
for score in student_scores:
    if highest_score < score:
        highest_score = score
print(highest_score)

# -------------------- Range ---------------------

for number in range(1,11,2):
    print(number)

sum_1_to_100 = 0
for number in range(1,101):
    sum_1_to_100 += number

print(sum_1_to_100)