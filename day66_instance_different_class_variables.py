

class Employee:
    companyName = "apple"
    noOfEmployees = 0
    def __init__(self,name):
        self.name = name
        self.raise_amount = 0.02
        Employee.noOfEmployees +=1
    def showDetails(self):
        print(f"the name of the Employee is {self.name} and the raise amount in {self.noOfEmployees } sized {self.companyName} is {self.raise_amount}")

#Employee.showDetails(emp1)
emp1=Employee("harry")
emp1.raise_amount=0.3
emp1.companyName="apple india"
emp1.showDetails() 
Employee.companyName="google"
print(Employee.companyName)


emp2 =Employee("rohan")
emp2.companyName = "nestle"
emp2.showDetails()

print("\n")
# class variables


class myclass:
    class_variable =0

    def __init__(self):
        myclass.class_variable +=1

    def print_class_variable (self):
        print(myclass.class_variable)

obj1 = myclass()
obj2 = myclass()

obj1.print_class_variable()
obj2.print_class_variable()



print("\n")

# instance variables

class myclass:
    def __init__(self,name):
        self.name=name


    def print_name(self):
        print(self.name)


obj1=myclass("ritesh")
obj2=myclass("rohan")

obj1.print_name()
obj2.print_name()







































