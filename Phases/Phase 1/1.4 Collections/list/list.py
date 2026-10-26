numbers = [1,2,3,4,5]
names = ["Ali","Ahmed"]
multiple_datatype = [10,"Hello",3.14,True]
empty = []

# index accessing 
print(numbers[0])
print(numbers[-1]) #reverse start
print(numbers[3])
# list slicing 
print(numbers[1:4])
print(numbers[:3]) # 0 to 3rd index
print(numbers[::2]) #get every second item after 0 index
print(numbers[::-1]) # reverse list
# update list item 
numbers[2] = 100
print(numbers)
# length check 
print(len(numbers))

# some methods of list 

# Adding Elements
# append(),extend(),insert()
# Removing Elements
# remove(),pop(),del,clear()
# Searching
# in,not in,index(),count()
# Sorting
# sort(),sorted(),reverse(),reversed()
# Copying
# copy(),list(),=,deep copy ()
# Joining Lists
# +,extend(),*



# Common Functions
# len(),sum(),max(),min(),any(),all(),enumerate(),zip()


# len()-->List mein total items batata hai.

fruits = ["Apple","Banana","Orange"]
print(len(fruits))


# sum()-->Sirf numeric values ka total karta hai.

numbers = [10,20,30]
print(sum(numbers))
# solution for multiple datatype in list 
prices = [100, 250, "N/A", 300]
total = sum(x for x in prices if isinstance(x, (int, float)))
print(total)


# max()-->Largest value.
numbers = [10,30,20]
print(max(numbers))
# compare alphabets 
names = ["Ali","Usman","Ahmed"]
print(max(names))


# min()-->Smallest value.

numbers = [10,30,20]
print(min(numbers))


# any()-->Agar kam az kam ek value True ho to True return karta hai.

values = [False,False,True]
print(any(values))
numbers = [0,0,1] # 5 is true and 0 is false
print(any(numbers))


# all()-->Agar sab values True hon tab hi True return karta hai.
numbers = [1,2,3]
print(all(numbers))

# enumerate()-->Loop ke sath index bhi deta hai.
fruits = ["Apple","Banana","Orange"]
for index, fruit in enumerate(fruits):
    print(index, fruit)
# start value changed 
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)



# zip()-->Do ya zyada iterables ko pair bana deta hai.
names = ["Ali","Ahmed","Usman"]
marks = [80,90,75]
print(list(zip(names, marks)))

for name, mark in zip(names, marks):
    print(name, mark)
