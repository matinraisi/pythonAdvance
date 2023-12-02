# num  =int(input("....: "))
# def faunc(a=10):
#     return a + 10



# # (lambda x : x+10)()
# print((lambda x : x+10)(num))


# f1 = lambda a :  a *2
# # add = f1(3,5)
# # tmp = add +10
# print(f1(num))

# map()
# filter()


# list_ = [5,4,8,10,12,2]
# a = len(list_)
# print(a)
# add = []
# for i in list_:
#     add.append(i+2)
# print(add)



# def func(name):
#     return len(name)
# print(func(('ali' , 'matin','reza' , 'mmd')))


# x = map(func , ('ali' , 'matin','reza' , 'mmd'))


# def myfunc(a, b):
#   return a + b

# x = map(myfunc, ('apple', 'banana', 'cherry'), ( 'lemon', 'pineapple'))

# print(x)

# #convert the map into a list, for readability:
# print(list(x))

# list_ = [5,4,8,10,12,2]
# def func(a):
#     return a +2


# x = map(func , list_)

# print(list(x))


# print(list(map(lambda x : x+2, [1, 2, 3, 4])))


list_ = [1,2,3,5,4,8,10,12,2,-1,-10,-5,-8]

# def func(z):
#     if z<5:
#         return  False
#     else:
#         return True

# x=filter(func , list_)

# print(list(x))

print(list(filter(lambda z: False if z<5 else True , list_)))