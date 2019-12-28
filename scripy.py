'''
CURRENT STATUS:
	-> USER CAN BE REGISTERED IN THE DATABASE
	-> USER CAN LOGIN IF REGISTERED
	-> USER CAN ADD TOOLS IN THE DATABASE
	-> SESSION IS USED HENCE USER CAN LOG IN AND OUT 

TODOS:
	-> SHARING AMONG USERS , CART SYSTEM TO BE IMPLEMENTED
	-> RATE AND PAYMENT SYSTEM
	-> MORE BETTER CODE AND PROPER SCENARIOS TEST

'''
from peewee import *
#peewee is ORM (Object relation mapping) tool that helps us to easily integrate with sqllite without writing length queries
#NOTE : THIS IS JUST A PROTOTYPE  HENCE ORM WILL BE REPLACED WITH NORMAL QUERIES 

db = SqliteDatabase('user.db')
#Initiate database
SESSION = []
#User gets added in this list when logged in 


class ProgramIntro:
	def __init__(self):
		self.line = '----------------------------------------------------------------'
		self.name = '                             Shared power                     '
		self.info = 'Please login (1) or register (2)'

	def show(self):
		print(self.line)
		print(self.name)
		print(self.info)

	def register(self):
		option = int(input("Enter here : "))
		if option == 1:
			return True
		elif option == 2:
			return False
		else:
			print("No option")


class KYC:
	def set_name(self):
		self.name = input("Please enter your name : ")
		return self.name
	def set_email(self):
		self.email = input("Please enter your email : ")
		return self.email
	def set_password(self):
		self.password = input("Please enter your password : ")
		return self.password


#AS in ORM we can create model or blueprint of our database which helps us better to intregrate with sqllite

class Users(Model):
	username = 'bisesh'
	email = CharField()
	password = CharField()

	class Meta:
		database = db

class Tools(Model):
	owner = ForeignKeyField(Users, backref="tols")
	name = CharField()

	class Meta:
		database = db


class Register(Users):
	def __init__(self, username_, email_, password_):
		super().__init__()
		db.connect()
		db.create_tables([Users])
		self.username_ = username_
		self.email_ = email_
		self.password_ = password_
		
	def reg(self):
		a = Users.create(username=self.username_, email=self.email_, password=self.password_)
		print(a)

		
class Session(Users):

	def __init__(self, username='', password=''):
		self.username = username
		self.password = password

	def login(self):
		a = Users.get(Users.name == self.username)
		if a:
			if a.password == self.password:
				SESSION.append(self.username)


	def logout(self):
		SESSION.pop()

def check_session(username):

	if len(SESSION) == 1 and SESSION[0] == username:
		return True
	

class AddTool(Tools, Users):

	def __init__(self):
		db.create_tables([Tools])


	def add(self):
		if check_session(self.username):
			tool_name = input("Enter the name of the tool")
			ow = Users.select().where(Users.username == SESSION[0]).get()
			t = Tools.create(owner=ow , name=tool_name)
			print(t)
		else:
			print("Please login")



p = ProgramIntro()
p.show()
k = KYC()

if not p.register():
	name = k.set_name()
	email = k.set_email()
	password = k.set_password()
	r = Register(name, email, password)
	r.reg()
	print("User registered")
elif  p.register():
	name = k.set_name()
	password = k.set_password()
	s = Session(name,password)
	s.login()
	print(SESSION)

log = input()
if log == 'logout':
	s = Session()
	s.logout()
elif log == 'add':
	a = AddTool()
	a.add()