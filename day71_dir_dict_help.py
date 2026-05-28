
# dir method

#x=[1,2,3]
x="ritesh"

print(dir(x))

print('\n')

# dict method

class person:
    def __init__(self,name,age):
        self.name =name
        self.age=age
        self.version=1

p=person("john",30)
print(p.__dict__)        
    

print("\n")

# help method


class person:
    def __init__(self,name,age):
        self.name =name
        self.age=age
        self.version=1

p=person("john",30)
print(p.__dict__)        
print(help(person))    





