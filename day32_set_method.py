
#union and update method

name1={"ram","syam","ritesh","rishu"}
name2={"ram","roshan","ritesh","sanu",6}
name3=name1.union(name2)
print(name3)
name1.update(name2)
print(name1,name2)

a={12,2,34,54}
b={1,4,12,4,5}
a.update(b)
print(a)

#intersection and update method

num1={1,2,5,6,8,9,12}
num2={1,2,7,67,89,12}
num3=num1.intersection(num2)
print(num3)


num2.update(num1)
print(num2)

#synnetric_ difference and update

cities1={"tokyo","madrid","berlin","delhi"}
cities2={"tokyo","seoul","kabul","madrid"}
cities3=cities1.symmetric_difference(cities2)
print(cities3)

cities1.symmetric_difference_update(cities2)
print(cities1)


#difference

cities1={"tokyo","madrid","berlin","delhi"}
cities2={"tokyo","seoul","kabul","madrid"}
cities3=cities1.difference(cities2)
print(cities3)


#isdisjoint

cities1={"tokyo","madrid","berlin","delhi"}
cities2={"tokyo","seoul","kabul","madrid"}

print(cities1.isdisjoint(cities2))

cities1={"tokyo1","madrid3","berlin","delhi"}
cities2={"tokyo","seoul","kabul","madrid"}
print(cities1.isdisjoint(cities2))


#issuper set and subset


cities1={"tokyo","madrid","berlin","delhi"}
cities2={"seoul","kabul"}
print(cities1.issuperset(cities2))

cities3={"tokyo","madrid","delhi"}
print(cities1.issuperset(cities3))

print(cities3.issubset(cities1))


# add method

cities={"tokyo","madrid","berlin","delhi"}
cities.add("kabul")
print(cities)


#update method


cities1={"tokyo","madrid","berlin","delhi"}
cities2={"seoul","kabul"}
cities1.update(cities2)
print(cities1)


#remove/discard


cities1={"tokyo","madrid","berlin","delhi"}
cities1.remove("tokyo")

#cities1.discard("tokyo2")
print(cities1)


#pop

cities1={"tokyo","madrid","berlin","delhi"}
item=cities1.pop()
print(cities1)
print(item)

#del method and clear method



cities1={"tokyo","madrid","berlin","delhi"}
del cities1
cities1={"tokyo","madrid","berlin","delhi"}

cities1.clear()
print(cities1)


#####exit

info={"ritesh",1,12.43,"ram",50}

if"ritesh" in info:
    print("ritesh is present")
else:
    print("no")    










