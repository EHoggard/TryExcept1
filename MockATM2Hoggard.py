allowedUsers = ['Ebonnee', 'Kristina', 'Keenan']
allowedPassword = ['passwordEbonnee','passwordKristina','passwordKeenan']

import time
current = time.localtime()
current_time = time.strftime("%H:%M")
print(current_time)

def main():
    if(name in allowedUsers):
        password = input("Your password? \n")
        userID = allowedUsers.index(name)

    if(password == allowedPassword[userID]):

        print('Welcome %s' % name)
        print('These are the available options:')
        print('1. Withdrawl')
        print('2. Cash Deposit')
        print('3. Complaint')

        selectedOption = int(input('Please select an option: \n'))
        

        if(selectedOption == 1):
            print('you selected %s' % selectedOption)
            withdrawlATM()
        elif(selectedOption == 2):
            print('you selected %s' % selectedOption)
            deposit()
        elif(selectedOption == 3):
            print('you selected %s' % selectedOption)
            review()
        elif(selectedOption != 1, selectedOption != 2, selectedOption != 3):
            print('Invalid option selected, please try again.')
    else:
        print('Invalid Option selected, please try again')


    




import datetime
#now = datetime.datetime.now()
#print("Current date and time : ")
#print (now.strftime("%Y-%m-%d %H:%M:%S"))
print(current_time)

Balance = 6000



def withdrawlATM():
    input("How much would you like to withdraw? \n")
    print('Please Take your cash')
    
        

def deposit():
    Deposit = input("How much would you like to deposit? \n")
    sum = float(Balance) + float(Deposit)
    print('Your current Balance is', sum)
        
def review():
    input("What issue would you like to report? \n")
    print('Thank you for contacting us')