import os
import time
def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

class User:

    def __init__(self, first_name, last_name, email, password, status='inactive'):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self. password= password 
        self.status=status

    def display_user(self):
        print(f"First name: {self.first_name}")   
        print(f"Last name: {self.last_name}") 
        print(f"Email: {self.email}") 
        print(f"Password: {self. password}") 
        print(f"Status: {self.status}") 
        print('_'*20)

def create_user():
    first_name=input("Enter first name: ")
    last_name=input("Enter last name: ")  
    email=input("Enter email: ")       
    password=input("Enter password: ")

    return User(first_name,last_name,email,password) 

new_users=[]
while True:
    print("\n welcome to user management \n")
    print("\n choose an action: \n")
    print("1. Add new user")
    print("2.Display all users")
    print("3.Exit /n")

    choice=input("Enter your choice: ")

    if choice=='1':
        new_users.append(create_user())
        print("User added successfully!")
        time.sleep(2)
    elif choice=='2':
        clear_screen()
        if new_users:
            print("Displaying all new_users.....")
            time.sleep(2)
            for i in new_users:
                i.display_user()
            time.sleep(2)
        else:
            print("sorry, didnot find any user to display!")
            time.sleep(2)
    elif choice=='3':
        print("Exiting......")
        break

    else:
        print("invalid choice! please try again.")                    



   