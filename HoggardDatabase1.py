def create(accountNumber, allowedUsernames):

    completionstate = False

    try:
        f = open("Data/user_record/" + str(accountNumber) + ".txt", "x")
    except FileExistsError:
        print("User already exists")
        return completionstate
    else:
        f.write(str(allowedUsernames))
        completionstate = True
    finally:
        f.close()
    return completionstate

def update(user_account_number):
    print("update user record")

def read(user_account_number):
    print("Read user record")

def delete(user_account_number):
    print("delete user record")

def find(user_account_number):
    print("Find user")

