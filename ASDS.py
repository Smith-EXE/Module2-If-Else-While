# Ethan Smith ASDS.py Build Version 0.1

# This build will accept a input of a students names and GPA and output a message for each student entered displaying the students current academic standing. (Dean's list or Honor roll)
lName = ""
inInfo = True
print("Welcome to the student academic standing determination system! If you wish to exit enter 'ZZZ' as the students last name.")
while (inInfo == True):
    lName = str(input("Enter the students last name: "))
    if (lName == "ZZZ"): # This function will exit the program if the input for last name is equal to "ZZZ"
        exit()
    fName = str(input("Enter the students first name: "))
    gpa = float(input("Enter the students GPA: "))
    if (gpa >= 3.50):   # These If Statements will determine the students academic standing.
        print("Congrats!", fName, lName, "has made The Dean's List!")
    elif (gpa >= 3.25 and gpa < 3.5):
        print("Congrats!", fName, lName, "has made The Honor Roll!")
    else:
        print("Unfortunately", fName, lName, "needs to try harder.")
    
    
    
    
    