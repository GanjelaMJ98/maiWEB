# -*- coding: utf8 -*-
#5.1
int_a = 5
int_b = 2
float_a = 3.3
float_b = 6.2
bool_true = True
bool_false = False
n = None
str_a = "Hello"
str_b = "World"
list1 = []
list2 = list()
tuple_a = tuple()
tuple_b = 's',



''' + '''
print("int 5 + int 2 = ", int_a + int_b)
print("float 6.2 + float 3.3 = ", float_b + float_a)
print("bool True + bool False = ", bool_true + bool_false)
print("int 5 + float 6.2 = ", int_a + float_b)
print("float 6.2 + bool True = ", float_b + bool_true)
print("int 5 + bool False = ", int_a + bool_false)
''' - '''
print()
print("int 5 - int 2 = ", int_a - int_b)
print("float 6.2 - float 3.3 = ", float_b - float_a)
print("bool True - bool False = ", bool_true - bool_false)
print("int 5 - float 6.2 = ", int_a - float_b)
print("float 6.2 - bool True = ", float_b - bool_true)
print("int 5 - bool False = ", int_a - bool_false)
''' * '''
print()
print("int 5 * int 2 = ", int_a * int_b)
print("float 6.2 * float 3.3 = ", float_b * float_a)
print("bool True * bool False = ", bool_true * bool_false)
print("int 5 * float 6.2 = ", int_a * float_b)
print("float 6.2 * bool True = ", float_b * bool_true)
print("int 5 * bool False = ", int_a * bool_false)
''' / '''
print()
print("int 5 / int 2 = ", int_a / int_b)
print("float 6.2 / float 3.3 = ", float_b / float_a)
print("bool True / bool False = ZeroDivisionError ")
print("int 5 / float 6.2 = ", int_a / float_b)
print("float 6.2 / bool True = ", float_b / bool_true)
print("int 5 / bool True = ", int_a / bool_true)
''' 5.2 '''
print()
print("str Hello + str World = ", str_a + str_b)
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
print("str Hello * int 5 = ", str_a * int_a)
print("str Hello * float 3.3 = Error")
print("str Hello * bool False = ", str_a * bool_false)
print()
print("str Hello / str World = Error")
print("str Hello / int 5 = Error")
print("str Hello / float 3.3 = Error")
print("str Hello / bool False =Error")
''' 5.3 '''
list1.append(int_a);
list1.append(float_b);
list2.append(bool_true);
list2.append(str_a);
list2.append(list1);
list1.append(int_a);
list1.append(int_a);
print(list1)
print(list2)
print(list2[2][0])
list1.pop()
print(list1)
''' 5.4 '''
print("tuple + tuple",tuple_a+tuple_b)
#Все операции над списками, не изменяющие список (сложение, умножение на число, методы index() и count() и некоторые другие операции).
#Не знаю зачем я вообще это делаю






