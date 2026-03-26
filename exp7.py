students = {}

def add_student():
    name = input("Enter student name: ")
    grade = input("Enter grade: ")
    attendance = int(input("Enter attendance percentage: "))

    students[name] = {
        "grade": grade,
        "attendance": attendance
    }
    print(f"Student '{name}' added successfully!\n")

def update_student():
    name = input("Enter student name to update: ")

    if name in students:
        print("1. Update Grade")
        print("2. Update Attendance")
        choice = input("Choose field to update (1/2): ")

        if choice == '1':
            new_grade = input("Enter new grade: ")
            students[name]["grade"] = new_grade
            print("Grade updated!\n")

        elif choice == '2':
            new_att = int(input("Enter new attendance: "))
            students[name]["attendance"] = new_att
            print("Attendance updated!\n")
