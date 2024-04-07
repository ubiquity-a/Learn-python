# function
'''
def add_no(n1,n2):
    return n1+n2
add = add_no(2,6)
print(add)

def add_no(n1,n2,n3):
    print(n1+n2+n3)
add = add_no(2,1,8)
'''

# function greater of three
'''
def greatest(a,b,c):
    if a>b and b>c:
        print("a is greatest")
    else:
        if b>a and b>c:
            print("b is greatest")
        else:
            print("c is greatest")   
greatest(4,2,1)            '''

# palindrome
'''
def is_palindrone(str):
    str1 = str[-1::-1]
    if str1==str:           #naman
        return True
    else:
        return False    


str1 = input("enter any string")
print(is_palindrone(str1))
'''

# fibonacci series
'''
def fibonacci_seq(n):
    a = 0
    b = 1
    if n==1:
        print(a)
    elif n==2:
        print(a,b)
    else:
        print(a,b, end = " ")  
        for i in range(n-2):      
            c=a+b
            a = b
            b = c
            print(b , end = " ")
fibonacci_seq(7)   
'''

# scope
'''
x = 5
def func(x):
    
    x = 8
    return x
print(func(x))
print(x)  '''

# list
'''
bhai = [1,2,"mahi", 2.4,  None]
print(bhai)
print(bhai[1:3])    #slicing
bhai[1:]= 'mukku'            # breaking of string also can break list
print(bhai)
'''

# data list 
# add item to list using append method ,insert,extend
'''
list = [1,2,"mahi", 4, "akku"]
list.append("muku")
print(list)

# insert method to specific position   
list.insert(1,"dakku")
print(list)
list1 = [6,7,"akk"]           # can use extend method to add another list
list.extend(list1)
print(list)
print(list+list1)


#pop element ,del,remove
list.pop()
print(list)
del list[2]
print(list)
list.remove("akku")
print(list)
'''

# check whether the element is present
'''
fruit = ['apple',"mango","grapes"]
if 'banana' in fruit:
    print("yes")
else:
    print("no")    
    
# some method like count, sort method, reverse, clear, copy, sorted function
print(fruit.count("mango"))
fruit.sort()         # this method sort orignal list permanentaly
print(fruit)
fruit.reverse()
print(fruit)
print(sorted(fruit))  # this method does not sort original list
print(fruit)
#fruit.clear()   #empty the list
print(fruit)   
fruitess = fruit.copy()
print(fruitess)

# compare list
veg1 = ["began", "spinach", "tomato"]
veg2 = ["began", "spinach", "tomato"]
print(veg1 == veg2)  # true  check values are same
print(veg1 is veg2)   # false  because it check memeory location is same or not

'''

# join method is used to convert list to string
'''
veg1 = ["began", "spinach", "tomato"]
print(veg1)
print(','.join(veg1))

# list inside list //matrix
matrix = [[1,2,3],[4,5,6],[7,8,9]]
for i in matrix:
    for j in i:
        print(j)
print(matrix[2][2])
# type method is used to know datatype
print(type(matrix))

# using range function create list
list = [1,3,4,6,3,1,9,8,6,2,4,1,9,5,15]
print(list)
list.pop()                 # pop method return the poped value
print(list)

# index method
print(list.index(1, 6))   # means find 1 checking start from index 3
print(list.index(4,3,5))   # means find 4 checking start from index 9 and stop at 5

# exercise
def neg_list(list1):
    ng_list = []
    for i in list1:
        ng_list.append(-i)
    return ng_list
list1 = [1,2,4,6,3,2,9,8]        
print(neg_list(list1))
'''

# exercise
'''
list = [5,4,3,2,1,7,6]
def square(list):
    sq = []
    for i in list:
        sq.append(i**2)
    return sq
print(square(list))  


# reverse list


def rev(list):
    new = []
    for i in range(1,len(list)+1):
        p = list.pop()
        new.append(p)
    return new    
list = [1,3,4,5,6,9]
print(rev(list))

# reverse
def reverse(l):
    return l[-1::-1]
l = [1,2,3,4]
print(reverse(l))

# 3rd method to reverse
def reverse(l):
    l.reverse()
    return l
l1 = [1,2,8,3]
print(reverse(l1))


# exercise
def reverse_ele(l):
    ele = []
    for i in l:
        ele.append(i[-1::-1])
    return ele
l = ["akku","mahi"]
print(reverse_ele(l))

#exercise
def odd_even(l):
    odd = []
    even = []
    for i in l:
        if i%2 == 0:
            even.append(i)
        else:
            odd.append(i)
    result = [even, odd]      
    return result
l = [0,2,18,7,6,5,4]
print(odd_even(l))
'''

# exercise  print coomon element of two lists in one list
'''
def common(l1,l2):
    list1 = []
    for i in l1:
            if i in l2:
                list1.append(i) 
            else:
                pass    
    return list1
l1 = [1,2,8,9]
l2 = [6,8,2,4]
print(common(l1,l2))

# min max fn
l = [1,2,5,3,2]
print(min(l))
print(max(l))
# find greatest_diff
def greatest_diff(l):
     return max(l)-min(l)
l =[9,7,8,2]
print(greatest_diff(l))
'''

# exercise
'''
def type_count(l):
    count = 0
    for i in l:
        if type(i) == list:
            count += 1
    return count
l = [9,8,5,[1,3,7],[2,6]]  
print(type_count(l))      
'''

# tuples support len, index,count ,slicing method

'''
tuple4 = (1,2,3,4,5)
tuple1 = 'akku', 4,'mahi','siya'  
num = tuple(range(1,10))          # also a method of creating tuple 
tuple2 = (2)      #not tuple
tuple3 = (2,)
print(tuple)
print(type(tuple1))
print(type(tuple2))

# str,list,tuple
num = tuple(range(1,10))
tuple = str((1,2,3,4,5))
list = str([1,2,3,4,5])
print(type(list))

'''

# dictionary  , we can store anything
'''
user = {
    'name': 'akku',
         'age': 22,
         'list': [8,5]
         }
print(type(user))
user1 = dict(name = 'akku', age = 22, address = "kanpur")
print(type(user1))

# access data ----dict use no index
#use key to access
print(user['name'])
#add values in dict
user5 = {}
user5['name'] = 'ak'
print(user)
 
#check whther keys and value present or not
if 'name' in user:
    print("yes") 
else:
    print("no") 
if 'ak' in user.values():
     print("yes") 
else:
    print("no") 

# print all values
for i in user.values():
    print(i)        
for i in user:               #will print keys
    print(i) 

    

# add data in dict
user = {
    'name': 'akku',
         'age': 22,
         'list': [8,5]
         }
user['song']  = 'if'  
print(user)
# delete
print(user.pop('list'))
print(user)

# add dict into another dict using update method
user6 = {
    'id': 78,
    'sr': 11
}
user.update(user6)
print(user)


# items method is used for looping
# aslo a good way
user = {
    'name': 'akku',
         'age': 22,
         'list': [8,5]
         }
user_items = user.items()
print(user_items)
print(type(user_items))

user_keys = user.keys()
print(user_keys)
'''

# methods for dictionary
# fromkeys, can take at most two arguements at a time
'''
d = dict.fromkeys(['name','age'], ['akku', 34])
print(d)

'''
#get method is used to handle errors and it returns true or false
'''
user = {
    'name': 'akku',
         'age': 22,
         'list': [8,5]
         }
print(user.get('name'))
if user.get('bhag ja'):              #it return none----> false
    print("present")
else:
    pass    

# when we want any string in place of none ----use get method
print(user.get('fav', 'not found !'))

#clear method

#user.clear()
#print(user)


# copy method
user = {
    'name': 'akku',
         'age': 22,
         'list': [8,5]
         }
user1 =  user.copy()
print(user1)
print(user1.popitem())  #print popped item
print(user == user1)
'''

# exercise
'''
def cube_finder(n):
    cube = {}
    for i in range(1,n+1):
        cube[i]=i**3
    return cube

print(cube_finder(8))

#word counter in dictionary
def count_word(n):
    count = {}
    for i in n:
        count[i] = n.count(i)
    return count    
print(count_word("akanksha"))

'''
# exercise
'''
dict = {}
name = input("enter name")
age = input("enter age")
id = input("enter id")
fav_songs = input("enter fav songs").split(',')

dict['name'] = name
dict['age'] = age
dict['id'] = id
dict['fav_songs'] = fav_songs

for key, value in dict.items():
    print(f"{key}: {value}")


# print second largest item
n = int(input())
arr = map(int, input().split())
mylist = sorted(list(set(arr)))
print(mylist[-2])    
'''

'''

lst = []
for _i in range(int(input())):
    name = input()
    score = float(input())
    ele = [name, score]
    lst.append(ele)
print(lst)


lst = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
'''
'''
# Sort the list based on grades
lst.sort(key=lambda x: x[1])
print(lst)
# Find the lowest grade
lowest_grade = lst[0][1]

# Find the second lowest grade
second_lowest_grade = None
for student in lst:
    if student[1] > lowest_grade:
        second_lowest_grade = student[1]
        break

# Collect students with the second lowest grade
second_lowest_students = [student[0] for student in lst if student[1] == second_lowest_grade]

# Sort the names alphabetically
second_lowest_students.sort()

# Print each name on a new line
for student in second_lowest_students:
    print(student)
       


python_students = [['siya', 37.21], ['Berry', 97.21], ['Tina', 37.21], ['Akriti', 41], ['Harsh', 39]]

# Sort the students based on grades
python_students.sort(key=lambda x: x[1])

# Find the second lowest grade
second_lowest_grade = sorted(set(student[1] for student in python_students))[1]

# Extract names with the second lowest grade
second_lowest_students = [student[0] for student in python_students if student[1] == second_lowest_grade]

# Sort the names alphabetically
second_lowest_students.sort()

# Print each name on a new line
for student in second_lowest_students:
    print(student)
'''

'''
def solve(s):
    output = ""
    i = 0
    while i<len(s):
        if i[0].islower():
            output= i.title()+output
            output = i+output
        elif i[0].isdigit():
            output= i.capitalize()+output
            output = i+output
        else:
            output=i+output
               

    return output
if __name__ == '__main__':
    

    s = input()
    result = solve(s)
    print(result)
'''


'''
def convert_case(input_str):
    output_str = ""
    uppercase_next = False

    for char in input_str:
        if char.isalpha():
            if uppercase_next:
                output_str += char.title()
                uppercase_next = False
            else:
                output_str += char.title()
                uppercase_next = True
        else:
            output_str += char

    return output_str

input_str = "1 w 3 r 3g"
output_str = convert_case(input_str)
print(output_str)
'''

'''
def capitalize_words(text):
  """Capitalizes the first letter of each word in a string, ignoring numbers at the beginning.

  Args:
      text: The input string.

  Returns:
      The string with the first letter of each word capitalized.
  """
  words = text.split()
  result = []
  for word in words:
    if  word[0].isdigit():  # Check if the first character is not a digit
      result.append(word.capitalize())
    elif word[0].islower():
      result.append(word.capitalize()) 
    else:
      result.append(word)
  return " ".join(result)

text = "132 456 Wq  m e"
output = capitalize_words(text)
print(output)
'''
import math
import os
import random
import re
import sys
def solve(s):
 
  """Converts a string with numbers and letters to uppercase with spaces between words.

  Args:
      text: The input string.

  Returns:
      The converted string.
  """
  result = ""
  for char in s:
    if char[0].isalpha():
      result += char.capitalize() 
    elif char[0].isdigit():
        result += char 
    else:
      result += char.lower()
  return result.strip()

# Example usage

        
    
text = "3g"
converted_text = solve(text)
print(converted_text)

