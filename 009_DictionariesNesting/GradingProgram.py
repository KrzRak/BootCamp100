# Grading Program v1.0.0
# -----------------------------------------------------
# Instructions
# -----------------------------------------------------
# You have access to a database of student_scores in the format of a dictionary. The keys in student_scores are the names of the students and the values are their exam scores.
# Write a program that converts their scores to grades. By the end of your program, you should have a new dictionary called student_grades that should contain student names for keys and their grades for values. The final version of the student_grades dictionary will be checked.
# DO NOT modify lines 1-7 to change the existing student_scores dictionary.
# DO NOT write any print statements.
# This is the scoring criteria:
#     Scores 91 - 100: Grade = "Outstanding"
#     Scores 81 - 90: Grade = "Exceeds Expectations"
#     Scores 71 - 80: Grade = "Acceptable"
#     Scores 70 or lower: Grade = "Fail"
# Expected Output
# '{'Harry': 'Exceeds Expectations', 'Ron': 'Acceptable', 'Hermione': 'Outstanding', 'Draco': 'Acceptable', 'Neville': 'Fail'}'
# Hint
# Remember that looping through a Dictionary will only give you the keys and not the values.
# If in doubt as to why your code is not doing what you expected, you can always print out the intermediate values.
# At the end of your program, the print statement will show the final student_scores dictionary, do not change this.
# -----------------------------------------------------

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
def add_grades(name):
    if student_scores[name] > 90:
        student_grades[name] = "Outstanding"
    elif student_scores[name] > 80:
        student_grades[name] = "Exceeds Expectations"
    elif student_scores[name] > 70:
        student_grades[name] = "Acceptable"
    else:
        student_grades[name] = "Fail"

for student in student_scores:
    add_grades(student)

# 🚨 Don't change the code below 👇
print(student_grades)