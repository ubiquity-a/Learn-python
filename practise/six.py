# object oriented programming
'''
class laptop:
    def __init__(self,bname,model_name,price):    # self represent object
        print('init method get called')
        self.bname = bname
        self.model_name = model_name
        self.price = price
l1 = laptop('pihhvak', 'i316bsdk',60000)     # init method get called
l2 = laptop('pihhvak', 'c-saleibsdk',60000)     #init method get called
print(l1.bname, l1.price)
'''

# instance method

'''
class person:
    def __init__(self, fname,lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def full_name(self):
        return f'{self.fname} {self.lname}'  

    def test_age(self):
        if self.age>19:
            return True  
        else:
            return False
p1 = person('akku', 'yadav', 22)
p2 = person('mukku', 'yadav', 12)

print(person.full_name(p2))
print(p1.full_name())   #also can write as
print(p2.test_age())


#exercise


class laptop:
    def __init__(self,bname,model_name,price):    # self represent object
        print('init method get called')
        self.bname = bname
        self.model_name = model_name
        self.price = price

    def percentage_off(self,n):
        discount = self.price-((n/100)*self.price) 
        return discount 


l1 = laptop('pihhvak', 'i316bsdk',60000)     # init method get called
l2 = laptop('pihhvak', 'c-saleibsdk',60000)     #init method get called
print(l1.bname, l1.price)
print(l1.percentage_off(70))



#exercise
import math
class circle:
    def __init__(self,radius,diameter):
        self.radius = radius
        self.diameter = diameter
    def area(self):
        areaOfCircle =  3.14*self.radius**2
        return areaOfCircle
    def circumference(self):
        circumf = 2*3.14*self.radius
        return circumf
c1 = circle(10,20)
c2 = circle(5,10)
print(c1.area())
print(c2.circumference())



#exercise

class laptop:
    discount_percent = 10
    def __init__(self,bname,model_name,price):    # self represent object
        print('init method get called')
        self.bname = bname
        self.model_name = model_name
        self.price = price

    def percentage_off(self,n):
        discount = self.price-((self.discount_percent/100)*self.price) 
        return discount 


l1 = laptop('pihhvak', 'i316bsdk',60000)     # init method get called
l2 = laptop('pihhvak', 'c-saleibsdk',60000)     #init method get called
l1.discount_percent = 40     # can change the value
print(l1.bname, l1.price)
print(l1.percentage_off(70))



#exercise
class teacher:
    count_instance = 0
    def __init__(self,name,sub,department):
        teacher.count_instance += 1
        self.name = name
        self.sub = sub
        self.department = department
t1 = teacher('siyaa','maths', 'IT') 
t2 = teacher('kiyaa','maths', 'IT') 
t3 = teacher('tiyaa','maths', 'IT') 
t4 = teacher('riyaa','maths', 'IT')  
print(teacher.count_instance)  

# exercise return no of isntance in string format
class teacher:
    count_instance = 0
    def __init__(self,name,sub,department):
        teacher.count_instance += 1
        self.name = name
        self.sub = sub
        self.department = department

    @classmethod       # genertaor help to use class as first arg
    def count_instances(cls):
        return f'no of instance of {cls.__name__} created in class is {cls.count_instance}'    
t1 = teacher('siyaa','maths', 'IT') 
t2 = teacher('kiyaa','maths', 'IT') 
t3 = teacher('tiyaa','maths', 'IT') 
t4 = teacher('riyaa','maths', 'IT')  
print(teacher.count_instances()) 



#exercise how to pass insatnce value as string
class teacher:
    count_instance = 0
    def __init__(self,name,sub,department):
        teacher.count_instance += 1
        self.__name = name
        self._sub = sub
        self.department = department

    @classmethod
    def from_string(cls,string):
        name,sub,dept = string.split(',')
        return cls(name,sub,dept)

    @classmethod       # genertaor help to use class as first arg
    def count_instances(cls):
        return f'no of instance of {cls.__name__} created in class is {cls.count_instance}'    

# can pass the arg as string
t1 = teacher('siyaa','maths', 'IT')   
t4 = teacher.from_string('akku,science,civil')
print(t4.count_instances())
print(t1._sub)      #not generate error
#print(t1.__name)   # give error
print(t1.__dict__)



'''
#static method
#@staticmethod
# use @property instead of getter method and @instance.setter instead of setter method here isntance can be any variable
#nkk
'''n = [1,2,3,4]
l1 = n.pop(2)  
print(n) 
'''


n = int(input())
arr = map(int, input().split())
mylist = list(arr)
l1 = max(mylist)
print(mylist.remove(l1) )



