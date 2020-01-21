#! /usr/bin/python3

#PROJECT STATUS
from tkinter import *
import sqlite3
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
        window.geometry("1100x600+100+50")
        window.configure(bg="black")
        window.resizable(0, 0)
        # window.configure(background="black")
        background_image = PhotoImage('tool1.jpg')
        print(type(background_image))
        # Label(text="LOGIN", font=30,background="black", fg="skyblue").pack(pady=30)
        # background_label = Label(window, image=background_image)
        # background_label.place(x=0, y=0, relwidth=1, relheight=1)
        username_label = Label(window, font=("Arial", 25),text="Username : ", background="black", fg="green")
        username_label.pack()
        username_entry = Entry(window ,cursor='dot', bd=1, width=27, font=("Arial", 30))
        username_entry.pack()
        password_label = Label(window, font=("Arial", 25),text="Password : ", background="black", fg="green")
        password_label.pack()
        password_entry = Entry(window, cursor='dot', bd=1, width=27, font=("Arial", 30))
        password_entry.pack(pady=12)
        login_button = Button(text="Login", bg="green",font=("Arial",20),fg="black",command=lambda : d.login(username_entry.get(), password_entry.get(), window))
        login_button.pack(pady=10)
       
        down_text = Label(window, text="Not registered yet ? ", background="black", font=20)
        down_text.pack()
        down_text_button = Button(text="Register", font=("Arial", 20), bg="green",fg="black",command=lambda : show_register_page(True, window))
        down_text_button.pack()
        window.mainloop()

class RegisterPage():

    def __init__(self):
        window = Tk()
        window.configure(bg="black")
        window.geometry("1100x600+100+50")
        window.configure(bg="black")
        # window.resizable(0, 0)
        Label(text="REGISTER", font=30,background="black", fg="green").pack(pady=10)

        username_label = Label(window, text="Username : " , fg="green",background="black", font=("Arial", 30))
        username_label.pack()
        username_entry = Entry(window, cursor='dot', bd=1, width=27, font=("Arial", 30)) 
        username_entry.pack()
        password_label = Label(window, text="Password : " , background="black", fg="green",font=("Arial", 30))
        password_label.pack()
        password_entry = Entry(window, show='*', cursor='dot', bd=1, width=27, font=("Arial", 30))
        password_entry.pack()
        email_label = Label(window, text="Email : ", background="black",  fg="green",font=("Arial", 30))
        email_label.pack()
        email_entry = Entry(window, cursor='dot', bd=1, width=27, font=("Arial", 30))
        email_entry.pack()
        address_label = Label(window, text="Address : " ,fg="green" , background="black", font=("Arial", 30)) 
        address_label.pack()
        address_entry = Entry(window, cursor='dot', bd=1, width=27, font=("Arial", 30))
        address_entry.pack()
        phoneno_label = Label(window, text="Phone-no : ", fg="green",background="black", font=("Arial", 30))
        phoneno_label.pack()
        phoneno_entry = Entry(window, cursor='dot', bd=1, width=27, font=("Arial", 30))
        phoneno_entry.pack(pady=20) 
        register_button = Button(text="Register", font=("Arial", 20),bg="green", fg="black", command=lambda : d.register(username_entry.get(), password_entry.get(), email_entry.get(), address_entry.get(), phoneno_entry.get(), window))
        register_button.pack()
        back = Button(text="Back", bg="green", font=("Arial", 20),fg="black" ,command=lambda:back_login(window))
        back.pack()
        window.mainloop()

class AddToolPage():

    def __init__(self):
        window = Tk()
        window.geometry('300x500')
        tools_name_label = Label(window, font=("Arial", 25),text="Tool's name ")
        tools_name_label.grid(row=0, column=0)
        tools_name_entry = Entry(window, cursor='dot', bd=1, width=27, font=("Arial", 30))
        tools_name_entry.grid(row=0, column=1)
        description_label = Label(window, font=("Arial", 25),text="Description : ")
        description_label.grid(row=1, column=0)
        description_entry = Entry(window, cursor='dot', bd=1, width=27, font=("Arial", 30))
        description_entry.grid(row=1, column=1)
        half_day_rate_label = Label(window, font=("Arial", 25),text="Half day rate : ")
        half_day_rate_label.grid(row=2, column=0)
        half_day_rate_entry = Entry(window, cursor='dot', bd=1, width=27, font=("Arial", 30))
        half_day_rate_entry.grid(row=2, column=1)
        full_day_rate_label = Label(window, font=("Arial", 25),text="full day rate : ")
        full_day_rate_label.grid(row=3, column=0)
        full_day_rate_entry = Entry(window,cursor='dot', bd=1, width=27, font=("Arial", 30) )
        full_day_rate_entry.grid(row=3, column=1)
       
        submit_button = Button(text="Submit", font=("Arial", 25),command=lambda : d.add_tool(tools_name_entry.get(), description_entry.get(), half_day_rate_entry.get(), full_day_rate_entry.get(),window))
        submit_button.grid(row=6, column=5)
        window.mainloop()
           
def check(s):
    print(s)

class DashBoard:

    def __init__(self):
        window = Tk()
        self.hirings = []
        window.geometry("1100x600")
        window.configure(bg="black")
        # window.resizable(0, 0)
        self.searchEntry = Entry(window, cursor='dot', bd=1, width=27, font=("Arial", 30))
        self.searchEntry.place(x=280, y=80)
        self.searchButton = Button(window, text="Search", bg="green", padx=10, pady=11, command=lambda:t.view_and_hire(self.searchEntry.get(), window))
        self.searchButton.place(x=940, y=80)
        self.add_button = Button(window,text="Add Tool", bg="green" ,command=lambda: print('dfd'))
        self.add_button.place(x=500, y=170)
        self.viewbutton = Button(window, text="View Cart", bg="green",command=lambda: cart_page(window))
        self.viewbutton.place(x=400, y=170)
        self.viewbutton_ = Button(window, text="View Hired tools", bg="green",command=lambda: my_tools_page(window))
        self.viewbutton_.place(x=600, y=170)
        scrollbar = Scrollbar(window)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.listbox = Listbox(window, bd=0 ,yscrollcommand=scrollbar.set, bg="black",font=("Arial", 20), fg="white", highlightcolor = 'green',justify='center')
        self.listbox.bind('<<ListboxSelect>>', self.curSec)
        s =  t.get_tools(SESSION[0])

        for i in s:
            self.listbox.insert(END, i[0])
        self.listbox.place(x=450, y=300)
        Button(window, text="Hire", bg="green", fg="black", font=40, command=lambda:t.confirm_hire(self.hirings, window)).place(x=535, y=620)
        window.mainloop()

  
    def curSec(self, event):
        value = (self.listbox.get(self.listbox.curselection()))
        print(value)
        self.hirings.append((SESSION[0],value, datetime.datetime.now().strftime("%Y%m%d")))

class MyToolsPage:

    def __init__(self):
        window = Tk()
        self.returned = []
        window.configure(bg="black")
        window.geometry("500x600")
        c.execute("""SELECT * FROM hirings WHERE username=?""",(SESSION[0],))
        a = c.fetchall()
        Label(window, text="HIRED TOOLS" , font=("Arial", 30), bg="black", fg="green").pack(pady=20)
        scrollbar = Scrollbar(window)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.listbox = Listbox(window, bd=0 ,yscrollcommand=scrollbar.set, bg="black",font=("Arial", 20), fg="white", highlightcolor = 'green',justify='center')
        self.listbox.bind('<<ListboxSelect>>', self.curSec)
        self.listbox.configure(font=30, fg="green", bg="black")
        
        for i in a:
            self.listbox.insert(END, i[1])
        self.listbox.pack()
        Button(window, bg="green" , fg="black",font=('Arial',20),text="Return", command=lambda:t.return_tools(self.returned)).pack()
        back_button = Button(window, text="Back", bg="green",font=('Arial',20),fg="black",command=lambda:show_dashboard_(window))             
        back_button.pack()

    def curSec(self, event):
        value = self.listbox.get(self.listbox.curselection())
        self.returned.append(value)

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
            image text,
            FOREIGN KEY(user_name) REFERENCES users(username)
            )""")
        except Exception as e:
            print(e)
        try:
            c.execute( """CREATE TABLE invoices(
                username text,
                description text,
                quantity integer,
                price integer,
                total integer,
                delivery integer, 
                insurance integer
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
        window.configure(bg="black")
        window.geometry("1100x600+100+50")
        # label = Label(window, text=tool_name)
        # label.grid(row=0, column=0)
        c.execute("""SELECT * FROM tools WHERE tool_name=?""", (tool_name,))
        a = c.fetchall()
        description_label = Label(window , text='Description -> ', font=("Arial", 25),bg="black", )
        description_label.grid(row=3, column=0)
        half_day_rate_label = Label(window, text='Half day rate -> ', bg="black", font=("Arial", 25))
        half_day_rate_label.grid(row=4, column=0)
        full_day_rate_label = Label(window, text='Full day rate -> ', bg="black", font=("Arial", 25))
        full_day_rate_label.grid(row=5, column=0)
        owner_label = Label(window, text='Owner -> ', bg="black", font=("Arial", 25))
        owner_label.grid(row=6 , column=0)
        description = Label(window , text=a[0][1], bg="black", font=("Arial", 25))
        description.grid(row=3, column=1)
        half_day_rate = Label(window, text=a[0][2], bg="black", font=("Arial", 25))
        half_day_rate.grid(row=4, column=1)
        full_day_rate = Label(window, text=a[0][3], bg="black", font=("Arial", 25))
        full_day_rate.grid(row=5, column=1)
        owner = Label(window, text=a[0][4], bg="black", font=("Arial", 25))
        owner.grid(row=6 , column=1)
        add_to_cart_button = Button(window, bg="green",fg="black",font=('Arial', 40),text="Add to cart" , 
        command=lambda : t.add_to_cart(tool_name, SESSION[0], window))
        add_to_cart_button.grid(row=4, column=3)
        data = []
        data.append((SESSION[0], tool_name, datetime.datetime.now().strftime("%Y%m%d")))
        hire_button = Button(window, text="Hire", bg="green",fg="black",font=('Arial', 40),command=lambda: t.confirm_hire(data, window))
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
                c.execute("""DELETE FROM cart WHERE username=? and tool_name=?""", (SESSION[0],i[1]))
                conn.commit()
        else:
            print("{} is hired".format(cart_data))
            c.execute("""INSERT INTO hirings VALUES (?, ?, ? , ? , ?)""", (cart_data[0][0], cart_data[0][1], 
        datetime.datetime.now().strftime("%Y%m%d"), quantity, s))
            conn.commit()
        c.execute("""DELETE FROM cart WHERE username=? and tool_name=?""", (SESSION[0], cart_data[0][1]))
        conn.commit()
        msg.showinfo('showinfo ', 'Above item/s are hired')
        print("Cart data of {} is deleted".format(SESSION[0]))
        window.destroy()
        show_dashboard()

    def confirm_hire(self, data, window):
    
        window.destroy()
        window = Tk()
        window.configure(bg="black")
        window.geometry("500x600")
        quantity_label = Label(window, bg="black", fg="green" ,font=("Arial", 25),text="Quantity")
        quantity_label.pack(pady=7)
        quantity = Entry(window ,cursor='dot', bd=1, width=27, font=("Arial", 30) )
        quantity.insert(0, 1)
        quantity.pack(pady=15)
        delivery = IntVar()
        delivery_opt = Checkbutton(window, font=("Arial", 30),variable=delivery , text="Request for delivery")
        delivery_opt.pack()
        Button(window, text="Confirm" , command=lambda: t.hire_tools(data, quantity.get(),delivery, window)).pack()
        # t.hire_tools(data, quantity.get(), delivery_opt.get(), window)
     

    def view_invoice_page(self):
        c.execute("""SELECT * FROM invoice WHERE username=? """, (username, ))
        invoices = c.fetchall()
        print(invoices)   

    def return_tools(self, tools):
        hiringgg = []
        for i in tools:
            c.execute("""SELECT * FROM hirings WHERE tool_name=? and username=? """, (i, SESSION[0]))
            a = c.fetchall()
            print(a)
            c.execute("""SELECT * FROM tools WHERE tool_name=?""", (i))
            b = c.fetchall()
            print(b)
            half_day_rate = b[0][1]
            full_day_rate = b[0][2]
            hiringgg.append((i, full_day_rate, a[0][3], full_day_rate*a[0][3]))
        for i in hirings:
            c.execute("""INSERT INTO INVOICE VALUES (?, ? , ?, ?)""", (i[0], i[1], i[2], i[3]))
            conn.commit()
        # a = self.generate_invoice()
        view_invoice_page(a , window)
        



def get_cart_data():
    c.execute("""SELECT * FROM cart WHERE username=?""", (SESSION[0],))
    return c.fetchall()
t = Tools()


class CartPage:

    def __init__(self):
        window = Tk()
        window.configure(bg="black")
        window.geometry("500x600")
        cart_data = get_cart_data()
        for i in cart_data:
            label = Label(window, text="-->"+i[1], bg="black", fg="yellow" ,font=50)
            label.pack(pady=22)
        if len(cart_data) != 0:
            hire_button = Button(window, text="Hire" , bg="skyblue", fg="black", font=40,command=lambda : t.confirm_hire(cart_data, window))    
            hire_button.pack(pady=10)
        button = Button(window ,text="Back", bg="skyblue",fg="black",command=lambda: show_dashboard_(window))
        button.pack()

class Invoice:

    def __init__(self, data):
        window = Tk()
        window.config(bg="black")

        window.geometry("500x600")
        window.title('Invoice')
        Label(window, text="Description", font=("Arial", 20)).pack()
        Label(window, text="Hammer", font=("Arial", 20)).pack(pady=10)
        Label(window, text="Price", font=("Arial", 20)).pack()
        Label(window, text="400", font=("Arial", 20)).pack(pady=10)
        Label(window, text="Quantity", font=("Arial", 20)).pack()
        Label(window, text="1", font=("Arial", 20)).pack(pady=10)
        Label(window, text="Total", font=("Arial", 20)).pack()
        Label(window, text="400", font=("Arial", 20)).pack(pady=10)
        Label(window, text="Delivery", font=("Arial", 20)).pack()
        Label(window, text="0", font=("Arial", 20)).pack(pady=10)
        Label(window, text="Insurance", font=("Arial", 20)).pack()
        Label(window, text="5", font=("Arial", 20)).pack(pady=10)
        window.mainloop()

#CALLING TOOL INSTANCE

#cart page
def cart_page(window):
    window.destroy()
    c = CartPage()


#----------------------------------------------------------------------------------------------------------------
#GUI code ..

login_page()
