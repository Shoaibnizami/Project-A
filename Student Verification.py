namelist = ["Zahid", "Kumail", "Wahid", "Hammad"]

ID = {"Zahid": "42111", "Kumail": "42115", "Wahid": "99871", "Hammad": "10105"}


total_students = len(namelist)
print("Enter your 6 digits ID number for further process")

StuID = input("Please enter your Student ID: ")

if StuID in ID.values():

    if StuID == ID["Zahid"]:
        print("You are enrolled in Diploma of Cyber Security")
        print("Hi Mr.", namelist[0])

    elif StuID == ID["Kumail"]:
        print("You are enrolled in the Diploma of Artificial Intelligence")
        print("Hi Mr.", namelist[1])

    elif StuID == ID["Wahid"]:
        print("You are enrolled in the Diploma of Machine Learning")
        print("Hi Mr.", namelist[2])

    elif StuID == ID["Hammad"]:
        print("You are enrolled in the Diploma of DevOps")
        print("Hi Mr.", namelist[3])

    else:
        print("No diploma program found for this student ID")
    print("Student ID:", StuID)

else:
    print("No student found with this ID, Enter your name and email address for registration")


print("Enter your CNIC number to verify before login at our LMS portal")
cnic = input("Enter CNIC number (xxxxx-xxxxxxx-x): ")

if len(cnic) == 15 and cnic.count('-') == 2:
    print("CNIC verification successful!")
    print("Entered CNIC:", cnic)
else:
    print("Invalid CNIC format. Please enter a valid CNIC number.")