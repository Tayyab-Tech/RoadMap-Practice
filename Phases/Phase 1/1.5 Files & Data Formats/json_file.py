# JSON = JavaScript Object Notation
# Most APIs use JSON.
# Example
# {
#     "name": "Ali",
#     "age": 20,
#     "city": "Lahore"
# }
import json

# # Convert Python → JSON
# student = {
#     "name": "Ali",
#     "age": 20
# }
# json_data = json.dumps(student)
# print(json_data)
# # dumps()
# # Converts object → JSON string


# # Convert JSON → Python
# data = '{"name":"Ali","age":20}'
# student = json.loads(data)
# print(student)



student = {
    "name": "Ali",
    "age": 20
}
# write json 
with open("Phase 1\\1.5 Files & Data Formats\\student.json", "w") as file:
    json.dump(student, file)


with open("Phase 1\\1.5 Files & Data Formats\\student.json") as file:
    data = json.load(file)

print(data)



# JSON Methods
# | Method  | Purpose              |
# | ------- | -------------------- |
# | dump()  | Python → JSON file   |
# | load()  | JSON file → Python   |
# | dumps() | Python → JSON string |
# | loads() | JSON string → Python |


# dump()
# Writes into a file.
# dumps()
# Returns a JSON string.
# load()
# Reads JSON from a file.
# loads()
# Reads JSON from a string.


# exception handling 
try:
    with open("abc.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found")
    