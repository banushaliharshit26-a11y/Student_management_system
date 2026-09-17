students=[]

print("Welcome to the Student Data Organizer")
print()

while True:
    print("1. Add student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete student")
    print("5. Display Subjects Offered")
    print("6. Exit")
    choice=int(input("Enter your choice: "))
    print()
    if choice == 1 :
        print("Enter Student Details")
        id=int(input("Enter Student ID: "))
        name=input("Enter Student Name: ")
        age=int(input("Enter Student Age: "))
        grade=input("Enter Student Grade: ")
        dob=input("Date of Birth (YYYY-MM-DD): ")
        subject=input("Subjects (comma-separated): ")
        print()
        
        id_dob=(id,dob)
        subjects=set(subject.split(","))

         

        student={
            "name":name,
            "age":age,
            "grade":grade,
            "subject":subjects,
            "info":id_dob
        }
        students.append(student)
        print("Student Added Successfully")
        print()
    elif choice == 2 :
        print("_ _ _ Display All Students _ _ _")
        for std in students:
            if len(students)!=0:
                print(f"Student ID: {std["info"][0]}| Name: {std["name"]}| Age: {std["age"]}| Grade: {std["grade"]}| Subjects: {std["subject"]}| DOB: {std["info"][1]}")
                print("...")
            print()
    elif choice == 3 :
        std_id=int(input("Enter a student id: "))
        for std in students:
            if std ["info"][0]==std_id:
        
                print("1. Update Name: ")
                print("2. Update Age:  ")
                print("3. Update Grade: ")
                print("4. Update Subjects: ")

                std_choice = int(input("Enter your choice between 1 to 4 : "))

                if std_choice == 1:
                    new_name = input("Enter the New Name: ")
                    std["name"]=new_name
                    print("Student Name Updated Successfully")
                    print()
                    

                elif std_choice == 2:
                    new_age=int(input("Enter New Age: "))
                    std["age"]=new_age
                    print("Student Age Updated Successfully")
                    print()
                    
                elif std_choice==3:
                    new_grade=input("Enter a New Grade: ")
                    std["grade"]=new_grade
                    print("Student Grade Updated Successfully")
                    print()
                    
                elif std_choice==4:
                   new_subject=input("Enter New Subjects: ")
                   subjects=set(new_subject.split(","))
                   std["subject"]=subjects
                   print("Subject Updated Successfully")
                   print()  
            
            else:
                print("Student ID not found")
        print()

    elif choice == 4 :
        student_id=int(input("Enter a Student ID: "))
        for x in students:
            if x ["info"][0]==student_id:
                students.remove(x)
                print("Student Removed Successfully!")
                print()
                break
            
        else:
            print("Student ID not found")

    elif choice==5 :
                a =set()
                for i in students:
                    for x in i["subject"]:
                        a.add(x)
                for subj in a:
                    print(subj)
                print()

    elif choice == 6 :
        print("Exited Successfully!")
        break

    else:
        print("Invalid Choice! Please try again.")
        print()
