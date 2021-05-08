name = input("What is your username? \n")
allowedUsers = ['Ebonnee', 'Kristina', 'Keenan']
allowedPassword = ['passwordEbonnee','passwordKristina','passwordKeenan']


if(name in allowedUsers):
    password = input("Your password? \n")
    userID = allowedUsers.index(name)

    if(password == allowedPassword[userID]):

        print('Welcome %s' % name)
        print('These are the available options:')
        print('1. Withdrawl')
        print('2. Cash Deposit')
        print('3. Complaint')

        selectedOption = int(input('Please select an option:'))
        

        if(selectedOption == 1):
            print('you selected %s' % selectedOption)

        elif(selectedOption == 2):
            print('you selected %s' % selectedOption)

        elif(selectedOption == 3):
            print('you selected %s' % selectedOption)

        else:
            print('Invalid Option selected, please try again')
            
    else:
        print('Password Incorrect, please try again')

    
else:
    print('Name not found, please try again')
    


import datetime
now = datetime.datetime.now()
print("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

Balance = 6000



if(selectedOption == 1):
    input("How much would you like to withdraw? \n")
    print('Please Take your cash')
    while selectedOption == 1:
        print('Welcome %s' % name)
        print('These are the available options:')
        print('1. Withdrawl')
        print('2. Cash Deposit')
        print('3. Complaint')

        break
        

elif(selectedOption == 2):
    Deposit = input("How much would you like to deposit? \n")
    sum = float(Balance) + float(Deposit)
    print('Your current Balance is', sum)
    while selectedOption == 2:
        print('Welcome %s' % name)
        print('These are the available options:')
        print('1. Withdrawl')
        print('2. Cash Deposit')
        print('3. Complaint')

        break
        
elif(selectedOption == 3):
    input("What issue would you like to report? \n")
    print('Thank you for contacting us')
    while selectedOption == 3:
        print('Welcome %s' % name)
        print('These are the available options:')
        print('1. Withdrawl')
        print('2. Cash Deposit')
        print('3. Complaint')

        break
