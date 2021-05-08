def create(accountNumber, allowedUsernames):

        f = open("data/user_record/" + str(accountNumber) + ".txt", "x")
        f.write(str(allowedUsernames))
        f.close()
        
def update(user_account_number):
    print("update user record")

def read(user_account_number):
    print("Read user record")

def delete(user_account_number):
    print("delete user record")

def find(user_account_number):
    print("Find user")

create(4008336494, ["Pia", 'Pie', 'reck@gmail.com', 'passwordSucess', 2000])