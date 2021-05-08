# create record
# update record
# read record
# delete record
# CRUD

import os
import Validation

user_db_path = "data/user_record"

def create(account_number, user_details, first_name, last_name, email, password):
    user_data = first_name + "," + last_name + "," + password + "," + str(0)

    if does_account_number_exist(account_number):
        return False

    if (does_email_exist(email)):
        return False

    completion_state = False

    try:
        f = open(user_db_path + str(account_number) + ".txt", "x")
    except FileExistsError:

        print("User already exists")
        delete(account_number)

      
    else:
        f.write(str(user_details))
        completion_state = True

    finally:
        f.close()

        return completion_state





def read(user_account_number):


    is_valid_account_number = Validation.account_number_validation(user_account_number)
    try:

        if is_valid_account_number:
            f = open(user_db_path + str(user_account_number) + ".txt", "r")
        else:
            f = open(user_db_path + user_account_number, "r")

    except FileNotFoundError:

        print("User not found")

    except FileExistsError:
        
        does_file_contain_data = read(user_db_path + str(user_account_number + ".txt")
        if not does_file_contain_data:
            delete(user_account_number)
    except TypeError:
        print("Invalid Account Number Format")
    else:   
        return f.readline()
    return False

def update(user_account_number):
    print("update user record")

def delete(user_account_number):
    print("delete user record")

    is_delete_successful = False

    if os.path.exists(user_db_path + str(user_account_number) + ".txt"):
        try:

            os.remove(user_db_path + str(user_account_number + ".txt"))
            is_delete_successful = True

        except FileNotFoundError:
            print("user not found")
            

        return is_delete_successful

def does_email_exist(account_number, email):
    
    all_users = os.listdir(user_db_path)

    for user in all_users:
        user_list = str.split(str.split(user, ','))
        if email in user_list:
            return True
    return False

def does_account_number_exist(account_number):
    all_users = os.listdir(user_db_path)

    for user in all_users:

        if user == str(account_number) + ".txt":

            return True
    return False

def authenticated_user(accountNumber, password):

    if does_account_number_exist(accountNumber):

        user = str.split(read(accountNumber), ',')

        if password == user[3]:
            return user

    return False