#slicing
name = "akkuuuuu  listen!! you are the most beutiful person by heart okay don't be doubtful  "
#print(name[0:4])
#print(name[-1])

#step arguement

#print(name[0:5:2])  # here 2 means 2 step move
#print(name[-1::-1])  # reverse string
#namee = input("enter name")
#print(namee[-1::-1])

# string method  
'''print(len(name))
print(name.lower())
print(name.upper())
print(name.title())  # first letter wil be upper rest wilbe small
print(name.count("s"))
print(name.rstrip())
print(name.lstrip())
print(name.strip())'''

# find and replace method
'''print(name.replace(" ", "")) 
print(name.find("doubt"))              # this method return index
print(name.replace("doubt", "", 1))'''

# center method


namee = "mahi"
print(namee.center(9, "*"))
x = 6
if x>=6:
    pass            # pass statement is used to ignore that block


# number guessing game

'''
winning_number = 9 
guess_no = input("guess any number")
guess_numb = int(guess_no)
if guess_numb == winning_number:
    print("you won!!")
elif guess_numb < winning_number:  
    print("too low")  
else:
    print("too high")  '''

 # exercise
'''name, age = input("enetr name and age").split(",")
age = int(age)
if (name[0] == 'a' or name[0] == 'A') and age>10:
    print("can watch coco") 
else:
    print("can't")   ''' 

#exercise
'''age = input("enetr age")
age = int(age)
if 1<=age<=3:
    print("free") 
elif 4<=age<=10 :
    print("150 rs") 
elif 11<=age<=60:
    print("250 rs")  
else:
    print("200 rs") '''
                
# in keyword
name = "akku is good"
if 's' in name:
    print("yes")
else:
    print("no")    
print(name.find("kk"))           #return 1 or -1


#  empty method and 
'''name1 = input("enter it now if you want")
if name1:
    print(f" name is {name1}")
else:
    print("can\'t type")  '''  



# while loop
'''number = input("enter number")
number = int(number)
sum = 0
i = 0
while i<=number:
    sum= sum+i
    i = i+1
print(f"sum is {sum}") '''

# exercise sum of the digit of given number

'''string = input("enter number more than one digit")
n = len(string)
i = 0
sum = 0
while i < n:
    sum = sum+int(string[i])
    i = i+1
print(sum)    '''

# exercise print count of each word
# amazing

'''name = input("enter name")
i = 1
while i<len(name):
    print(f" {name[i]} : {name.count(name[i])}")
    i+=1        '''


    # for loop
    # for in loop and for each loop
'''for i in range(1,10):    # means range from 1 to 9
    print(f"hi :{i}")

    # exercise sum of n numbers
sum = 0    
for i in range(1,11):
    sum = sum+i
print(sum)   '''

#exercise
'''n = input('enter any no')
sum = 0
for i in range(1,len(n)):
    sum=sum+int(n[i])
print(sum)

# exercise
name = input("enter name")
for i in range(1, len(name)):
    print(f"{name[i]}: {int(name.count(name[i]))} ")   '''



# break and continue
''' for i in range(1,11):
    if i == 5:
        break
    print(i)


for i in range(1,11):
    if i == 5:
        continue
    print(i)   '''

    # guess number winning game
'''
import random
winning_no = random.randint(1,100)
number = int(input("enter number"))
guess = 1
game_over = True
while game_over:
    if number == winning_no:
        print(f"you win in guess time {guess}")
        game_over = True
    else:
        if number<winning_no:
            print("tooo low")
            guess+=1
            number = int(input("again enter no"))
          
        else:
            print("too high")
            guess+=1
            number = int(input("again enter no"))

'''
# exercise



    # dry coding  means don't repeat steps

    # step arguement
'''for i in range(0,10,2):          # here 2 work as step/gap
    print(i)                      # can help in finding even and odd

for i in range(10,0,-1):          # here 2 work as step/gap
    print(i)                '''          

# for loop with string
    
'''
for i in "akku":
    print(i)   
name = "babyyy"
for i in name:
    print(i) 
'''
#exercise
'''
num = input("enter any no")
sum = 0
for i in num:                           # error not solved
    sum = sum+ int(i)
print(sum)

'''

#exercise
'''
n1,n2 = input("enter number").split(",")
n1 = int(n1)
n2 = int(n2)
if n1>n2:
    print("n1 is greater")
else:
    print("n2 is greater")   
    ''' 
# using function

'''
def greater(n1,n2):
    
    if n1>n2:
        return n1
    return n2

sol = greater(6,3)
print(sol) '''