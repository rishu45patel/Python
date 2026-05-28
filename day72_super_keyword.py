
class parentclass:
    def parent_method(self):
        print("this is the parent method")

class childclass(parentclass):
    def child_method(self):
        print("this is the child method")

        super().parent_method()

child_object=childclass()
child_object.child_method()                






class employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id

class programmer(employee):
    def __init__(self,name,id,lang):
        super().__init__(name,id) 
        self.lang=lang

rohan=employee("rohan das","456")
harry=programmer("harry","234","python")

print(harry.name)
print(harry.id)
print(harry.lang)






























