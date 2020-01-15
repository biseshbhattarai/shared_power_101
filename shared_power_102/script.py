#! /usr/bin/python3

#PROJECT STATUS

'''
COMPLETED:
	1> Register
	2> Login
	3> Add

'''
from tkinter import *
import sqlite3
import sys
conn = sqlite3.connect('user.db')
c = conn.cursor()
FEATS = ['Register', 'Login', 'View&Search', 'View Cart', 'Add Tool', 'Logout']
global d
SESSION = []
ACTION = []
SYSTEM_ON = False
#DATABASE INITIALIZATION
#--------------------------------------------------------------------------------------
class LoginPage:

    def __init__(self):
        window = Tk()
        window.geometry('300x500')
        username_label = Label(window, text="Username : ")
        username_label.grid(row=0, column=0)
        username_entry = Entry(window)
        username_entry.grid(row=0, column=1)
        password_label = Label(window, text="Password : ")
        password_label.grid(row=1, column=0)
        password_entry = Entry(window)
        password_entry.grid(row=1, column=1)
        login_button = Button(text="Login", command=lambda : d.login(username_entry.get(), password_entry.get(), window))
        login_button.grid(sticky='nsew')
        gap = Label(window)
        gap.grid(pady=10)
        down_text = Label(window, text="Not registered yet ? ")
        down_text.grid(sticky='nsew')
        down_text_button = Button(text="Register", command=lambda : show_register_page(True, window))
        down_text_button.grid(sticky='nsew')
        window.mainloop()

class RegisterPage():

    def __init__(self):
        window = Tk()
        window.geometry('300x500')
        username_label = Label(window, text="Username : ")
        username_label.grid(row=0, column=0)
        username_entry = Entry(window)
        username_entry.grid(row=0, column=1)
        password_label = Label(window, text="Password : ")
        password_label.grid(row=1, column=0)
        password_entry = Entry(window, show='*')
        password_entry.grid(row=1, column=1)
        email_label = Label(window, text="Email : ")
        email_label.grid(row=2, column=0)
        email_entry = Entry(window)
        email_entry.grid(row=2, column=1)
        address_label = Label(window, text="Address : ")
        address_label.grid(row=3, column=0)
        address_entry = Entry(window)
        address_entry.grid(row=3, column=1)
        phoneno_label = Label(window, text="Phone-no : ")
        phoneno_label.grid(row=4, column=0)
        phoneno_entry = Entry(window)
        phoneno_entry.grid(row=4, column=1) 
        register_button = Button(text="Register", command=lambda : d.register(username_entry.get(), password_entry.get(), email_entry.get(), address_entry.get(), phoneno_entry.get(), window))
        register_button.grid(sticky='nsew')
        window.mainloop()

class AddToolPage():

    def __init__(self):
        window = Tk()
        window.geometry('300x500')
        tools_name_label = Label(window, text="Tool's name ")
        tools_name_label.grid(row=0, column=0)
        tools_name_entry = Entry(window)
        tools_name_entry.grid(row=0, column=1)
        description_label = Label(window, text="Description : ")
        description_label.grid(row=1, column=0)
        description_entry = Entry(window)
        description_entry.grid(row=1, column=1)
        half_day_rate_label = Label(window, text="Half day rate : ")
        half_day_rate_label.grid(row=2, column=0)
        half_day_rate_entry = Entry(window)
        half_day_rate_entry.grid(row=2, column=1)
        full_day_rate_label = Label(window, text="full day rate : ")
        full_day_rate_label.grid(row=3, column=0)
        full_day_rate_entry = Entry(window)
        full_day_rate_entry.grid(row=3, column=1)
       
        submit_button = Button(text="Submit", command=lambda : d.add_tool(tools_name_entry.get(), description_entry.get(), half_day_rate_entry.get(), full_day_rate_entry.get(),window))
        submit_button.grid(sticky='nsew')
        window.mainloop()

class DashBoard:

    def __init__(self):
        window = Tk()
        window.geometry("300x500")
        title_label = Label(window, text="Welcome "+ SESSION[0].upper()+ " to your dashboard")
        title_label.pack()
        gappp = Label(window)
        gappp.pack(pady=7)
        search_entry = Entry(window)
        search_entry.insert(0, 'Search here...')
        search_entry.pack()
        search_submit = Button(window, text="Submit", command=lambda : t.view_and_hire(search_entry.get(), window))
        search_submit.pack()
        s =  t.get_tools(SESSION[0])
        counter1 = 0
        counter2 = 1
        print(len(s))
        for i in s:
            # counter2 += 1
            # print(len(s))
           
            gap = Label(window, text="--------------------------------------")
            gap.pack(pady=10)
            for k in i:
                photo = Label(window, text="#TODO PHOTO GOES HERE")
                labels = Label(window, text=k)
                labels.pack()
                counter1 += 1
                counter2 += 1
                # print(counter1, counter2)
                
              

def login_page():
    a = LoginPage()

def show_register_page(p , window):
    if p == True:
        window.destroy()
    b = RegisterPage()
def show_dashboard():
    c = DashBoard()
def add_tool_page():
    a = AddToolPage()


class Db:
    def __init__(self):
     
        try: 
    
            c.execute("""CREATE TABLE users(
            username text,
            email text,
            password text,
            address text,
            phoneno integer

            )""")
        except:
            pass
        try:
            c.execute( """CREATE TABLE tools(
            tool_name text,
            half_day_rate integer,
            full_day_rate integer,
            description text,
            user_name text,
            FOREIGN KEY(user_name) REFERENCES users(username)
            )""")
        except Exception as e:
            print(e)
        try:
            c.execute(  """CREATE TABLE invoices(
                description text,
                quantity integer,
                price integer,
                total integer
            )""")
        except Exception as e:
            print(e)

    def get_one_user(self,username):
        c.execute("""SELECT * FROM users WHERE username=?""",(username,))
        a = c.fetchall()
        if len(a) == 0:
            return True

    def register(self,username,  password ,email, address , phoneno, controller):
   
        print(username, password ,email)
        if username != '' and password != '' and email != '' and address != '' and phoneno != 0:
            if self.get_one_user(username):
                command = """INSERT INTO users VALUES(? , ? , ? , ? ,? )"""
                c.execute(command, (username, email, password, address, phoneno))
                conn.commit()
                controller.destroy()
            else:
                print('User exists already with same name')
        else:
            print('All fields is necessary')

    def validate_user(self, username, password):
        c.execute("""SELECT * FROM users WHERE username=?""",(username,))
        s = c.fetchall()
        if len(s) != 0:
            if s[0][2] == password:
                return True

    def login(self, username, password, controller):
        if username != '' and password != '':
            if self.validate_user(username, password):
                SESSION.append(username)           
                print("logged in")
                print(SESSION)
                controller.destroy()
                show_dashboard()
                
            else:
                print("Incorrect password")
        else:
            print("All fields needed")

    def add_tool(self,tool_name, description , half_day_rate, full_day_rate, window):
        if tool_name != '' and description != '' and half_day_rate != '' and full_day_rate != '':
            command = """INSERT INTO tools VALUES(?,?,?,?,?)"""
            c.execute(command, (tool_name, description, half_day_rate, full_day_rate, SESSION[0]))
            conn.commit()
            print("Tools added")
            window.destroy()
            #GOTODASHBOARD
d = Db()

class Hire:

    def __init__(self, tool_name, s):
        window = Tk()
        window.geometry("300x500")
        # label = Label(window, text=tool_name)
        # label.grid(row=0, column=0)
        c.execute("""SELECT * FROM tools WHERE tool_name=?""", (tool_name,))
        a = c.fetchall()
        description_label = Label(window , text='Description : ')
        description_label.grid(row=0, column=0)
        half_day_rate_label = Label(window, text='Half day rate : ')
        half_day_rate_label.grid(row=1, column=0)
        full_day_rate_label = Label(window, text='Full day rate : ')
        full_day_rate_label.grid(row=2, column=0)
        owner_label = Label(window, text='Owner : ')
        owner_label.grid(row=3 , column=0)
        description = Label(window , text=a[0][1])
        description.grid(row=0, column=1)
        half_day_rate = Label(window, text=a[0][2])
        half_day_rate.grid(row=1, column=1)
        full_day_rate = Label(window, text=a[0][3])
        full_day_rate.grid(row=2, column=1)
        owner = Label(window, text=a[0][4])
        owner.grid(row=3 , column=1)
        window.mainloop()
        

def hireandviewPage(tool_name, window, s):
    window.destroy()
    h = Hire(tool_name, s)    

class Tools:

    def get_tools(self, username):
        c.execute("""SELECT * FROM tools WHERE user_name != ?""", (username,))
        return c.fetchall()

    def view_and_hire(self, tool_name, window):
        c.execute("""SELECT * FROM tools WHERE tool_name == ?""", (tool_name,))
        if len(c.fetchall()) != 0:
            hireandviewPage(tool_name, window, True)
        else:
            # hireandviewPage(tool_name , window, False)
            print("No such items")
    # def get_one_tool()
    
t = Tools()



#----------------------------------------------------------------------------------------------------------------
#GUI code ..

login_page()
