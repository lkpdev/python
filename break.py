student_name = ["abc", "def", "lmn", "xyz", "new"]

for name in student_name:
    if name == "def":
        print("Found student " + name)
        break
    print ("currently testing " + name)