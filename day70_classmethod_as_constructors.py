
class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary


    @classmethod
    def fromstr(cls,string):
        return cls(string.split("-")[0], int(string.split("-")[1])) 

e1=employee("harry",12000)
print(e1.name)
print(e1.salary)


string="jhon-12000"
e2=employee.fromstr(string)
print(e2.name)
print(e2.salary)


print("\n")



class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    @classmethod
    def from_string(cls,string):
        name,age=string.split(',')
        return cls(name,int(age))
      
person=person.from_string("john,80")
print(person.name,person.age)    
                

        
        

















































