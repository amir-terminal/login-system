users = {}
status = ""
def desplaymenu():
    status = input("are you a registered y/n : press q to quite : \n")
    if status == 'y':
        oldUser()
    elif status == 'n':
        newUser()
    
        

def oldUser():
    name = input('username : ')
    if name in users:
        password = input('password : ')
        if users[name] != password:
            print("password wrong")
        else:
            print("you're logged in")


    else:
        print("name does not exit ")

def newUser():
    name = input("enter your username : ")
    if name in users:
        print("username already taken !")
    else:
        password = input("enter you're passcode : ")
        users[name] = password
        print("\n User created seccesfully")
while status != 'q':
    desplaymenu()
    