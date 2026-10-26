import json
import os
from tut5 import save_dict

def test_save_dict(tmpdir,capsys): # tmpdir is a fixture method which creates sample or temparory directory
    filepath = os.path.join(tmpdir,"test.json")
    d = {"a":1,"b":2}
    save_dict(d,filepath)
    assert json.load(open(filepath,"r")) == d
    assert capsys.readouterr().out == "Saved\n"