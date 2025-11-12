student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    if row.student == 'Angela':
    #Access row.student or row.score
        print(row.score)