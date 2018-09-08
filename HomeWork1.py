#5.1
a = 5
b = 2
c = 3.3
d = 6.2
t = True
f = False
n = None
s = "Hello"
w = "World"
list1 = []
list2 = list()

''' + '''
print("int 5 + int 2 = ",a+b)
print("float 6.2 + float 3.3 = ",d+c)
print("bool True + bool False = ",t+f)
print("int 5 + float 6.2 = ",a+d)
print("float 6.2 + bool True = ",d+t)
print("int 5 + bool False = ",a+f)
''' - '''
print()
print("int 5 - int 2 = ",a-b)
print("float 6.2 - float 3.3 = ",d-c)
print("bool True - bool False = ",t-f)
print("int 5 - float 6.2 = ",a-d)
print("float 6.2 - bool True = ",d-t)
print("int 5 - bool False = ",a-f)
''' * '''
print()
print("int 5 * int 2 = ",a*b)
print("float 6.2 * float 3.3 = ",d*c)
print("bool True * bool False = ",t*f)
print("int 5 * float 6.2 = ",a*d)
print("float 6.2 * bool True = ",d*t)
print("int 5 * bool False = ",a*f)
''' / '''
print()
print("int 5 / int 2 = ",a/b)
print("float 6.2 / float 3.3 = ",d/c)
print("bool True / bool False = ZeroDivisionError ")
print("int 5 / float 6.2 = ",a/d)
print("float 6.2 / bool True = ",d/t)
print("int 5 / bool True = ",a/t)
''' 5.2 '''
print()
print("str Hello + str World = ",s+w)
print("str Hello + int 5 = Error")
print("str Hello + float 3.3 = Error")
print("str Hello + bool False = Error")
print()
print("str Hello - str World = Error")
print("str Hello - int 5 = Error")
print("str Hello - float 3.3 = Error")
print("str Hello - bool False = Error")
print()
print("str Hello * str World = Error")
print("str Hello * int 5 = ",s*a)
print("str Hello * float 3.3 = Error")
print("str Hello * bool False = ",s*f)
print()
print("str Hello / str World = Error")
print("str Hello / int 5 = Error")
print("str Hello / float 3.3 = Error")
print("str Hello / bool False =Error")
''' 5.3 '''
list1.append(a);
list1.append(d);
list2.append(t);
list2.append(s);
list2.append(list1);
list1.append(a);
list1.append(a);
print(list1)
print(list2)
print(list2)







