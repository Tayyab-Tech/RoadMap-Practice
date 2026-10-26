# Copying
# copy(),list(),=,deep copy ()

# = (Assignment) 
a = [10,20,30]
b = a
print(b)


a = [10,20,30]
b = a
b.append(40)
print(a)


# copy()--> New list banata hai.

a = [10,20,30,40]
b = a.copy()
b[1]=100
a.append(50)
print(a)
print(b)

# list()---> Ye bhi new copy banata hai.

a = [10,20]
b = list(a)
# print(b)

a = [1,2]
b = list(a)
b.append(3)
# print(a)
# print(b)

import copy
a = [
    [1,2],
    [3,4]
]
# b = a.copy() # shalllow copy bnata hai jo sirf outer list ko copy krta nested list ko copy nhi krta
b = copy.deepcopy(a) # orignal nested list ko change ni kry ga 
b[0][0] = 100
# print(a)
# print(b)