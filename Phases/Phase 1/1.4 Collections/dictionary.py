# Dictionary key : value pair mein data store karti hai. 

student = {
    "name": "Ali",
    "age": 20,
    "city": "ISL"
}
print(student.get("name")) #if not found return None or add default value as below
print(student.get("name1","Not found"))

# update 
student["city"] = "Lahore"
# multiple value update
student.update({
    "city":"Multan",
    "gender":"Male"
})

# pop key value 
# student.pop("age")

# last key value remove
# student.popitem()


print(student)

print(student.keys())
print(student.values())
print(student.items())

for value in student.values():
    print(value)

# keys are unique
# if same keys are found then last key value is prefered 
# dictionary is mutable but list in keys is not allowed

# Allowed
d = {
    1: "Ali",
    "name": "Ahmed",
    (1,2): "Tuple"
}
# Not Allowed
# {
#     [1,2]: "List"
# }

# add 
d["age"] = 21

print(d)
print(d[(1,2)])