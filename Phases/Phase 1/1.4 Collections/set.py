# Set Python ka ek collection data type hai jo unique (duplicate na hon) values store karta hai.
# Set unordered hota hai.

# Index nahi hota.
# Order fix nahi hota.
# Har baar print karne par order different ho sakta hai.

# unordered 
s = {10, 20, 30}
# so no indexing
# print(s[0])   # Error


# no duplicate values allow 
s = {10, 20, 10, 30,100}
print(s)


# mutable. can add or remove items 
s.add(40)
print(s)

# like remove in list if value not found it can't show any error 
s.discard(100)
print(s)

# Ye dictionary banegi.
new = {}
# Empty Set
new = set()



# union()-->Dono sets combine.
a = {1,2,3}
b = {3,4,5}
print(a|b)
print(a.union(b))


# intersection()-->Common values.
print(a&b)
print(a.intersection(b))


# difference()-->Jo sirf pehle set mein ho.
print(a-b)
print(a.difference(b))


# symmetric_difference()-->Jo common nahi hain.
print(a^b)
print(a.symmetric_difference(b))


# Comparison Methods

a = {1,2}
b = {1,2,3}

print(a.issubset(b))
print(b.issuperset(a))
print(a.isdisjoint(b)) #Check karta hai common element hai ya nahi.