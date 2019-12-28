!/usr/bin/python3



class Intro:

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
		self.feat = ['Register', 'Login', 'Search', 'Add', 'Hire']
		j = 0
		while j<= 2:
			print("{} : ({})".format(self.feat[j], j))
			j += 1


	def getAction(self, selected=False):
		self.action = input("Please enter the action : ")
		while not self.action:
			print("Please give the action index..")
			self.action = input("Please enter the action : ")

	def check_login(self, username='', password='', email='', address='', phoneno=0):
		if username and password:
			return True
	def check_register(self, username='', password='', email='', address='', phoneno=0):
		if username and password and len(password) >=7 and address and phoneno and type(phoneno) == type(1):
			return True
		

	def login(self):
		print("\n-----------------\nLOGIN\n-----------------")
		self.username = input("Username : ")
		self.password = input("Password : ")
		if self.check_login(self.username, self.password):
			print("You are logged in ")
		else:
			self.register()
	def register(self):
		print("\n-----------------\nREGISTER\n-----------------")
		self.username = input("Username : ")
		self.password = input("Password : ")
		self.address = input("Address : ")
		self.email = input("Email : ")
		self.phoneno = int(input("Phoneno : "))
		if self.check_register(self.username, self.password , self.email, self.address, self.phoneno):
			print("You are registered")
			self.login()
	def distributer(self):
		if self.action == '1':
			self.login()
		elif self.action == '0':
			self.register()

			

i = Intro()
print(i.show())
i.options()
i.getAction()
i.distributer()


class Cta:

	def __init__(self, username):
		self.username = username


	



l = Learn('masuhii')
print(l.getnmae())