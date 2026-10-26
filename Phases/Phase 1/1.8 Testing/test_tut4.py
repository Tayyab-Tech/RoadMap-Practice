# parameterized marking in which we can perform multiple testing in 1 fucntion like below 
import pytest
from tut4 import add


@pytest.mark.parametrize("a,b,c", 
                            [(1,2,3),("a","b","ab"),([1,2],[3],[1,2,3])] ,
                            ids = ["num","str","list"])
def test_add(a,b,c):
    assert add(a,b) == c