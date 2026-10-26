from tut2 import validate_age
import pytest
def test_validate_age_valid_age():
    validate_age(10)
def test_validate_age_invalid_age():
    with pytest.raises(ValueError) as exc_info:
        validate_age(-1)
    print(str(exc_info.value))
    with pytest.raises(ValueError, match = "Age cannot be less than 0"): # if it does't match the vale of exception in the main file it return error
        validate_age(-1)
    # with pytest.raises(ValueError) as exc_info:
    #     validate_age(-1)
    # print(str(exc_info.value)) == "Age cannot be less than 0"