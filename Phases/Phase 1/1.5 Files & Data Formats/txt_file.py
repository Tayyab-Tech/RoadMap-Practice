# file is used to store data permanently.

# Instead of storing data in variables (which disappear when the program ends), we save it into files.

# Python mainly uses:

# TXT (.txt)
# CSV (.csv)
# JSON (.json)
# file = open("file.txt", "r")

# | Mode | Meaning           |
# | ---- | ----------------- |
# | r    | Read              |
# | w    | Write (overwrite) |
# | a    | Append            |
# | x    | Create new file   |
# | rb   | Read binary       |
# | wb   | Write binary      |
# | r+   | Read + Write      |
# | a+   | Read + Append     |

# ========================= TXT file ======================

# with open("Phase 1\1.5 Files & Data Formats\txt\data.txt", "w") as file:
#     file.write("Hello") #overwrite file
# # writing multiple lines --> overwrite file 
lines = [
    "Ali\n",
    "Ahmed\n",
    "Sara\n"
]
with open("Phase 1\1.5 Files & Data Formats\txt\names.txt", "w") as file:
    file.writelines(lines)

# best way to open and close file 
with open("Phase 1\1.5 Files & Data Formats\txt\data.txt", "r") as file:
    data = file.read()

print(data)


with open("Phase 1\1.5 Files & Data Formats\txt\data.txt") as file:
    one_line = file.readline()
print("One Line" , one_line)


with open("Phase 1\1.5 Files & Data Formats\txt\data.txt") as file:
    data = file.readlines()
print(data)

with open("Phase 1\1.5 Files & Data Formats\txt\data.txt", "a") as file:
    file.write("\nPython")

# Important TXT Methods
# read()
# readline()
# readlines()
# write()
# writelines()
# close()
