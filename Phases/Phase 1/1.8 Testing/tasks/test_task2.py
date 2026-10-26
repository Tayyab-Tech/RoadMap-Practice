# Write TDD tests before implementing a prime number checker. 
import pytest
from task2 import is_prime, BankAccount, read_file, get_user, login, parse_json

def test_prime_number():
    assert is_prime(7) is True
    assert is_prime(13) is True


def test_not_prime():
    assert is_prime(4) is False
    assert is_prime(10) is False


def test_edge_cases():
    assert is_prime(0) is False
    assert is_prime(1) is False
    assert is_prime(2) is True


# Test a bank account class covering deposits, withdrawals, and insufficient funds. 
def test_deposit():
    account = BankAccount(1000)
    account.deposit(500)
    assert account.balance == 1500

def test_withdraw():
    account = BankAccount(1000)
    account.withdraw(300)
    assert account.balance == 700

def test_insufficient_funds():
    account = BankAccount(500)
    with pytest.raises(ValueError):
        account.withdraw(1000)


# Write tests for a file-reading function and verify it handles missing files correctly.
def test_missing_file():
    with pytest.raises(FileNotFoundError):
        read_file("missing.txt")

def test_read_file(tmp_path):
    file = tmp_path / "test.txt"
    file.write_text("Hello Python")
    result = read_file(file)
    assert result == "Hello Python"


# Use mocking to test a function that fetches data from an API without making real network calls.
from unittest.mock import patch

@patch("requests.get")
def test_get_user(mock_get):
    mock_get.return_value.json.return_value = {
        "id": 1,
        "name": "Test Mock",
        "email": "test-mocking@gmail.com"
    }
    result = get_user()
    mock_get.assert_called_once_with(
        "https://jsonplaceholder.typicode.com/users/1"
    )

    assert result["name"] == "Test Mock"


# Test a login function with valid credentials, invalid credentials, and empty inputs.
def test_valid_login():
    assert login("admin", "1234") is True

def test_invalid_username():
    assert login("user", "1234") is False

def test_invalid_password():
    assert login("admin", "wrong") is False

def test_empty_username():
    assert login("", "1234") is False

def test_empty_password():
    assert login("admin", "") is False


# Write tests for a JSON parser that validates both correct and malformed JSON.
import json
def test_valid_json():
    data = '{"name": "Ali", "age": 20}'
    result = parse_json(data)
    assert result["name"] == "Ali"
    assert result["age"] == 20

def test_invalid_json():
    data = '{"name": "Ali", "age": }'
    with pytest.raises(json.JSONDecodeError):
        parse_json(data)