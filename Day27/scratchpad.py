import pandas


students = {
    'student': ["Angela", "James", "Lily"],
    'score': [56, 76, 98]
}
# #looping through dictionaries:
# for (key, value) in students.items():
#     print(key)


import pandas
students_data_frame = pandas.DataFrame(students)
#
# for (key, value) in students_data_frame.items():
#     print(key)
#

# loop through rows of a data frame

for (index, row) in students_data_frame.iterrows():
    print(row.student)