import re 
from termcolor import colored
def validatePhone(phone):
    while not bool(re.search(r"^01[012][0-9]{8}$", phone)):
        phone = input(colored( "please enter a valid phone number : " , 'green'))
    return phone
def validatePassword(password):
    passPattern = re.compile(r'^(?=\S{6,20}$)(?=.*?\d)(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[^A-Za-z\s0-9])')
    while not bool(re.search(passPattern, password)):
        password = input(colored("Please enter a valid Password: ",'green'))
    print(colored("you entered a Valid Password :)",'yellow'))
    confirmPass = input(colored("Confirm password: ",'green'))
    while confirmPass != password:
        print(colored("Passwords do not match :(",'yellow'))
        print(colored("Enter password the same as you entered","yellow"))
        confirmPass = input(colored("Confirm password: ",'green'))
    print(colored("the passwords are the same :)",'yellow'))
    return password
def validateFname(fname) :
    while not fname.isalpha():
        fname = input (colored("Please enter a valid name : ",'green'))
    return fname
def validateLname(lname):
    while not lname.isalpha():
        lname = input (colored("Please enter a valid name : ",'green'))
    return lname



    
    
    pass
def validateEmail (email):
    while not bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email)):
        email = input (colored("Please enter a valid Email address: ","green" ))
    print(colored("valid email :) ","yellow"))
    return email
    pass
def checkUserAndPass(user, password):
    try :
        file = open("users.txt"  , "r")
        data = file.readlines()
        dataForEachUser=[]
        for ele in data :
            userData = ele.split(",")
            dataForEachUser.append(userData)
        # print(dataForEachUser)
        for dataOfUser in dataForEachUser :
            # print(dataOfUser[0] , dataOfUser[3])
            # print(user , password)
            if dataOfUser[0]==str(user) and dataOfUser[3]==str(password):
                return user
            else :
                continue
    except Exception as e:
        file = open ("errors.txt", "w")
        file.write (str(e))
        file.close()
    return
def checkExistenceOfMail(email):
    try :
        file = open("users.txt"  , "r")
        data = file.readlines()
        dataForEachUser=[]
        for ele in data :
            userData = ele.split(",")
            dataForEachUser.append(userData)
        for dataOfUser in dataForEachUser :
            if dataOfUser[2]==str(email) :
                return email
            else :
                continue 
    except Exception as e:
        file = open ("errors.txt", "w")
        file.write (str(e))
        file.close()
    return
def login():
    
    user = input (colored("Enter User Name : ",'green'))
    while not user.isalpha():
        user = input (colored("Enter User Name : ",'green'))
    password = input(colored("Enter Password : ",'green'))
    logedInUser = checkUserAndPass(user, password)
    if logedInUser :
        print (colored(f"hello {logedInUser} welcome back :) ",'yellow'))
    else:
        print(colored("Invalid username or password :( ","yellow"))
def register():
    fname = input (colored("Enter your first name : ",'green'))
    fname = validateFname(fname)
    lname = input (colored("Enter your last name : ","green"))
    lname = validateLname(lname)
    password =input(colored("Please enter a valid Password: ",'green'))
    password = validatePassword(password)
    email = input (colored("Please enter a valid Email address: ",'green'))
    email = validateEmail(email)
    mailAftercheckExistenceOfMail = checkExistenceOfMail(email)
    while mailAftercheckExistenceOfMail:
        print (colored("the email Already exists :( ","yellow"))
        email= input(colored("Please enter a new email : ","green"))
        email = validateEmail(email)
        mailAftercheckExistenceOfMail = checkExistenceOfMail(email)

    phone = input(colored("please enter a valid phone number : ",'green'))
    phone = validatePhone(phone)
    data = f"{fname},{lname},{email},{password},{phone}\n"
    try:
        file = open("users.txt", "a")
        file.write(data)
        file.close()
    except Exception as e:
        file = open ("errors.txt", "w")
        file.write (e)
        file.close()