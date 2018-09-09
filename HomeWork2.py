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
a = User('Pavel',"Ganjela",89017014147,"Her21","MAI")

class PhoneBook:
    list = []
    def add(self,user):
        self.list.append(user)
        self.list[0].printUser()


if __name__ == "__main__":
    pb = PhoneBook()
    pb.add(a)