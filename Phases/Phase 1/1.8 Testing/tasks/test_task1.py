# Write unit tests for a function that adds two numbers.
from task1 import add, is_even, is_palindrome, factorial, find_max, validate_password, calculate_grade, calculate_total_after_discount
import pytest

def test_add():
    assert add(2,3) == 5
    assert add(10,20) == 30




# Test a function that checks whether a number is even or odd.
def test_is_even():
    assert is_even(2) is True
    assert is_even(5) is False
    assert is_even(8) is True
    assert is_even(11) is False
    assert is_even(14) is True


# Test a palindrome-checking function with different inputs. 
def test_is_palindrome():
    assert is_palindrome("madam") is True
    assert is_palindrome("hello") is False
    assert is_palindrome("level") is True
    assert is_palindrome("hey") is False
    assert is_palindrome("racecar") is True



# Write tests for a factorial function, including edge cases. 
def test_factorial():
    assert factorial(6) == 720
    assert factorial(5) == 120
    assert factorial(4) == 24
    assert factorial(3) == 6
    assert factorial(2) == 2

def test_factorial_zero():
    assert factorial(0) == 1


def test_factorial_negative():
    with pytest.raises(ValueError):
        factorial(-5)


# Test a function that finds the maximum value in a list.
def test_find_max():
    assert find_max([6,4,2,8,10,3,1]) == 10
    assert find_max([10,20,30]) == 30
    assert find_max([-5,-2,-10]) == -2


# Write tests for a password validation function. 
def test_valid_password():
    assert validate_password("Password123") is True


def test_short_password():
    assert validate_password("Pass1") is False


def test_password_without_digit():
    assert validate_password("Password") is False


def test_password_without_uppercase():
    assert validate_password("password123") is False



# Test a student grade calculator for different score ranges.
def test_calculate_grade():
    assert calculate_grade(95) == "A"
    assert calculate_grade(85) == "B"
    assert calculate_grade(75) == "C"
    assert calculate_grade(65) == "D"
    assert calculate_grade(50) == "F"

def test_calculate_invalid_grade():
    with pytest.raises(ValueError):
        calculate_grade(110)


# Write unit tests for a shopping cart total calculation with discounts.         
def test_no_discount():
    assert calculate_total_after_discount(1000,0) == 1000

def test_10_percent_discount():
    assert calculate_total_after_discount(1000, 10) == 900


def test_20_percent_discount():
    assert calculate_total_after_discount(500, 20) == 400