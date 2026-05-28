

x=4
print(x)

def hello():
    x=5

    print(f"the local x is {x}")
    print("hello ritesh")

print(f"the global x is {x}")
hello()
x=5
print(f"the global x is {x}")
   

x=10 #global variable

def my_function():
    global x
    x=4
    y=5 #local variable

my_function()
print(x)
#print(y)#this will cause an error because y is a local variable and is not accessiable outside of the function



































