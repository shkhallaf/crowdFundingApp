import authentication
from termcolor import colored
print( colored("Welcome to the Crowd Funding Project :) " , 'green' ) )
print (colored( """1-> Register  
2-> Login 
3-> Exit.""" ,"yellow" ) )
choice = input(colored("Enter your choice : " ,'green'))
while choice == "1" or choice == "2":
    if choice == "1":
        authentication.register()
    elif choice == "2":
        authentication.login()
    else:
        break
    print (colored( """1-> Register  
2-> Login 
3-> Exit.""" ,"yellow" ) )
    choice = input(colored("Enter your choice : " ,'green'))



