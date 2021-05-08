#register
# - first name, last name, password, email
# - generate user account


#login
# - account number and password


#bank operations

#Initializing the system
import random

database = {} #Dictionary
userdatabase = {}

def init():


    isValidOptionSelected = False
    print("Welcome to Bank of Hoggard")

    while isValidOptionSelected == False:

        haveAccount = int(input("Do you have an account with us?: 1 (yes) 2 (no) \n"))
        
        if(haveAccount == 1):
            isValidOptionSelected = True
            login()
        elif(haveAccount == 2):
            isValidOptionSelected = True
            register()
        else:
            print("You have selected an invalid option")

def login():

    print("Login to your account")

    isloginsuccessful = False

    while isloginsuccessful == False:
        accountNumberfromuser = int(input("What is your account number? \n"))
        password = input("What is your password? \n")

        for accountnumber, userdetails in userdatabase.items():
            if(accountnumber == accountNumberfromuser):
                if(userdetails[3] == password):
                    isloginsuccessful = True
                    
        print("Invalid account or password")
    bankOperation(userdetails)

def register():
    print("Register for new account")

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("Create password \n")

    accountNumber = generateAccountNumber()
    print(accountNumber)
    database[accountNumber] = [ first_name, last_name, email, password ]

    print("Your account has been created")

    login()

def bankOperation(user):

    print("Welcome %s %s " % ( user[0], user[1] ) )


    selectedOption = int(input("What would you like to do? (1) Deposit (2) Withdrawl (3) Logout (4) Exit /n"))

    if (selectedOption == 1):
            
        depositOperation()
    elif (selectedOption == 2):
            
        withdrawlOperation()
    elif (selectedOption == 3):
            
        login()
    elif (selectedOption == 4):
            
        exit()
    else:
        print("Invalid Option Selected")
        bankOperation(user)


def withdrawlOperation():
    print("Withdrawl Operations")

def depositOperation():
    print("Deposit Operations")

def generateAccountNumber():

    return random.randrange(1111111111,9999999999)



#### ACTUAL BANKING SYSTEM ####

init()