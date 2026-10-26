# Write TDD tests before implementing a prime number checker. 
def is_prime(num):
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


# Test a bank account class covering deposits, withdrawals, and insufficient funds. 
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")

        self.balance -= amount


# Write tests for a file-reading function and verify it handles missing files correctly.
def read_file(filename):
    with open(filename, "r") as file:
        return file.read()


# Use mocking to test a function that fetches data from an API without making real network calls.
import requests
def get_user():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/1"
    )

    response.raise_for_status()

    return response.json()
user = get_user()
# print(user)
print(user["name"])
print(user["email"])


# Test a login function with valid credentials, invalid credentials, and empty inputs. 
def login(username, password):
    if not username or not password:
        return False
    if username == "admin" and password == "1234":
        return True

    return False


# Write tests for a JSON parser that validates both correct and malformed JSON.
import json
def parse_json(data):
    return json.loads(data)