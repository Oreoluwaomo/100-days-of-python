students_scores = {"students":["Alice","kola","bola","tola"],
                   "scores": [90,59,65,34]
                   }
import pandas as pd
student_dataframe = pd.DataFrame(students_scores)
print(student_dataframe)

# loop through a dataframe
for (key,value) in student_dataframe.items():
    print(key)
    print(value)

# using pandas iterrows to loop through
for (index,row) in student_dataframe.iterrows():
    print(index)
    print(row.students)