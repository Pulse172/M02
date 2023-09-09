last_name = "none"

while last_name != "ZZZ":
    last_name = input("Enter student's last name. Type 'ZZZ' to exit program: ")

    if last_name == "ZZZ" or last_name == "zzz":
        break

    first_name = input("Enter student's first name: ")
    gpa = float(input("Enter student's GPA: "))

    if gpa >= 3.5:
        honors = "made the Dean's List."
    elif gpa >= 3.25:
        honors = "made the Honor Roll."
    else:
        honors = "was not qualified for any honors."

    print(first_name, last_name, honors)