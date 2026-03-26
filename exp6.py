Grades = {"Alice":"A","Bob":"B"}
Attendance = {"Alice":90, "Bob":85}
Grades["Bob"] = "A"
Attendance["Bob"] = 88
Grades["Charlie"] = "C"
Attendance["Charlie"] = 80
Grades.pop("Alice")
Attendance.pop("Alice")
for Student in Grades:
    print(Student,"-Grade",Grades[Student],"Attendance",Attendance[Student])
