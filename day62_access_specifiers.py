
# public access 

class student:

    #constructor is defined
    def __init__(self,age,name):
        self.age = age     #public variable

        self.name = name   #public variable

obj = student(21,"harry")
print(obj.age)
print(obj.name)



# private access

class student:
    def __init__(self,age,name):
         self.__age = age  # an indication of private variable
         self.__name = name
    def __function(self): # an indication of private variable
        self.y=34
        print(self.y)

class subject(student):
    pass

obj=student(21,"harry")
obj1=subject(22,"ritesh")

#calling by object of class student

print(obj._student__age)
print(obj._student__function())

# calling by object of class subject

print(obj1._student__age)
print(obj1._student__function())




# name mangling

class myclass:
    def __init__(self):
        self._private_attribute="i am a private attribute"
        self.__mangled_attribute="i am a mangled"

my_object=myclass()

print(my_object._private_attribute)
print('_myclass__mangled_attribute')
#print(my_object.__mangled_attribute) #error




#protected access


class student:
    def __init__(self):
        self._name ="ritesh"

    def _funName(self): #protected method
        return "ias"

class subject(student):        # inherited class
    pass

obj = student()
obj1 = subject()

#calling by object of student class
print(obj._name)
print(obj._funName())

#calling by object of student class
print(obj._name)
print(obj._funName())

print(dir(obj))



























































