

try:
    l=[1,4,5,3]
    i=int(input("enter the index"))
    print(l[i])
    
except:
    print("some error occured")

finally:
    print("i am always executed") 


print("\n")



def func1():
   try:
    l=[1,4,5,3]
    i=int(input("enter the index"))
    print(l[i])
    return 1

   except:
    print("some error occured")
    return 0

   finally:
    print("i am always executed") 
 

x=func1()
print(x)































