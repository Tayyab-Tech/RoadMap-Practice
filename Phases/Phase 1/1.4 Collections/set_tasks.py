# Question 1
# Find the union of the following sets.

a = {1,2,3,4}
b = {3,4,5,6}
result = a|b
print(result)




# Question 2
# Find the intersection.

a = {10,20,30,40}
b = {30,40,50,60}
result = a&b
print(result)





# Question 3
# Find the difference

a = {1,2,3,4}
b = {3,4,5}
result = a-b
print(result)




# Question 4
# Find the symmetric difference.

a = {1,2,3}
b = {3,4,5}
result = a.symmetric_difference(b)
print(result)





# Question 5
# Check whether the following set is a subset.

a = {1,2}
b = {1,2,3,4}
result = a.issubset(b)
print(result)





# Question 6
# Remove duplicate values from the following list using a set.

numbers = [10,20,20,30,40,30,10]
result = set(numbers)
print(result)





# Question 7
# Find all unique words from the following sentence.

sentence = "Python is easy and Python is powerful"
words = sentence.split()
unique_words = set(words)
print(unique_words)





# Question 8
# Check whether the following two sets are disjoint.

a = {1,2,3}
b = {4,5,6}
result = a.isdisjoint(b)
print(result)





# Question 9
# Find the common elements among all three sets.

a = {1,2,3,4}
b = {2,3,5}
c = {2,6,3}
result = a&b&c
print(result)





# Question 10
# Create a program that stores the names of students who attended a class in a set. Then:
# Add one new student.
# Remove one student.
# Check whether "Ali" attended the class.

students = {"Ali", "Ahmed", "Usman", "Hamza"}
students.add("New")
students.remove("Hamza")
if "Ali" in students:
    print("Ali attended the class.")
else:
    print("Ali did not attend the class.")
print("Students:", students)