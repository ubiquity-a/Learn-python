#set is unordered collection of unique/remove duplicate items
'''
s = {1,2,3,4,2}
l = [1,2,3,2,4]
p=list(set(l))
print(p)

# add item in set
# s.add(6,5,7,9)  wrong method ...we can add one item at a time
s.add(6)
s.add(9)       
print(s)
#remove method
s.remove(3)
print(s)        # if you try to remove any item which does'nt exist in set then it will throw error


#copy method
s1 = s.copy()
print(s1)

# in set we can't store list  or dict or tuple
s2 = {1,2,3,'s', "akku"}
# s2 = {1,2,3,'s', "akku",[1,2,3]} throw error
print(s2)

#set math  like union, intersection
print(s1 | s2)    # union
print(s1 & s2)      #intersection
'''

# list comprehension minimize the code
#print square of numbers

'''
square = [i**2 for i in range(1,11)]
print(square)


#negative no
neg= []
for i in range(1,11):
    neg.append(-i)
print(neg)    

# do it in list comprehension
negative = [-i for i in range(1,11)]
print(negative)

# first letter of each string in list will store in list
names = ['akku','mahi','baby']
l = []
for i in names:
    l.append(i[0])
print(l)


#using list comprehension
list = [i[0] for i in names]
print(list)




#exercise
def rev(list):
    rev_list = []
    for i in list:
        rev_list.append(i[-1::-1])
    return rev_list


list = ["akamahi", 'bitti', 'siyaa']
print(rev(list))


#exercise
def make_str(list1):
    output = []
    for i in list1:
        if type(i)==int or type(i)== float:
           output.append(i)
    return output
list1 = [5,6,7,'akku',6.7,8.2, 4 ,"siya"]
print(make_str(list1))

#using comprehension
def stri(l):
    return [str(i) for i in l if (type(i) == int or type(i) == float) ]
l = [1,2,4,'kki','mahi',4.5]
print(stri(l))


 # exercise

def aasu(list3):
    even = []
    for i in list3:
        if i%2==0:
            even.append(i*2)
        else:
            even.append(-i)
    return even        
list3 = [1,2,5,8,3,2,9,14,13,18,45]
print(aasu(list3))

#using list comprehension
list3 = [1,2,5,8,3,2,9,14,13,18,45]
new = [i*2 if (i%2==0) else -i for i in list3 ]
print(new)

'''

#nested list create
'''
nested_list = [[i for i in range(1,4)] for j in range(1,5)]
print(nested_list)

#without comprehension method
new_list = []
for i in range(1,4):
    new_list.append([1,2,3])
print(new_list)    

'''

# dictionary comprehension
'''
square = {f"square of {num} is " : num**2 for num in range(1,5)}
print(square)

#count letter in string
name = "akanksha"
letter = { i:name.count(i) for i in name}
print(letter)

odd_even = {i: ('even' if i%2==0 else 'odd') for i in range(1,10)}
print(odd_even)
'''

#set comprehension
'''
s = { k**2 for k in range(1,6)}
print(s)

names = ['akku','mahi','siya']
unorder = {name[0] for name in names}
print(unorder)
'''


'''
# *args functions
#in args function we can pass any no o arguments
def total(*args):
    total = 1
    for i in args:
        total= total*i
    return total    
print(total(1,2,3,5))


# teo argument
def total(num, *args):              # args can contain nothing
    total = 1
    print(num)            #only 1
    print(args)       #(2,3,5) tuple
    for i in args:
        total= total*i
    return total    
print(total(1,2,3,5))


#args as argument
def total(*args):              # args can contain nothing
    total = 1
    print(args)            #only 1       #(2,3,5) tuple
    for i in args:
        total= total*i
    return total  
list = [1,2,3,5,6]  
print(total(*list))        # applying star in arguement it become unpack

#
def total(num, *args):              # args can contain nothing
    total = 1
    print(num)            # only 1
    print(args)           # (2,3,5) tuple
    if args:
        return [i**num for i in args]
    else:
        return "not pass args"   
num = [2,3,5] 
print(total(2, *num))


'''

# **kwargs    keyword args it always take arguemet as a dictionary
'''
def func(**kwargs):
    print(kwargs)
    print(type(kwargs))
func(name= 'akkubaby', age = 22)

# unpacking kwargs
def func(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for k,v in kwargs.items():
        print(f"{k}: {v}")
dict = {'name': 'akkubaby', 'age': 22}    
func(**dict)      #unpacking

def func(bf, **kwargs):
    print(bf,kwargs)
    print(type(kwargs))
    for k,v in kwargs.items():
        print(f"{k}: {v}")
dict = {'name': 'akkubaby', 'age': 22}    
func('no', **dict)      


#exercise
def capt(list):
    new_list = []
    for i in list:
        new_list.append(i.title())
    return new_list

list = ['akkubaby', 'siya', 'srishti']
print(capt(list))

'''


# lambda function  it is used to define function in one line
#anonymous fn  means no name
'''
add = lambda a,b : a*b
print(add(2,7))
print(add)
last =  lambda s : s[-1]
print(last('akku'))
  

  #using if else in lambda fn
ans = lambda s : len(s)>6
print(ans('mahiakkubaby'))



# Enumerate function is used with for loop to track position
def fun(s):
    for pos, name in enumerate(s):
        print(f"{pos}--- >{name}")
list = ["akanksha",'siya','srishti']
print(fun(list))
'''

#map fn   means call a function like this [fun(),fun(),fun()]
'''
numbers = [1,2,3]
square = list(map(lambda a:a**2, numbers))
print(square)

#list comp
man = [1,2,3]
list_new = [i**2 for i in man]
print(list_new)
'''


# filter function
'''

numbers = [1,3,7,8,9,10]
evens = tuple(filter(lambda a:a%2==0, numbers))
print(evens)

#list comprehension
even = [i for i in numbers if i%2==0 ]
print(even)


#itrator and iterables
numbers = [1,3,7,8,9,10]
squares = map(lambda a:a**2, numbers)
no = iter(numbers)
print(next(no))
print(next(no))
print(next(no))

'''
#zip function

'''
user = ["srishti", 'akanksha', 'siyaa']
age = [22,23,21]
print(list(zip(user,age)))


#also can
hey = [('srishti', 22), ('akanksha', 23), ('siyaa', 21)]
print(dict(hey))

#zip part 2
#print element [(1,2),(3,4)] in two diff list
l = [(1,2),(3,4),(9,7)]
l1, l2 = list(zip(*l))
print(l1)
print(l2)
'''
#exercise
new = []
l1 = [1,3,6]
l2 = [8,9,2]
for pair in zip(l1,l2):
    new.append(max(pair))
print(new)









