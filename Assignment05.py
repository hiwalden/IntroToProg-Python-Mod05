# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   WMarcus, 2/23/25, Created Script
# ------------------------------------------------------------------------------------------ #
#Import packages
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
student_first_name: str = ''
student_last_name: str = ''
course_name: str = ''
student_data: dict = {}
students: list = []
json_data: str = ''
file = None
menu_choice: str

#Read the data from Enrollments.json into a table
#--I anticipate FileNotFoundError as the most likely error, so I'll customize that message.
try:
    file = open(FILE_NAME, "r")
    students = json.load(file)
    file.close()
except FileNotFoundError as e:
    print("JSON file must exist before running this script!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
except Exception as e:
    print("General Exception\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
finally:
    if not file.closed:
        file.close()

#Establish interactive loop
while True:
    print(MENU)
    menu_choice = input("What would you like to do: ")

# Input user data
# -- The use case I'm fulfilling requires that no student names contain numbers.
    if menu_choice == "1":
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("Please re-attempt entering student information.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("Please re-attempt entering student information.")
        except ValueError as e:
            print("No part of any student name may contain numbers.")
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
            continue
        except Exception as e:
            print("-- Technical Error Message -- ")
            print("There was a non-specific error!\n")
            print(e, e.__doc__, type(e), sep='\n')
            continue

        course_name = input("Please enter the name of the course: ")
        student_data = {"FirstName":student_first_name,"LastName":student_last_name,"CourseName":course_name}
        students.append(student_data)
        print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        continue

# Present the current data
    elif menu_choice == "2":
        try:
            print("-"*50)
            for student in students:
                print(f"Student {student["FirstName"]} {student["LastName"]} is enrolled in {student["CourseName"]}")
            print("-"*50)
            continue
        except KeyError as e: #This is an expected exception, as Enrollments.json contains a key:value error.
            print("Unexpected Key:Value Pair in JSON File")
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
            continue
        except Exception as e:
            print("There was a non-specific error!\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
            continue

# Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file)
            file.close()
        except Exception as e:
            print("There was a non-specific error!\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
        finally:
            if not file.closed:
                file.close()
                continue 
        
    #Present Saved Data
        print("The following data was saved to file!")
        try:
            for each in students:
                print(f"Student {each["FirstName"]} {each["LastName"]} is enrolled in {each["CourseName"]}")
            continue
        except KeyError as e: #This is an expected exception, as Enrollments.json contains a key:value error
            print("Unexpected Key:Value Pair in JSON File")
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
        except Exception as e:
            print("There was a non-specific error!\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
        finally:
            continue

# Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")
        continue

print("Program Ended")
