# logging setup  
import logging

class InfoFilter(logging.Filter):
    def filter(self,record):
        return record.levelno == logging.INFO

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

info_handler = logging.FileHandler("Phase 1\\1.6 Reliability\\info.log")
info_handler.setLevel(logging.INFO)
info_handler.addFilter(InfoFilter())

error_handler = logging.FileHandler("Phase 1\\1.6 Reliability\\error.log")
error_handler.setLevel(logging.ERROR)

formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")

info_handler.setFormatter(formatter)
error_handler.setFormatter(formatter)

logger.addHandler(info_handler)
logger.addHandler(error_handler)


# Create separate log files for INFO and ERROR messages.

# logger.info("Program Started")
# logger.warning("Warning Message")
# logger.error("Something went wrong")




# Build a banking system that logs deposits, withdrawals, and failed transactions.

# balance = 5000
# while True:
#     print("\n1.Deposit")
#     print("2.Withdraw")
#     print("3.Exit")
#     choice = input("Choice: ")
#     if choice == "1":
#         amount = float(input("Amount: "))
#         balance += amount
#         logger.info(f"Deposited Rs.{amount}")
#         print("Deposit Successful")
#     elif choice == "2":
#         amount = float(input("Amount: "))
#         if amount > balance:
#             logger.error(f"Failed Withdrawal Rs.{amount}")
#             print("Insufficient Balance")
#         else:
#             balance -= amount
#             logger.info(f"Withdraw Rs.{amount}")
#             print("Withdrawal Successful")
#     elif choice == "3":
#         break
#     else:
#         print("Invalid Choice")








# Log every student's registration details and invalid registrations.

# students = {}
# print("Enter 0 to exit")
# while True:
#     roll = int(input("Roll No: "))
#     if roll == 0:
#         print("Program ended")
#         break
#     marks = int(input("Marks: "))
#     if roll in students:
#         logger.error(f"Duplicate Roll Number {roll}")
#         print("Roll already exists")
#     elif marks < 0 or marks > 100:
#         logger.error(f"Invalid Marks {marks}")
#         print("Invalid Marks")
#     else:
#         students[roll] = marks
#         logger.info(f"Student Registered Roll={roll} Marks={marks}")
#         print("Registration Successful")





# Build an inventory management system that logs stock updates, errors, and critical failures.

stock = {
    "Laptop": 10,
    "Mouse": 20
}
item = input("Item: ")
try:
    qty = int(input("Quantity: "))
    if item not in stock:
        logger.error(f"{item} not found")
        print("Item not found")
    elif qty <= 0:
        logger.error("Invalid Quantity")
        print("Invalid Quantity")
    elif qty > stock[item]:
        logger.critical(f"Stock Finished for {item}")
        print("Not enough stock")

    else:
        stock[item] -= qty

        logger.info(f"{qty} {item} sold")
        logger.info(f"Remaining Stock = {stock[item]}")

        print("Sale Successful")

except ValueError:

    logger.error("Quantity must be integer")

    print("Invalid Input")