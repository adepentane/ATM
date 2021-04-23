import random
#register
#username
#email
#password

database= {} #dictionary List

def init():

    isValidOptionSelected = False
    print("Welcome to Bank Adepentane")

    while isValidOptionSelected == False:
        haveAccount = int(input("Do you have an account with us: 1 (YES) 2(NO) \n"))
        
        if(haveAccount == 1):
            isValidOptionSelected = True
            login()
        elif(haveAccount == 2):
            isValidOptionSelected == True
            register()
        else:
            print("You have selected an invalid option")
def login():
    print("This is the Login Function")

def register():
    print("This is the Register Function")

def bankOperation():
    print("Some Operations goes in here")

def generateAccountNumber():
    print ("Generating Account Number")
    return random.randrange(1111111111,9999999999)

####### Get Your Account Number Below #######

print(generateAccountNumber())