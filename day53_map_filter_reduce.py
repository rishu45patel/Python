#map

#def cube(x):
 #   return x*x*x

#print(cube(2))

l=[1,2,4,6,4,3]
#newl=[ ]
#for item in l:
    #newl.append(cube,l)

newl = list(map(lambda x:x*x*x,l))

print(newl)


#filter

def filter_fuunction(a):
    return a>1

newl= list(filter(filter_fuunction,l))
print(newl)

#reduce


from functools import reduce

numbers=[1,4,5,7]

sum=reduce(lambda x,y: x+y,numbers)
print(sum)









































