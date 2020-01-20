#! /usr/bin/python3

#PROJECT STATUS
from tkinter import *
import sqlite3
import sys
from tkinter import messagebox as msg
import datetime
conn = sqlite3.connect('user.db')
c = conn.cursor()
SESSION = []

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
        register_button.grid(row=6 , column=2)
        back = Button(text="Back", command=lambda:back_login(window))
        back.grid(row=8, column=2)
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
           
def check(s):
    print(s)
class DashBoard:

    def __init__(self):
        window = Tk()
        scrollbar = Scrollbar(window)
        scrollbar.pack(side=RIGHT, fill=Y)
        scrollbar.pack(side=RIGHT, fill=Y)
        listbox = Listbox(window, yscrollcommand=scrollbar.set)
        window.geometry("300x500")
        title_label = Label(window, text="Welcome "+ SESSION[0].upper()+ " to your dashboard")
        title_label.pack()
        gappp = Label(window)
        gappp.pack(pady=7)
        cart_button = Button(window, text="View cart" , command=lambda:cart_page(window))
        cart_button.pack()
        my_tools = Button(window, text="My Tools", command=lambda:my_tools_page(window))
        my_tools.pack()
        search_entry = Entry(window)
        search_entry.insert(0, 'Search here...')
        search_entry.pack()
        search_submit = Button(window, text="Submit", command=lambda : t.view_and_hire(search_entry.get(), window))
        search_submit.pack(pady=15)
        Label(window, text="AVAILABLE TOOLS").pack(pady=12)

        s =  t.get_tools(SESSION[0])
       
        print(len(s))

        for i in s:
           listbox.insert(END, i[0])
        listbox.pack(side=LEFT, fill=BOTH)
        scrollbar.config(command=listbox.yview)
        window.mainloop()

                
class MyToolsPage:

    def __init__(self):
        window = Tk()
        window.geometry("300x500")
        c.execute("""SELECT * FROM hirings WHERE username=?""",(SESSION[0],))
        a = c.fetchall()
        for i in a:
            label = Label(window, text=i)
            label.pack()
        back_button = Button(window, text="Back", command=lambda:show_dashboard_(window))             
        back_button.pack()
def my_tools_page(window):
    window.destroy()
    m = MyToolsPage()

def login_page():
    a = LoginPage()
def back_login(window):
    window.destroy()
    a = LoginPage()

def show_register_page(p , window):
    if p == True:
        window.destroy()
    b = RegisterPage()
def show_dashboard():
    c = DashBoard()
def add_tool_page():
    a = AddToolPage()
def show_dashboard_(window):
    window.destroy()
    c = DashBoard()



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
            c.execute( """CREATE TABLE invoices(
                description text,
                quantity integer,
                price integer,
                total integer
            )""")
        except Exception:
            pass
        try:
            c.execute("""
                CREATE TABLE cart(
                    username text, 
                    tool_name text,
                    FOREIGN KEY (username) REFERENCES users(username)
                    FOREIGN KEY (tool_name) REFERENCES tools(tool_name)
                    )
            """)
        except Exception as e:
            print(e)
        try:
            c.execute("""
                    CREATE TABLE hirings(
                        username text,
                        tool_name text,
                        hired_date timestamp,
                        quantity integer,
                        delivery text,
                        FOREIGN KEY(username) REFERENCES users(username),
                        FOREIGN KEY (tool_name) REFERENCES tools(tool_name)
                        
                    )
            
            """)
        except :
            pass
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
                login_page()
            else:
                msg.showerror('Error', 'Username with same name already exists')
        else:
            msg.showerror('Error', 'Please fill all the fields')

    def validate_user(self, username, password):
        c.execute("""SELECT * FROM users WHERE username=?""",(username,))
        s = c.fetchall()
        if len(s) != 0:
            if len(s) != 0:
                if s[0][2] == password:
                    return True
        msg.showerror('Error', 'User doesnt exist')

    def login(self, username, password, controller):
        if username != '' and password != '':
            if self.validate_user(username, password):
                SESSION.append(username)           
                print("logged in")
                print(SESSION)
                controller.destroy()
                show_dashboard()
                
            else:
                msg.showerror('Error', 'Wrong password')
        else:
            msg.showerror('Error', 'All fields are necessary')

    def add_tool(self,tool_name, description , half_day_rate, full_day_rate, window):
        if tool_name != '' and description != '' and half_day_rate != '' and full_day_rate != '':
            command = """INSERT INTO tools VALUES(?,?,?,?,?)"""
            c.execute(command, (tool_name, description, half_day_rate, full_day_rate, SESSION[0]))
            conn.commit()
            msg.showinfo('Success', 'Tool is added')
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
        add_to_cart_button = Button(window, text="Add to cart" , 
        command=lambda : t.add_to_cart(tool_name, SESSION[0], window))
        add_to_cart_button.grid(row=4, column=3)
        data = []
        data.append((SESSION[0], tool_name, datetime.datetime.now().strftime("%Y%m%d")))
        hire_button = Button(window, text="Hire", command=lambda: t.confirm_hire(data, window))
        hire_button.grid(row=5, column=3)
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
            msg.showerror('Error', 'No such items found')
            # print("No such items")
    # def get_one_tool()
    
    def add_to_cart(self , tool_name, username, window):
        c.execute("""INSERT INTO cart VALUES(? , ? )""", (username , tool_name))
        conn.commit()
        msg.showinfo('Success', tool_name + ' is added on cart')
        window.destroy()
        show_dashboard()

    #HERE WE"LL UPDATE THE INVOICE 
    def hire_tools(self, cart_data, quantity,delivery,window):
        print(cart_data)
        if delivery == 1:
            s = 'True'
        else:
            s = 'False'
        if len(cart_data) > 1:
            for i in cart_data:
                print("{} are hired".format(i[1]))
                c.execute("""INSERT INTO hirings VALUES(?, ?, ?, ? , ?)""", (i[0], i[1], 
                datetime.datetime.now().strftime("%Y%m%d"), quantity , s))
                conn.commit()
        else:
            print("{} is hired".format(cart_data))
            c.execute("""INSERT INTO hirings VALUES (?, ?, ? , ? , ?)""", (cart_data[0][0], cart_data[0][1], 
        datetime.datetime.now().strftime("%Y%m%d"), quantity, s))
            conn.commit()
        c.execute("""DELETE FROM cart WHERE username=?""", (SESSION[0], ))
        conn.commit()
        msg.showinfo('showinfo ', 'Above item/s are hired')
        print("Cart data of {} is deleted".format(SESSION[0]))
        window.destroy()
        show_dashboard()

    def confirm_hire(self, data, window):
        window.destroy()
        window = Tk()
        window.geometry("300x500")
        quantity_label = Label(window, text="Quantity")
        quantity_label.pack()
        quantity = Entry(window)
        quantity.insert(0, 1)
        quantity.pack()
        delivery = IntVar()
        delivery_opt = Checkbutton(window, variable=delivery , text="Request for delivery")
        delivery_opt.pack()
        Button(window, text="Confirm" , command=lambda: t.hire_tools(data, quantity.get(),delivery, window)).pack()
        # t.hire_tools(data, quantity.get(), delivery_opt.get(), window)

    def generate_invoice(self):
        c.execute("""SELECT * FROM hirings WHERE username=?""", (SESSION[0]))
        a = c.fetchall()
        today_date = datetime.datetime.now().strftime("%Y%m%d")
        late = []
        for i in a:
            if (today_date - i[2]) > 3:
                late.append(True)
            
        total_fine = len(late) * 50
        ext = 0
        s = []
        for i in a:
            if i[4] == 'True':
                ext = 50
            s.append(i[1]+"\t"+i[2]+"\t"+i[3]+"\t"+total_fine+"\t"+ext)
        return s

    def return_tools(self):
        a = self.generate_invoice()
        view_invoice_page(a , window)



def get_cart_data():
    c.execute("""SELECT * FROM cart WHERE username=?""", (SESSION[0],))
    return c.fetchall()
t = Tools()


class CartPage:

    def __init__(self):
        window = Tk()
        window.geometry("300x500")
        cart_data = get_cart_data()
        for i in cart_data:
            label = Label(window, text=i[1])
            label.pack()
        if len(cart_data) != 0:
            hire_button = Button(window, text="Hire" , command=lambda : t.confirm_hire(cart_data, window))    
            hire_button.pack()
        button = Button(window ,text="Back", command=lambda: show_dashboard_(window))
        button.pack()

class Invoice:

    def __init__(self, data):
        window = Tk()
        window.geometry("300x500")



#CALLING TOOL INSTANCE

#cart page
def cart_page(window):
    window.destroy()
    c = CartPage()


#----------------------------------------------------------------------------------------------------------------
#GUI code ..

login_page()
