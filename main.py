# First Name: Beby
# Last Name: Alexis
# Class: SDEV 300
# Project: Week1_Assignment
# Date: March 17 /2024
"""
This is a python program for voter registration.
"""



print("United States Registration Office")
print("Welcome to the Python Voter Registration Application.")
# infinite loop
while True:
    # Soliciting the user's preference to proceed
    option = input("Do you want to continue with Voter Registration? (yes/no)\n").lower()
    # if the user entered yes ask for requisite information
    if option == "yes":
        # prompt the user for the first name
        fname = input("What is your first name?\n")
    # if the user doesn't want to continue, exit from the program
    else:
        break
    # Soliciting the user's preference to proceed
    option = input("Do you want to continue with Voter Registration? (yes/no)\n").lower()
    # if the user entered yes ask for requisite information
    if option == "yes":
        # asking for the lastname
        lname = input("What is you last name?\n")
    # if the user doesn't want to continue, exit from the program
    else:
        break
    # Soliciting the user's preference to proceed
    option = input("Do you want to continue with Voter Registration? (yes/no)\n").lower()
    # if the user entered yes ask for the requirements
    if option == "yes":
        # validating age between 18 and 120
        while True:
            try:
                age = int(input("What is your age?\n"))
                if 25 < age < 120:
                    break
                else:
                    print("Age should be >25 and <120")
            # if there is any exception continue and ask again
            except:
                continue
    # if the user doesn't want to continue, exit from the program
    else:
        break
    # Soliciting the user's preference to proceed
    option = input("Do you want to continue with Voter Registration? (yes/no)\n").lower()
    # if the user entered yes ask for requisite information
    if option == "yes":
        # prompt the user for citizenship
        citizen = input("Are you a U.S. Citizen? (yes/no)\n")
    # if the user doesn't want to continue, exit from the program
    else:
        break
    # asking if the user wants to continue
    option = input("Do you want to continue with Voter Registration? (yes/no)\n").lower()
    # if the user entered yes, ask for requisite information
    # check if the state entered by user has two letters
    if option == "yes":
        while True:
            try:
                state = input("What state do you live?\n")
                if len(state) == 2:
                    break
                else:
                    print("Please enter the two letters of your state\n")
            except:
                continue
    else:
        break
    # asking if the user wants to continue
    option = input("Do you want to continue with Voter Registration? (yes/no)\n").lower()
    # if the user entered yes, ask for requisite information
    if option == "yes":
        # ask for zip code
        zipcode = input("What is your zipcode?\n")
        # display the information

        print("\nThanks for registering to vote. Here is the information we received.")
        print("Name (first last): {} {}".format(fname, lname))
        print("Age: {}".format(age))
        print("U.S. Citizen: {}".format(citizen))
        print("State: {}".format(state))
        print("Zipcode: {}".format(zipcode))
        print("Thanks for trying the Voter Registration Application.")
        print("Your voter registration card should be shipped within 15 business days .")
        print("YOUR VOTE IS YOUR VOICE !")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
