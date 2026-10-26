# Searching ---> in,not in,index(),count()
# | Operator | Return                       |
# | -------- | ---------------------------- |
# | `in`     | True agar value mojood ho    |
# | `not in` | True agar value mojood na ho |

# in---> check karta hai ke koi value list mein mojood hai ya nahi.
fruits = ["Apple", "Banana", "Orange"]
print("Apple" in fruits)
# returns boolean value true or false 


# not in
# Ye in ka opposite hai.
# Check karta hai ke value list mein nahi hai.
fruits = ["Apple", "Banana"]
print("Orange" not in fruits)

users = ["Ali", "Ahmed"]
new_user = "Tayyab"
if new_user not in users:
    users.append(new_user)
print(users)


# index()----> kisi value ka pehla index return karta hai.
fruits = ["Apple", "Banana", "Orange"]
print(fruits.index("Banana"))

# Start Position from index 1 
numbers = [10, 20, 40, 30,10]
print(numbers.index(10, 1))


# start end syntax
# list.index(value, start, end)
numbers = [10, 20, 10, 30, 10]
print(numbers.index(10, 2, 5))
# search from 2 index to 4 index 



# count()--> batata hai ke koi value list mein kitni baar mojood hai.
numbers = [10, 20, 10, 30, 10]
print(numbers.count(10))

