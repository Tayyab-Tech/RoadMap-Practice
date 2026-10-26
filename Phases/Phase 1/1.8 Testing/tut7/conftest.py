import pytest
from tut7 import Student
from datetime import datetime

@pytest.fixture(scope = "function") # custom fixtures  ---> default scope is function if needed change it to module to change actual values of main class or function 
def dummy_student():
    return Student("nikhil", datetime(2000, 1, 1), "coe",20)

@pytest.fixture # below function gets multiple list of students which relays on fixture factory
def multiple_dummy_student() : 
    def make_dummy_student (name, credits):
        return Student(name, datetime(2000, 1, 1), "coe", credits)
    return make_dummy_student
