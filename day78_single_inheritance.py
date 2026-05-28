

class animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
    def make_sound(self):
        print("sound made by the animal")

class dog(animal):
    def __init__(self,name,breed):
        animal.__init__(self,name,species="dog")
        self.breed=breed

    def make_sound(self):
        print("bark!")

d=dog("dog","dog")
d.make_sound()

a=animal("dog","dog")
a.make_sound()











































