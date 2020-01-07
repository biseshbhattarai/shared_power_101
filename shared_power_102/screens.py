
#Implementing screen feature ... 
class HomeScreen:

    def __init__(self):

		self.feat = []
		

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


class ProfileScreen:
	pass

class AddToolScreen:
	pass

class CartScreen:
	pass

class ViewToolScreen:
	pass


