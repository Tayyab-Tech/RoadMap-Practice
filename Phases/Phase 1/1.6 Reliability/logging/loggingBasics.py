# Logging records what your program is doing.
# Instead of
# print("User logged in")
# Use logging.


# Why Logging?
# Track errors
# Record events
# Debug production programs
# Monitor applications


import logging # needed for logging
# logging.basicConfig(level=logging.WARNING) 
# logging.basicConfig(level=logging.WARNING,filename="path") 
# logging.debug("Debug")
# logging.info("Info")
# logging.warning("Warning")
# logging.error("Error")
# logging.critical("Critical")
# logging.info("Program started")


# Logging Levels
# | Level    | Purpose              |
# | -------- | -------------------- |
# | DEBUG    | Detailed information |
# | INFO     | General information  |
# | WARNING  | Something unexpected |
# | ERROR    | Error occurred       |
# | CRITICAL | Serious problem      |



# logging.basicConfig(
#     filename="Phase 1\\1.6 Reliability\\app.log",
#     # filemode='w',
#     level=logging.DEBUG,
#     format='%(asctime)s | %(name)s | %(levelname)s | %(message)s',
# )

# logging.info("Application Started")
# try:
#     print(10 / 0) 

# except Exception:
#     logging.exception("An error occurred") # this stores error in app.log file 


# 4. Validation
# Validation checks whether user input or data is correct before using it.

# Email Validation (Basic)
# email = input()
# if "@" in email and "." in email:
#     print("Valid")
# else:
#     print("Invalid")


# Combining Validation + Exceptions
# while True:

#     try:
#         salary = float(input())

#         if salary <= 0:
#             raise ValueError

#         break

#     except ValueError:
#         print("Enter a positive salary.")


# logging.basicConfig(level=logging.INFO)

# while True:

#     try:
#         age = int(input("Age: "))

#         if age < 18:
#             raise ValueError("Age must be 18+")

#         logging.info("Valid age entered")
#         print("Access Granted")
#         break

#     except ValueError as e:
#         logging.error(e)
#         print(e)



# import logging
# logger = logging.getLogger("mytestlogger")
# logger.setLevel(logging.DEBUG)
# handler = logging. StreamHandler()
# formatter = logging.Formatter('%(asctime)s - %(name)s -%(levelname)s -%(message)s')
# handler.setFormatter(formatter)
# logger.addHandler(handler)
# file_handler = logging.FileHandler("Phase 1\\1.6 Reliability\\mt_test_data.log",mode='a')
# file_handler.setFormatter(formatter)
# logger.addHandler(file_handler)

# # logger.info("infoooooo")
# # logger.debug("debuggggg")

# def addition(a,b):
#     logger.info(f" value of a is {a} and b is {b}")
#     logger.info(f"we are doing a calculation operation by doing a addioin of {a} and {b}")
#     logger.info(f"it will return {a} + {b}")
#     return a+b
# addition(4,5)



import logging

logging.basicConfig(
    filename="Phase 1\\1.6 Reliability\\app.log",
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

# logging.info("Application started")
# logging.error("Something went wrong")



# ========================= Using a Named Logger (recommended for real projects) =================

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)

# handler = logging.StreamHandler()
# formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s")
# handler.setFormatter(formatter)
# logger.addHandler(handler)

# logger.debug("Debugging details here")
# logger.info("Something normal happened")
# try:
#     1 / 0
# except ZeroDivisionError:
#     logger.exception("An error occurred")




# everywhere use this 
import logging

logger = logging.getLogger("my_app")
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)

file_handler = logging.FileHandler("Phase 1\\1.6 Reliability\\app1.log")
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.debug("Detailed info (file only)")
logger.warning("Shown in both console and file")