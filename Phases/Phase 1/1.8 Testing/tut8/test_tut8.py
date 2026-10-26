
from datetime import datetime
# from tut7 import get_topper
import pytest
from tut8 import Student
from datetime import datetime
from tut8 import is_eligible_for_degree

# fixtures written in conftest.py 

def test_student_get_age(dummy_student):
    dummy_student_age = (datetime.now() - dummy_student.dob).days // 365
    assert dummy_student.get_age() == dummy_student_age

# def test_student_is_eligible_for_degree_true(make_dummy_student) :
#     assert is_eligible_for_degree(make_dummy_student("sam", 19)) is False

# def test_student_is_eligible_for_degree_false(make_dummy_student) :
#     assert is_eligible_for_degree(make_dummy_student("sam", 21)) is True

# except this use parametrized marker 

@pytest.mark.parametrize("credit,expected", [(21,True),(19,False)])
def test_student_is_eligible_for_degree(make_dummy_student,credit,expected) :
    assert is_eligible_for_degree(make_dummy_student("sam", credit)) is expected
