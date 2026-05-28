


class employee:
    company="apple"
    def show(self):
        print(f"the name is {self.name} and company is {self.company}")

    @classmethod
    def changecompany(cls,newcompany):
        cls.company=newcompany

e1=employee()
e1.name="harry"
e1.show()
e1.changecompany("tasla")
e1.show()
print(employee.company)            











































