class chatbook:
    def __init__(self):
        # defining default attributes:
        self.username = ''
        self.password = ''
        self.loggedin = False

        #call 'main menu which was created later' under the constructor itself
        self.menu()
        
    # method: main menu    
    def menu(self):
        user_input = input("""welcome to chatbook. how do you want to proceed?
                           1. press 1 to signup
                           2. press 2 to signin
                           3. press 3 to write a post
                           4. press 4 to message a friend
                           5. press any other key to exit""")
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            exit()



#creating object 
#obj = chatbook()            

# Method - sign up
    def signup(self):
        email = input("enter your email here")
        pwd = input ("enter your password here")
        self.username = email
        self.password = pwd
        print("you have signed up successfully.")

    # print a new line
        print("\n")
        self.menu()

    # Method - sign in
    def signin(self):
        if self.username=='' and self.password=='':
            print("please signup first by pressing 1 in main menu")
        else:
            uname = input("enter your email here")
            pwd = input("enter your password here")
            if self.username==uname and self.password==pwd:
                print("you have signed in successfully.")
                self.loggedin = True
            else:
                print("please input correct credentials")
        print("\n")
        self.menu()


obj = chatbook() 