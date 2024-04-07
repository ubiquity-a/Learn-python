# args and *krgs
'''
def avg(*args):
    avg = []
    for pair in zip(*args):
        avg.append(sum(pair)/len(pair))    
            
    return avg
print(avg([1,2,3],[4,5,6],[7,8,9])) 


#lis comprehension
avrage = lambda *args: [[sum(pair)/len(pair)] for pair in zip(*args)]
print(avrage)
#how to input list
'''

'''
list = []
n = int(input("enter no of elements "))
for i in range(1, n+1):
    ele = int(input())
    list.append(ele)
print(list)    


#any and all fn 
#any fn return true if any case is true and vice versa
#all fn return return true if all case are true . If any case is false then it will return false
n1 = [1,7,3,9,5]
n2 = [6,8,9,7,2]

print(all([i%2!=0 for i in n1]))
print(any([i%2==0 for i in n2]))
'''

#min max fn  for complex data structure
'''
l = ['akanksha', 'radhe','siyaa','yaduvanshi']
print(max(l, key = lambda i: len(i)))
list = {
     'baby' : {'name': 'akku', 'age': 22},
     'bubu' : {'name': 'pakkuku', 'age': 32},
     'subu' : {'name': 'chaakkuku', 'age': 12}
}

#print(max(list, key = lambda i:i.get('age')))
#another method
print(max(list, key = lambda item : list[item]['age']))



#sorted fn
guitars = [
    {'name': 'akku', 'price': 2222},
    {'name': 'pakkuku', 'price': 1232},
    {'name': 'chaakkuku', 'price': 4112}

]

print(sorted(guitars, key = lambda d : d['price']))


# to print reverse descending order
print(sorted(guitars, key = lambda d : d['price'], reverse = True))
'''


#doc string help to understand the code 
#doc string write inclosed in  ''' or """
'''
def plus(a,b):
   
    return a+b
print(sum.__doc__)
print(len.__doc__)
print(sum.__doc__)
print(help.__doc__)


# Decorators
# closures firstly learn about it
def plus(a,b):
    return a+b
p = plus
print(plus.__name__)
print(p.__name__)


#how to pass fn as a arguement
l = [1,5,7,8]
def my_map(func, l):
    new_list = []
    for item in l:
        new_list.append(func(item))
    return new_list
print(my_map(lambda a : a**2, l))   



# function return fn also known as closure
def outer_func():
    def inner_func():
        print("hey there")
    return inner_func    
var = outer_func()
#try without var()
var()


#decorators - enhance the functionality of other fn
def decorator_fn(any_fn):
    def wrapper_fn():
        print("hey baby!!")
        any_fn()
    return wrapper_fn

# @ is called syntatic sugar
@decorator_fn   # short cut 
def func1():
    print("hii srishti!!")
func1()
#var = decorator_fn(func1)    these both is used when shortcut is not applied
#var()


# part 2


def decorator_fn(any_fn):
    def wrapper_fn(*args, **kwargs):
        print("hey baby!!")
        return any_fn(*args, **kwargs)
    return wrapper_fn

# @ is called syntatic sugar
@decorator_fn   # short cut 
def func1(a,b):
    return a+b
print(func1(3,5))
'''

# part3  doc string
'''
from functools import wraps            #module
def print_sum(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f"you are besharam {function.__name__}")
        return function(*args, **kwargs)
    return wrapper

 
    

@print_sum
def func(a,b):
    # hello there
    return a+b
 
print(func(5,9))
'''


# how to calculate time taken to run code
'''
import time

t1 = time.time()              # time taken in start
 

print('this is line one')
x = 5
if x == 5:
    print('x is equal to 5')
print('this is line 2')
t2 = time.time()
print(t2-t1)


# decorator exercise
from functools import wraps
import time

def calculate_time(func1):
    @wraps(func1)
    def wrapper_fn(*args,  **kwargs):
        print("hey baccha")
        t1 = time.time()
        returned_value = func1(*args,  **kwargs)
        t2 = time.time()
        t = t2-t1
        print(f'this fn took time{t}')
        return returned_value
    return wrapper_fn
    


@calculate_time

def sq_finder(n):  
    return [i**2 for i in  range(1,n+1)]
print(sq_finder(10))
 


#exercise 3 
# frame a fn that accept only integer value
from functools import wraps
def only_integer(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        if all([type(arg) == int for arg in args]):
            return function(*args, **kwargs)
        print("invalid arguments")
    return wrapper    

        

@only_integer
def add_all(*args):
    total = 0
    for i in args:
        total = total+i
    return total
print(add_all(1,2,3,4,5,[9,8,5]))
 '''


# generators
# it basically wrap the decorate fn 
'''
from functools import wraps
def allow_int(data_type):
    def only_integer(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            if all([type(arg) == int for arg in args]):
                return function(*args, **kwargs)
            print("invalid arguments")
        return wrapper    
    return only_integer
        

@allow_int(int)
def add_all(*args):
    total = 0
    for i in args:
        total = total+i
    return total
print(add_all(1,2,3,4,5))



# iterabl
l1 = [1,2,3]     # iterable
for i in l1:
    print(i)          # here i is iterator
'''


# generators are iterators 
# generator store one item of list/tuple aat a time while iterators store whole list at a time   
'''
def even_generator(n):
    for i in range(1, n+1):
        if i%2==0:
            yield(i)
for i in even_generator(10):            
    print(i)
even_nums = even_generator(10)
for num in even_nums:
    print(num)   
for num in even_nums:
    print(num)   
'''


# generator comprehension
# it is same as list comprehension only diff is () in stead of []
import time
t1 = time.time()
square = (i**2 for i in range(1,10))

'''
i = iter(square)
print(next(square))
print(next(square))
print(next(square))
'''
t2 = time.time()
t = t2-t1
print(t)
#for i in square:
#    print(i)


# xcalcule time
import time
t1 = time.time()
square = [i**2 for i in range(1,10000000)] 

t2 = time.time()    # list take more time than generator
t = t2-t1
print(t)






