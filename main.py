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
    choice=(input("Enter your choice: "))
    if choice=="1":
        print("Enter Student details")
        id=int(input("Enter a Student ID: "))
        name=input("Enter a Student Name: ")
        age=int(input("Enter a Student Age: "))
        grade=input("Enter a Student Grade: ")
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
            "subject":subjects,
            "info":id_dob
        }
        students.append(student)
        print("student added successfully")
    elif choice=="2":
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

    elif choice=="3":
        std_id=int(input("Enter a student id: "))
        for std in students:
            if std ["info"][0]==std_id:
        
                print("1. for update name: ")
                print("2. for update age:  ")
                print("3. for update grade: ")
                print("4. for update subjects: ")

                std_choice = int(input("Enter your choice between 1 to 4 : "))

                if std_choice == 1:
                    new_name = input("enter the new name: ")
                    std["name"]=new_name
                    print("student name updated successfully")
                elif std_choice == 2:
                    new_age=int(input("enter new age: "))
                    std["age"]=age
                    print("Age update successfully")
                elif std_choice==3:
                    new_grade=input("enter a new grade: ")
                    std["grade"]=grade
                    print("student Grade updated successfully")
                elif std_choice==4:
                    new_subject=input("enter new subject: ")
                    std["subject"]=subject
                    print("Subject Update Successfully")
                else:
                    print("student update scuessfully!")


            else:
                print("id are not found")

    
    elif choice=="4":
        student_id=int(input("Enter a student id"))
        for x in students:
            if x ["info"][0]==student_id:
                students.remove(x)
                print("student remove successfully!")     
        else:
            print("student id not found")



    elif choice=="6":
        print("Exit Successfully!")
        break
