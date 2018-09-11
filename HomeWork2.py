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
c = User('Vlad', "Baranov",89017014142, "Zad42","MAI")


class PhoneBook:
    list = []
    def add(self,user = None):
        if user == None:
            print()
            print("New user:")
            print()
            new_name = input("Name: ")
            new_lastname = input("Lastname: ")
            new_number = input("Number: ")
            new_adress = input("Adress: ")
            new_work = input("Work: ")
            new_User =User(new_name,new_lastname,new_number,new_adress,new_work)
            self.list.append(new_User)
        else:
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
                if field == "Name":
                    user.name = newObject
                elif field =='Lastname':
                    user.lastname = newObject
                elif field =='Number':
                    user.number = newObject
                elif field =='Adress':
                    user.adress = newObject
                else:
                    print("This field not found")
                    return
                print("Ok:")
                user.printUser()
                return
        print("Not Found")
    def rm(self,name,lastname):
        for user in  self.list:
            if user.name == name and user.lastname == lastname:
                self.list.remove(user)
    def search(self,name=None,lastname = None, number = None,adress = None, work = None):
        #TODO: else print(Notfound)
        if name is not None and lastname is not None:
            for user in self.list:
                if user.name == name and user.lastname == lastname:
                    user.printUser()
        elif number is not None:
            for user in self.list:
                if user.number == number:
                    user.printUser()
        elif work is not None:
            for user in self.list:
                if user.work == work:
                    user.printUser()
        elif adress is not None:
            for user in self.list:
                if user.adress == adress:
                    user.printUser()

def Interface():
    pb = PhoneBook()
    pb.add(c)
    pb.add(b)
    while(1):
        act = int(input("""Select an action
                1. Print PhoneBook
                2. Add new Contact
                3. Correct Contact
                4. Remove Contact
                5. Find contact
                6. Exit"""))
        if act == 1:
            pb.printBook()
        elif act == 2:
            pb.add()
        elif act == 3:
            print()
            cor_name = input("Input Name to Correction: ")
            cor_lastname = input("Input Lastname to Correction: ")
            pb.correct(cor_name,cor_lastname)
        elif act == 4:
            print()
            rm_name = input("Input Name to delete: ")
            rm_lastname = input("Input Lastname to delete: ")
            pb.rm(rm_name, rm_lastname)
        elif act == 5:
            a = int(input("""Search by ...
                            1. name & lastname
                            2. number
                            3. work
                            4. adress
                        """))
            if a == 1:
                s_name = input("Name: ")
                s_lastname = input("Lastname: ")
                pb.search(name= s_name, lastname=s_lastname)
            if a == 2:
                s_number = input("Number: ")
                pb.search(number=s_number)
            if a == 3:
                s_work = input("Work: ")
                pb.search(number=s_work)
            if a == 4:
                s_adress = input("Adress: ")
                pb.search(number=s_adress)
        elif act == 6:
            return

if __name__ == "__main__":
    Interface()
    #pb = PhoneBook()
    #pb.add(c)
    #pb.add(b)
    #pb.add(a)

    #pb.printBook()
    #name = input("Name: ")
    #pb.search(number=89017014142)

    #pb.rm(name ="Pavel", lastname="Ganjela")
    #pb.add(user = None)
    #lastname = input("Lastname: ")
    #pb.correct(name,lastname)
   # pb.printBook()
#TODO fix correct
#TODO fix search
