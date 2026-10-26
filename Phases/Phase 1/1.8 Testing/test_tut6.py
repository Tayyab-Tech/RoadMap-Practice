import pytest
from tut6 import Student
from datetime import datetime

@pytest.fixture(scope = "function") # custom fixtures  ---> default scope is function if needed change it to module to change actual values of main class or function 
def dummy_student():
    return Student("nikhil", datetime(2000, 1, 1), "coe")

def test_student_get_age(dummy_student):
    dummy_student_age = (datetime.now() - dummy_student.dob).days // 365
    assert dummy_student.get_age() == dummy_student_age

def test_student_add_credits(dummy_student) :
    dummy_student.add_credits(5)
    assert dummy_student.get_credits() == 5

def test_student_get_credits(dummy_student) :
    assert dummy_student.get_credits() == 0