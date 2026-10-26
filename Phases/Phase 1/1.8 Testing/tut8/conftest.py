import pytest
from tut8 import Student
from datetime import datetime

# below 1 funtion is for test_tut8.py
@pytest.fixture(params=[21,19], ids = ["eligible","ineligible"]) # paramterized fixtures  
def dummy_student(request):
    return Student("nikhil", datetime(2000, 1, 1), "coe",request.param) # request.param will call the parameter value 1 by 1

@pytest.fixture # below function gets multiple list of students which relays on fixture factory
def make_dummy_student() : 
    def _make_dummy_student (name, credits):
        return Student(name, datetime(2000, 1, 1), "coe", credits)
    return _make_dummy_student
