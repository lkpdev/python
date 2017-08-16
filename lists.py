#student_names = []
student_names= ["abc", "xyz", "lmn"]
student_names[0] == "abc"
student_names[-1] == "lmn"

student_names.append("new")

print(student_names)
student_names==["abc", "xyz", "lmn"]
 #"abc" in student_names == True
#len(student_list) == 4
del student_names[2]
print(student_names)
print(student_names[1:])
print(student_names[1:-1])

#print(student_list)

for name in student_names:
    print("student name is {0}".format(name))