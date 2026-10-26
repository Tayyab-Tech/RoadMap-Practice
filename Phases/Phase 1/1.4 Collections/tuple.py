# Tuple Python ka ek ordered collection hai jo multiple values store karta hai.
# Tuple immutable hota hai.
# Immutable ka matlab:
# Create hone ke baad tuple ko change nahi kar sakte.

data = ("Ali", 20, True)
print(data)

# do not change give type error 
data = (10,20,30)
# data[1] = 100

# empty tuple 
t = ()
print(type(t))

# without parantheses
t = 10,20,30
print(type(t))

# list to tuple 
l = [1,2,3]
t = tuple(l)
print(t)

# convert string into tuple 
print(tuple("Python"))

# dictionary to tuple 
d = tuple({
    "a":1,
    "b":2
}) #only print keys
print(d)


student = (
    "Ali",
    20,
    "CS"
) # this is packing
print(student)
name,age,dept = student #this is unpacking
print(name)
print(age)
print(dept)


# extend unpacking 
t=(1,2,3,4,5)

a,*b,c=t
print(a)
print(b)
print(c)

t = (10, 20, 30)
*a,b = t
print(a)
print(b)
# * sirf ek variable ke sath use ho sakta hai. otherwise syntax error