# # logging setup 
# import logging
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)

# consoleHandler = logging.StreamHandler()
# consoleHandler.setLevel(logging.DEBUG)

# formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s")
# consoleHandler.setFormatter(formatter)

# logger.addHandler(consoleHandler)



# # Log a message when the program starts.
# logger.info(f"Program started")
# print("Welcome")





# # Log user login attempts.
# username = input("Enter username: ")
# logger.info(f"Login Attempt by user : {username}")
# if username == "admin":
#     print("Login Successful")
#     logger.info("Login Successfull")
# else:
#     print("Login Failed")
#     logger.warning("Login Failed")





# # Log successful calculations in a calculator.
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# result = num1 + num2
# logger.info(f"Calculation Performed : {num1} + {num2} = {result}")
# print("Result = ",result)






# # Log warning messages for invalid menu choices.
# print("1. Deposit")
# print("2. Withdraw")
# choice = input("Enter choice: ")
# if choice not in ["1","2"]:
#     logger.warning(f"Invalid menu choice entered : {choice}")
#     print("invalid choice")






# # Log errors when invalid input is entered.
# try:
#     age = int(input("Enter age: "))
#     print("Age =", age)
# except ValueError:
#     logger.error("User entered invalid age input")
#     print("Please enter a valid number")






# =========================================================================



import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# consoleHandler = logging.StreamHandler()
# consoleHandler.setLevel(logging.DEBUG)

fileHandler = logging.FileHandler("Phase 1\\1.6 Reliability\\app3.log")
fileHandler.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s")
# consoleHandler.setFormatter(formatter)
fileHandler.setFormatter(formatter)

# logger.addHandler(consoleHandler)
logger.addHandler(fileHandler)


# Save all logs to a file named app.log.

# logger.info("Program Started")
# logger.warning("This is a warning")
# logger.error("This is an error")
# print("Logs saved in app.log")






# Log every exception that occurs in a calculator program.

# try:
#     num1 = float(input("Enter first number: "))
#     op = input("Enter operator (+,-,*,/): ")
#     num2 = float(input("Enter second number: "))
#     if op == "+":
#         print(num1 + num2)
#     elif op == "-":
#         print(num1 - num2)
#     elif op == "*":
#         print(num1 * num2)
#     elif op == "/":
#         print(num1 / num2)
#     else:
#         raise ValueError("Invalid Operator")
# except Exception as e:
#     logger.error(e)
#     print("An error occurred.")





# Log successful and failed login attempts separately.

# username = input("Username: ")
# password = input("Password: ")
# if username == "admin" and password == "1234":
#     logger.info(f"Successful login : {username}")
#     print("Login Successful")
# else:
#     logger.warning(f"Failed login attempt : {username}")
#     print("Invalid Username or Password")






    
# Log file read/write operations.
try:
    # Write to file
    file = open("Phase 1\\1.6 Reliability\\data.txt", "w")
    file.write("Hello Python")
    file.close()

    logger.info("Data written to data.txt")

    # Read from file
    file = open("data.txt", "r")
    content = file.read()
    file.close()

    logger.info("Data read from data.txt")

    print(content)

except Exception as e:
    logger.error(e)