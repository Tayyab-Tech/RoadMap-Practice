
from datetime import datetime
from tut7 import get_topper
import pytest
from tut7 import Student
from datetime import datetime

# @pytest.fixture(scope = "function") # custom fixtures  ---> default scope is function if needed change it to module to change actual values of main class or function 
# def dummy_student():
#     return Student("nikhil", datetime(2000, 1, 1), "coe",20)

# @pytest.fixture # below function gets multiple list of students which relays on fixture factory
# def multiple_dummy_student() : 
#     def make_dummy_student (name, credits):
#         return Student(name, datetime(2000, 1, 1), "coe", credits)
#     return make_dummy_student

# if u don't want to write code in the same file of unit test add fixture in conftest.py it will automatically run the file when u test the main file 


def test_student_get_age(dummy_student):
    dummy_student_age = (datetime.now() - dummy_student.dob).days // 365
    assert dummy_student.get_age() == dummy_student_age

def test_student_get_credits(dummy_student) :
    assert dummy_student.get_credits() == 20 

def test_get_topper(multiple_dummy_student) :
    students = [
        multiple_dummy_student("ram", 21),
        multiple_dummy_student("shyam", 19),
        multiple_dummy_student("ravi", 22)
    ]
    topper = get_topper(students)

    assert topper == students [2]