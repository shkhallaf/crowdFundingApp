import authentication
print("Welcome to the Crowd Funding Project :) ")
print ("""1-> Register  
2-> Login 
3-> Exit.""")
choice = input("Enter your choice : ")
while choice == "1" or choice == "2":
    if choice == "1":
        authentication.register()
    elif choice == "2":
        authentication.login()
    else:
        break
    print ("""1-> Register  
2-> Login 
3-> Exit.""")
    choice = input("Enter your choice : ")

