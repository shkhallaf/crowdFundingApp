import re
def validatePhone(phone):
    while not bool(re.search(r"^01[012][0-9]{8}$", phone)):
        phone = input("please enter a valid phone number : ")
    return phone
def validatePassword(password):
    passPattern = re.compile(r'^(?=\S{6,20}$)(?=.*?\d)(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[^A-Za-z\s0-9])')
    while not bool(re.search(passPattern, password)):
        password = input("Please enter a valid Password: ")
    print("you entered a Valid Password :)")
    confirmPass = input("Confirm password: ")
    while confirmPass != password:
        print("Passwords do not match :(")
        print("Enter password the same as you entered")
        confirmPass = input("Confirm password: ")
    print("the passwords are the same :)")
    return password
def validateFname(fname) :
    while not fname.isalpha():
        fname = input ("Please enter a valid name : ")
    return fname
def validateLname(lname):
    while not lname.isalpha():
        lname = input ("Please enter a valid name : ")
    return lname



    
    
    pass
def validateEmail (email):
    while not bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email)):
        email = input ("Please enter a valid Email address: ")
    print("valid email :) ")
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
    
    user = input ("Enter User Name : ")
    while not user.isalpha():
        user = input ("Enter User Name : ")
    password = input("Enter Password : ")
    logedInUser = checkUserAndPass(user, password)
    if logedInUser :
        print (f"hello {logedInUser} welcome back :) ")
    else:
        print("Invalid username or password :( ")
def register():
    fname = input ("Enter your first name : ")
    fname = validateFname(fname)
    lname = input ("Enter your last name : ")
    lname = validateLname(lname)
    password =input("Please enter a valid Password: ")
    password = validatePassword(password)
    email = input ("Please enter a valid Email address: ")
    email = validateEmail(email)
    mailAftercheckExistenceOfMail = checkExistenceOfMail(email)
    while mailAftercheckExistenceOfMail:
        print ("the email Already exists :( ")
        email= input("Please enter a new email : ")
        email = validateEmail(email)
        mailAftercheckExistenceOfMail = checkExistenceOfMail(email)

    phone = input("please enter a valid phone number : ")
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