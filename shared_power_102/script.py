#! /usr/bin/python3

#PROJECT STATUS

'''
COMPLETED:
	1> Register
	2> Login
	3> Add

'''

import sqlite3

conn = sqlite3.connect('user.db')
c = conn.cursor()

SESSION = []
ACTION = []

#DATABASE INITIALIZATION
#--------------------------------------------------------------------------------------
try:
	J
	c.execute("""CREATE TABLE users(
			username text,
			email text,
			password text,
			address text,
			phoneno integer
			)""")
	c.execute("""CREATE TABLE tools(
			tool_name text,
			half_day_rate integer,
			full_day_rate integer,
			description text
			)""")
	c.execute("""CREATE TABLE invoices(
				description text,
				quantity integer,
				price integer,
				total integer
			)""")
except Exception as e:
	print(e)
	
#-------------------------------------------------------------------------------------------------
#DATABASE COMMANDS
def register(username, email, password, address , phoneno):
	c.execute("INSERT INTO users VALUES(?,?,?,?,?)",(username, email, password, address, phoneno))
	conn.commit()


def check_user(username):
	c.execute("SELECT * FROM users WHERE username = ?", (username,))
	print(c.fetchall())
	if len(c.fetchall()) == 0:
		return True 

def validate_login(username, password):
	c.execute("SELECT * FROM users WHERE username=? and password=?", (username, password))
	if bool((c.fetchall())):
		return True

def add_tool(tool_name, half_day_rate, full_day_rate, description):
	c.execute("INSERT INTO tools VALUES(?, ?, ?, ?)",(tool_name, half_day_rate, full_day_rate, description))
	conn.commit()

def get_tool(tool_name, description):
	c.execute("SELECT * FROM tools WHERE tool_name=?", (tool_name,))
	if len(c.fetchall()) != 0:
		print(c.fetchall())
	else:
		print("No tools available")
def add_in_session(user):
	SESSION.append(user)

def check_session_status(username):
	if len(SESSION) == 1 and SESSION[0] == username:
		return True





#------------------------------------------------------------------
#Code for validating proper and strong password

def check_alphanumeric_count(a):
    chars = ['@', '$', '%', '#', '&', '"', '!', '*', '^', "'"]
    s = []
    for i in a:
        for j in chars:
            if i == j:
                s.append(True)
    if len(s) >= 2:
        return True
    else:
        return False


def check_num_count(a):
    num = [(i+1) for i in range(10)] # [1, 2 , 3, 4, 5 ,6, 7, 8, 9, 10]
    s = []
    for i in a:
        for n in num:
            if i == str(n):
                s.append(True)
    if len(s) >= 2:
        return True
    else:
        return False        


def check_password_strength(password):
    if len(password) >= 7:
        if check_alphanumeric_count(password) and check_num_count(password):
            return True
        else:
            print("Password error : More alphanumeric or num req")
            return False
    else:
        print("Password error : Too less characters : MIN required")
        return False
#---------------------------------------------------------------
class Registration:
	def __init__(self):
		self.username = ''
		self.password = ''
		self.email = ''
		self.address = ''
		self.phoneno = 0

	def check_login(self, username='', password='', email='', address='', phoneno=0):
		if username and password:
			return True
	
	
	def login(self):
		print("\n-----------------\nLOGIN\n-----------------")
		self.username = input("Username : ")
		self.password = input("Password : ")
		if self.check_login(self.username, self.password):
			if validate_login(self.username, self.password):
				SESSION.append(self.username)
				return True
			else:
				print("Wrong credentials")
		else:
			self.register()

	def logout(self):
		SESSION.pop()
				 
	def check_register(self, username='', password='', email='', address='', phoneno=0):
		if username and password and len(password) >=7 and address and phoneno and type(phoneno) == type(1):
			return True

	def register(self):
		
		
		print("\n-----------------\nREGISTER\n-----------------")
		self.username = input("Username : ")
		self.password = input("Password : ")
		self.address = input("Address : ")
		self.email = input("Email : ")
		self.phoneno = int(input("Phoneno : "))
		if self.check_register(self.username, self.password , self.email, self.address, self.phoneno):
			if check_user(self.username):
				if check_password_strength(self.password):
					register(self.username, self.email, self.password , self.address, self.phoneno)	
					print("User registered")
				
			else:
				print("User with same name already exists.")
		else:
			print("Error")

#-----------------------------------------------------------------------------------------------------

		

class Tools(Registration):

	def __init__(self):
		super().__init__()
		self.tool_name = ''
		self.description = ''
		self.half_day_rate = 0
		self.full_day_rate = 0 

	def get_tool_name(self):
		self.tool_name = input("Enter tool name")

	def search_tool(self):
		if check_session_status(self.username):
			self.get_tool_name()
			if self.get_tool_name is not None:
				get_tool(self.tool_name)
			else:
				print("Please enter tool name")

	def set_tool_data(self):
		self.tool_name = input("Enter tool name")
		self.description = input("Enter tool description")
		self.full_day_rate = int(input("Enter full day rate"))
		self.half_day_rate = int(input("Enter half day rate"))

	def add_tool(self, tool_name, half_day_rate, full_day_rate, description):
		if check_session_status(self.username):
			self.set_tool_data()
			try:
				add_tool(self.tool_name, self.half_day_rate, self.full_day_rate, self.description)
			except Exception:
				print(Exception)

#---------------------------------------------------------------------------------------------------------------
class Invoice(Tools):

	def __init__(self , invoice_no):
		super().__init__()
		self.__invoice_no = invoice_no
		self.description = ''
		self.quantity = 0
		self.price = 0
		self.total = 0

	def generate_invoice(self):
		pass


#----------------------------------------------------------------------------------------------------------------


class HomePage:

	def __init__(self):
		self.feat = []
		self.action = ''
		self.username = ''
		self.password = ''
		self.email = ''
		self.address = ''
		self.phoneno = 0

	def show(self):
		return "Welcome to shared power\n\n\n\n -----------------------------\n"

	def options(self):
		self.feat = ['Register', 'Login']
		j = 0
		while j<= 1:
			print("{} : ({})".format(self.feat[j], j))
			j += 1


	def getAction(self, selected=False):
		s = input("Please enter the action : ")
		ACTION.append(s)
		while not bool(ACTION):
			print("Please give the action index..")
			s= input("Please enter the action : ")
		print(ACTION)

class Index(Tools):

	def __init__(self):
		super().__init__()
		self.feats = ['Add Tool', 'View & search tool', 'View Cart', 'Logout']


	def show(self):
		j = 2
		print("\n\n--------------------------------------Welcome ! {} , to shared power------------------------------------------------------------".format(SESSION[0]))

		for i in self.feats:
			print("\n\n{} : ({})".format(i, j))
			j += 1
class Distributer(Index , HomePage, Registration, Tools):

	def __init__(self):
		super().__init__()
		pass
	
	def distribute(self):
		if ACTION[0] == '1':
			if self.login():
				self.show()
				ACTION.pop()
				self.getAction()
				if len(ACTION) == 1:
					self.distribute()

		elif ACTION[0] == '0':
			self.register()
		elif ACTION[0] == '2':
			print(SESSION)
		elif ACTION[0] == '3':
			self.tool
		elif ACTION[0] == '4':
			print(SESSION)
		elif ACTION[0] == '5':
			print(SESSION)

class Delivery(Tools, Invoice, Registration):

	def __init__(self):
		super().__init__()
		self.total_deliveries = 6
		self.available = 6
		if self.out_of_valley:
			self.delivery_open = True
		self.delivery_open = False
		
	def delivery(self):
		if self.delivery_open and bool(self.available):
			self.available -= 1
	
	def update_invoice():
		pass

class Insurance(Tools, Registration):

	def __init__(self):
		super().__init__()
		pass

i = HomePage()
print(i.show())
i.options()
i.getAction()
d = Distributer()
d.distribute()
