students=[]

print("Welcome to the student Data Organizer")
print()

while True:
    print("1. Add student")
    print("2. Display All Student")
    print("3. Update Student Information")
    print("4. Delete student")
    print("5. Dispaly subject offered")
    print("6. Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        print("Enter Student details")
        id=int(input("Student ID: "))
        name=input("Name: ")
        age=int(input("Age: "))
        grade=input("Grade: ")
        dob=input("Date of Birth (YYY-MM-DD): ")
        subject=input("Subjects(comma-separated): ")
        
        id_dob=(id,dob)
        subjects=set()

        for x in subject.split(","):
            subjects.add(x)

        student={
            "name":name,
            "age":age,
            "grade":grade,
            "subject":subject,
            "info":id_dob
        }
        students.append(student)
        print("student added successfully")
    elif choice==2:
        print("\n")
        print("_ _ _ Display All Students _ _ _")
        for std in students:
            if len(students)!=0:
                print(f"student name is :{std["name"]}")
                print(f"student age is : {std["age"]}")
                print(f"student grade is : {std["grade"]}")
                print(f"student subject is : {std["subject"]}")
                print(f"student id is : {std["info"][0]}")
                print(f"student dob: {std ["info"][1]}")
