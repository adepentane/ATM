allowedUsers = ['Sheyi', 'Adepentane', 'Luke', 'James']
allowedPassword = ['PasswordSheyi', 'PasswordAdepentane', 'PasswordLuke', 'PasswordJames']

username = input("what is your username ?\n")

if (username in allowedUsers):
    password = input("Your Password ?\n")
    userId = allowedUsers.index(username)

    if (password == allowedPassword[userId]):
        print('Welcome &s' % username)
        print('These are the Available Options:')
        print('1. Withdrawal')
        print('2. Cash Deposit')
        print('3. Complaint')

        selectedOption = int(input('Please select and option \n')))

        if(selectedOption == 1):
            print('You selected %s' % selectedOption)
            pass
        elif(selectedOption == 2):
            print('You selected %s' % selectedOption)
            pass
        elif(selectedOption == 3):
            print('You selected %s' % selectedOption)
            pass
        else:
            print('Invalid Option Selected, please try Again')
    else:
        print('Password Incorrect, please try again')

    
else:
    print('Name not found, please try again')






