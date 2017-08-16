student_name=["a", "abc", "def", "xyz", "lmn", "new"]

for name in student_name:
    if name == "def":
        continue
        print("found student " + name)
    
    print("continue testing " + name)