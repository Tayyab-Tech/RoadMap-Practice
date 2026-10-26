from tut3 import add
import pytest
import sys

@pytest.mark.skip(reason="Just skip")
def test_add_num() :
    assert add(1, 2) == 3

@pytest.mark.skipif(sys.version_info>(3,7),reason="Version above 3.7")
def test_add_str():
    assert add("a", "b") == "ab"

@pytest.mark.xfail(sys.platform=="linux", reason="don't run on linux")
def test_add_list() :
    assert add([1], [2]) == [1,2]
    raise Exception()