Student={}

while True:
    print("Welcome to the Student Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Check Result")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        name = input("Enter student name: ")
        age = input("Enter student age: ")
        marks = input("Enter student marks: ")
        Student[name] = {'age': age, 'marks': marks}
        print(f"Student {name} added successfully.")
        
    elif choice == '2':
        if not Student:
            print("No students found.")
        else:
            print("List of Students:")
            for name, info in Student.items():
                print(f"Name: {name}, Age: {info['age']}, Marks: {info['marks']}")
                
    elif choice == '3':
        name = input("Enter student name to check result: ")
        if name in Student:
            info = Student[name]
            if int(info['marks']) >= 50:
                print(f"Student {name} has passed with marks: {info['marks']}")
            else:
                print(f"Student {name} has failed with marks: {info['marks']}")
        else:
            print("Student not found.")
    elif choice == '5':
        print("Exiting the system. Goodbye!")
        break
        
    else:
        print("Invalid choice. Please try again.")
