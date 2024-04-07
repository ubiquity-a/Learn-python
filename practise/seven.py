# encapsulation , abstraction, name mangling (not a convention)
class person:
    def __init__(self, fname,lname, age):
        self.fname = fname
        self.lname = lname
        self._age = age

    def full_name(self):
        return f'{self.fname} {self.lname}'  

    def test_age(self):
        if self._age>19:
            return True  
        else:
            return False
p1 = person('akku', 'yadav', 22)
p2 = person('mukku', 'yaduvanshi', 12)

print(person.full_name(p2))
print(p1.full_name())   #also can write as
print(p2.test_age())