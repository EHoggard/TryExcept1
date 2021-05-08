import datetime
now = datetime.datetime.now()
print("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

import random

database = {} 
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

    name = input("What is your username? \n")
    allowedUsernames = ['Applejack489', 'Walker911', 'Zebra065']
    allowedPassword = ['passwordSucess','passwordOld','passwordToo']

    if(name in allowedUsernames):
        password = input("Your password? \n")
        userID = allowedUsernames.index(name)

    if(password == allowedPassword[userID]):
        print("Password Accepted")            
    else:
        print('Account or username is not valid')             
        
        
    bankOperation(allowedUsernames)

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

def bankOperation(allowedUsernames):

    print("Welcome %s %s " % ( allowedUsernames[0], allowedUsernames[1] ) )
    
    
    selectedOption = int(input("What would you like to do? (1) Deposit (2) Withdrawl (3) Complaint (4) Exit \n"))

    if (selectedOption == 1):
            
        depositOperation()
    elif (selectedOption == 2):
            
        withdrawlOperation()
    elif (selectedOption == 3):
            
        Complaint()
    elif (selectedOption == 4):
            
        exit()
    else:
        print("Invalid Option Selected")
        bankOperation(allowedUsernames)

Balance = 6000

def withdrawlOperation():
    input("How much would you like to withdrawl? \n")
    print("Please take your cash")

def depositOperation():
    Deposit = input("How much would you like to deposit? \n")
    sum = float(Balance) + float(Deposit)
    print('Your current Balance is', sum)

def Complaint():
    input("What issue would you like to report? \n")
    print("Thank you for contacting us")

def generateAccountNumber():

    return random.randrange(1111111111,9999999999)

init()