def account_number_validation(accountNumber):
    if accountNumber:

        

            try:
                int(accountNumber)

                if len(str(accountNumber)) == 10:

                    return True
                else:
                    print("Invalid Account Type")
                    return False
            except ValueError:
                print("Invalid Account Number, Account Number should be an integer")
            except TypeError:
                print("Invalid Account Type")
                return False
        
    else:
        print("Account number is a required field")
        return False

