# -*- coding: utf8 -*-

class User:
    def __init__(self, name , lastname, number, adress,work):
        self.name = name
        self.lastname = lastname
        self.number = number
        self.adress = adress
        self.work = work
    def printUser(self):
        print("User:",self.name+" "+self.lastname)
        print("Number",self.number)
        print()

a = User('Pavel',"Ganjela",89017014142,"Her21","MAI")
b = User('Artem', "Zvezdin",89345677328, "Zad42","MAI")


class PhoneBook:
    list = []
    def add(self,user):
        self.list.append(user)
    def printBook(self):
    	for user in self.list:
    		user.printUser()
    def correct(self,name,lastname):
    	for user in  self.list:
    		if user.name == name and user.lastname == lastname:
    			user.printUser()
    			field = str(input("Input field to correct: "))
    			newObject = input("New: ")
    			if field == "name":
    				user.name = newObject
    			elif field =='lastname':
    				user.lastname = newObject
    			elif field =='number':
    				user.number = newObject
    			elif field =='adress':
    				user.adress = newObject
    			print("Ok:")
    			user.printUser()
    			return
    	print("Not Found")


if __name__ == "__main__":
    pb = PhoneBook()
    pb.add(b)
    pb.add(a)
    pb.printBook()
    name = input("Name: ")
    lastname = input("Lastname: ")
    pb.correct(name,lastname)
    pb.printBook()

