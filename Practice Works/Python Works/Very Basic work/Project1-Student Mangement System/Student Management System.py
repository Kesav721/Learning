import random
from datetime import datetime

Name_List = []
Roll_no_List = []
Age_List = []
Department_List = []
Marks_List = []
Student_ID=0
Student_ID_List=[]
Time_List=[]

def login():
    while True:
        print("        LOGIN        \n")
        username = input("Username: ")
        password = input("Password: ")

        if username == 'a' and password == 'a':   #enter the username & password
            print("You are logged in\n")
            return True
        else:
            
            print("Try again! \n")

def get_function():
    print("Choose an option:")
    print("ADD - Add Student Record")
    print("VIEW - View Student Records")
    print("EDIT - Edit Student Record")
    print("DEL - Delete Student Record")
    print("TOP - View Top Performer")
    print("S - Search by Student ID") 
    print("Q - Quit\n")
    choice = input("Enter the function to perform: ").upper()
    return choice

def add_details():
    Name = input("\nEnter the name: ")
    Roll_No = input("Enter the Roll number: ")
    Age = input("Enter the Age: ")
    Department = input("Enter the Department: ")
    Marks = input("Enter the Marks: ")

    Name_List.append(Name)
    Roll_no_List.append(Roll_No)
    Age_List.append(Age)
    Department_List.append(Department)
    Marks_List.append(Marks)
    student_ID_generator()
    time_record()
    print("\nStudent details added successfully!\n")
    with open("Student_Records.txt", "w") as file:
                file.write("---- STUDENT RECORDS ----\n\n")
                for i in range(len(Name_List)):
                    file.write(f"Name: {Name_List[i]}\n")
                    file.write(f"Roll No: {Roll_no_List[i]}\n")
                    file.write(f"Age: {Age_List[i]}\n")
                    file.write(f"Department: {Department_List[i]}\n")
                    file.write(f"Marks: {Marks_List[i]}\n")
                    file.write("-------------------------\n")
    print("Data successfully saved to Student_Records.txt\n")
    
    

def details_printer():
    print("\n--- STUDENT RECORDS ---")
    for i in range(len(Name_List)):
        print(f"Name: {Name_List[i]}")
        print(f"Roll No: {Roll_no_List[i]}")
        print(f"Age: {Age_List[i]}")
        print(f"Department: {Department_List[i]}")
        print(f"Marks: {Marks_List[i]}")
        print(f"Entry Time: {Time_List[i]}") 
        print("-----------------------")

def editor():
    edit_roll_no = input("Enter the Roll Number of the student to edit: ")

    if edit_roll_no in Roll_no_List:  
        index = Roll_no_List.index(edit_roll_no)

        print("\nCurrent details of the student:")
        print(f"1. Name: {Name_List[index]}")
        print(f"2. Roll No: {Roll_no_List[index]}")
        print(f"3. Age: {Age_List[index]}")
        print(f"4. Department: {Department_List[index]}")
        print(f"5. Marks: {Marks_List[index]}")
        print("-----------------------")

        print("\nWhich detail do you want to edit?")
        print("1 - Name")
        print("2 - Age")
        print("3 - Department")
        print("4 - Marks")
        print("5 - Edit All")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            Name_List[index] = input("Enter new name: ")
        elif choice == "2":
            Age_List[index] = input("Enter new age: ")
        elif choice == "3":
            Department_List[index] = input("Enter new department: ")
        elif choice == "4":
            Marks_List[index] = input("Enter new marks: ")
        elif choice == "5":
            Name_List[index] = input("Enter new name: ")
            Age_List[index] = input("Enter new age: ")
            Department_List[index] = input("Enter new department: ")
            Marks_List[index] = input("Enter new marks: ")
        else:
            print("Invalid choice! No changes made.\n")
            return

        print("\n Record updated successfully!\n")

        with open("Student_Records.txt", "w") as file:
            file.write("---- STUDENT RECORDS ----\n\n")
            for i in range(len(Name_List)):
                file.write(f"Student ID: {Student_ID_List[i]}\n")
                file.write(f"Name: {Name_List[i]}\n")
                file.write(f"Roll No: {Roll_no_List[i]}\n")
                file.write(f"Age: {Age_List[i]}\n")
                file.write(f"Department: {Department_List[i]}\n")
                file.write(f"Marks: {Marks_List[i]}\n")
                file.write("-------------------------\n")

        print("Changes saved to Student_Records.txt\n")

    else:
        print("Roll number not found!\n")


def delete():
    delete_roll_no = input("Enter the roll number to delete: ")  
    if delete_roll_no in Roll_no_List:  
        index = Roll_no_List.index(delete_roll_no)
        del Name_List[index]
        del Roll_no_List[index]
        del Age_List[index]
        del Department_List[index]
        del Marks_List[index]
        del Time_List[index]
        print("Record deleted successfully!\n")
    else:
        print("Roll number not found!\n") 

    with open("Student_Records.txt", "w") as file:
                    file.write("---- STUDENT RECORDS ----\n\n")
                    for i in range(len(Name_List)):
                        file.write(f"Name: {Name_List[i]}\n")
                        file.write(f"Roll No: {Roll_no_List[i]}\n")
                        file.write(f"Age: {Age_List[i]}\n")
                        file.write(f"Department: {Department_List[i]}\n")
                        file.write(f"Marks: {Marks_List[i]}\n")
                        file.write("-------------------------\n")
    print("Data successfully saved to Student_Records.txt\n")


def student_ID_generator():
    global Student_ID
    Student_ID+=1
    print(f"The students ID is : {Student_ID}")
    Student_ID_List.append(Student_ID)
    

def search():
    try:
        ID_to_search = int(input("Enter the Student ID: "))
        if ID_to_search in Student_ID_List:
            index = Student_ID_List.index(ID_to_search)
            print("\nThe result of the search is:\n")
            print(f"Name: {Name_List[index]}")
            print(f"Roll No: {Roll_no_List[index]}")
            print(f"Age: {Age_List[index]}")
            print(f"Department: {Department_List[index]}")
            print(f"Marks: {Marks_List[index]}")
            print("-----------------------")
        else:
            print("Student ID not found!\n")
    except ValueError:
        print("Invalid input! Please enter a numeric Student ID.\n")


    
    

def top_performer():
    if len(Marks_List) == 0:
        print("No student records available!\n")
    else:
        max_marks = max(Marks_List)
        print(f"\nTop Performer(s) with {max_marks} marks:")
        for i in range(len(Marks_List)):
            if Marks_List[i] == max_marks:
                print("Student ID:", Student_ID_List[i])
                print("Name:", Name_List[i])
                print("Roll No:", Roll_no_List[i])
                print("Department:", Department_List[i])
                print("-----------------------")
        print()

    

def time_record():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    Time_List.append(current_time)
    print("Time of entry: ",current_time)

if login():  
    while True:
        choice = get_function()

        if choice == "ADD":
            add_details()
        elif choice == "VIEW":
            details_printer()
        elif choice == "EDIT":
            editor()
        elif choice == "DEL":
            delete()
        elif choice == "TOP":   
            top_performer()
        elif choice == "CSV":
            to_csv()
        elif choice == "S":
            search()
        elif choice == "Q":
            print("Logging out... Goodbye!")
            break
        else:
            print("Invalid option! Try again.\n")
