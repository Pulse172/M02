#Jerron Jones
# Honors Calculator
#This program determines if a student makes the honor roll or not.

last_name = "none"

while last_name != "ZZZ":
    last_name = input("Enter student's last name. Type 'ZZZ' to exit program: ") #user inputs the students last name

    if last_name == "ZZZ" or last_name == "zzz": #Ends program if ZZZ is entered
        break

    first_name = input("Enter student's first name: ") #user enters first name
    gpa = float(input("Enter student's GPA: "))#user enters GPA

    if gpa >= 3.5:
        honors = "made the Dean's List." #determines if students get any honors
    elif gpa >= 3.25:
        honors = "made the Honor Roll."
    else:
        honors = "was not qualified for any honors."

    print(first_name, last_name, honors)#prints what honor student recieved