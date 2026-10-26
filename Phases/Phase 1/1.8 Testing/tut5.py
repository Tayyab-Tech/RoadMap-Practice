import json

def save_dict(d,filepath):
    json.dump(d,open(filepath,'w'))
    print("Saved")