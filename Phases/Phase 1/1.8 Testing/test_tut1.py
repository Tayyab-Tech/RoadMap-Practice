from tut1 import add

def test_add(): # if u want to test with pytest test_ must be the starting name of ur testing function
    assert add(1,3) == 4

def test_add_str():
    assert add("a", "b") == "ab"

class TestSample: # Test is the prefix for testing if we don't enter this class will not bi in tested queue
    def test_add_num(self):
        assert add(1, 2) == 3

    def test_add_str(self):
        assert add("a", "b") == "ab"
