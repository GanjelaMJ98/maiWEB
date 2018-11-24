import sqlite3
conn = sqlite3.connect('DB.db') #connect db

cursor = conn.cursor()

buf =list()
class Contact:
	name = str()
	number = str()
	adress = str()
	work = str()
	def __init__(self, name, number, adress, work):
		self.name = name
		self.number = number
		self.adress = adress
		self.work = work
	def print(self):
		print(self.name, self.number, self.adress, self.work)
	def Returner(self):
		a =[self.name, self.number, self.adress, self.work]
		return a

class Phonebook:
	l1 = list()
	l2 = list()

	def __init__(self):
		db = cursor.execute('SELECT * FROM main')

		for user in db:
			new_contact = Contact(name = user[1], number = user[2], adress = user[3],work = user[4])
			self.l2.append(new_contact)

	def addDB(self):
		delete = 'DELETE FROM main WHERE 1=1'
		cursor.execute(delete)
		for user in self.l2:
			
			sql = "INSERT INTO main VALUES(NULL, '{0}', '{1}', '{2}', '{3}')".format(user.name, user.number, user.adress, user.work)
			cursor.execute(sql)
		conn.commit()

	def Insert(self, contact):
		for user in self.l2:

			if user.Returner() == contact.Returner():
				print("DOUBLE CONTACT")
				return -1
		self.l2.append(contact)

	def PrintAll(self):
		for user in self.l2:
			user.print()

	def SearchbyName(self, name):
		result = list()
		for user in self.l2:
			if user.name == name:
				result.append(user)
		if result == []:
			print("NOT FOUND\n")
			return -1

		for user in result:
			user.print()
		return result

	def SearchbyNumber(self, number):
		result = list()
		for user in self.l2:
			if user.number == number:
				result.append(user)
		if result == []:
			print("NOT FOUND\n")
			return -1

		for user in result:
			user.print()
		return result

	def SearchbyAdress(self, adress):
		result = list()
		for user in self.l2:
			if user.adress == adress:
				result.append(user)
		if result == []:
			print("NOT FOUND\n")
			return -1

		for user in result:
			user.print()
		return result

	def SearchbyWork(self, work):
		result = list()
		for user in self.l2:
			if user.work == work:
				result.append(user)
		if result == []:
			print("NOT FOUND\n")
			return -1

		for user in result:
			user.print()
		return result

	def Delete(self, result):
		if result == -1:
			return -1
		while(1):
			j = 0
			i = 0
			for user in result: #KOSTYL
				j += 1 
			if j == 1:
				for user in self.l2:
					for user2 in result:
						if user == user2:
							del self.l2[i]
							print("DELETE")
							return 0
					i+=1		
			else:
				a = input("Choose number of contact do you want to delete?\n")
				i = 1
				for user in result:
					if i == int(a):
						i = 0
						for user2 in self.l2:
							if user2 == user:
								del self.l2[i]
								print("DELETE")
								return 0
							i+=1
					i+=1

	def DeleteByName(self, name):
		result = self.SearchbyName(name)
		self.Delete(result)

	def DeleteByNumber(self, name):
		result = self.SearchbyNumber(name)
		self.Delete(result)

	def DeleteByAdress(self, name):
		result = self.SearchbyAdress(name)
		self.Delete(result)

	def DeleteByWork(self, name):
		result = self.SearchbyWork(name)
		self.Delete(result)
		
	def RedactFind(self):
		while(1):
			result = []
			print("What contact do you want to change?")
			b = input("\nChoose parametr for finding contact\n1-for name\n2-for number\n3-for adress\n4-for-work\n")
			if b == '1':
				c = input("\nName: ")
				result = self.SearchbyName(c)
			elif b == '3':
				c = input("\nadress: ")
				result = self.SearchbyAdress(c)
			elif b == '2':
				c = input("\nNumber: ")
				result = self.SearchbyNumber(c)
			elif b == '4':
				c = input("\nWork: ")
				result = self.SearchbyWork(c)
			else:
				print("Error Input")
			if result == -1:
				return -1

			j = 0
			i = 1
			for user in result: #KOSTYL
				j += 1 
			if j == 1:
				return result
			else:
				a = input("Choose what contact do you want to change?\n")
				for user in result:
					if i == int(a):
						user.print()
						return user
					i+=1
			print("Error")
			return -1

	def Redact(self):
	
		result = self.RedactFind()
		if result==-1:
			return -1
		while(1):
			a = input("What you want to change\n1 - name\n2 - number\n3 - adress\n4 - work\n")
			name = input("Input new: ")
			if a == "1":
				result.name = name
			elif a == "2":
				result.number = name
			elif a == "3":
				result.adress = name
			elif a == "4":
				result.work = name
			else:
				print("Error Input")
				return -1
			a = input("Do you want this contact more?(y-yes)\n")
			if a == 'y':
				continue
			else:
				return 0

def Asker():
	a= input("name: ")
	b = input("\nnumber: ")
	c = input("\nadress: ")
	d = input("\nwork: ")
	spisok = [a, b, c, d]
	return spisok
def chooser(phonebook):
	cnt = True
	while(1):
		a = input("Choose, what you want\n1-for add new contact\n2-for find contact\n3-for delete contact\n4-for show all contact\n5-for redacting\nother-for quit\n")
		if a=='1':
			lis = Asker()
			ex = Contact(lis[0], lis[1], lis[2], lis[3])
			p.Insert(ex)
		elif a == '2':
			b = input("\nChoose parametr\n1-for name\n2-for adress\n3-for number\n4-for-work\n")
			if b == '1':
				c = input("\nName: ")
				phonebook.SearchbyName(c)
			elif b == '2':
				c = input("\nadress: ")
				phonebook.SearchbyAdress(c)
			elif b == '3':
				c = input("\nNumber: ")
				phonebook.SearchbyNumber(c)
			elif b == '4':
				c = input("\nWork: ")
				phonebook.SearchbyWork(c)
			else:
				print("Error Input")
				continue
		elif a == '3':
			b = input("Choose parametr\n1-for name\n2-for number\n3-for adress\n4-for-work\n")
			if b == '1':
				c = input("Name: ")
				print(phonebook.DeleteByName(c))
			elif b == '3':
				c = input("adress: ")
				print(phonebook.DeleteByAdress(c))
			elif b == '2':
				c = input("Number: ")
				print(phonebook.DeleteByNumber(c))
			elif b == '4':
				c = input("Work: ")
				print(phonebook.DeleteByWork(c))
			else:
				continue
		elif a == '4':
			phonebook.PrintAll()
		elif a == '5':
			phonebook.Redact()
		else:
			phonebook.addDB()

			break


if __name__ == "__main__":
	p = Phonebook()
	chooser(p)
conn.close()