import json


def create_material_dict(version=1):
    header = {}

    header["version"] = version




def write_to_json(input_dict, out_file=''):
    a = {'a':1,'b':2,'c':3}
    tojson = json.dumps(a, ensure_ascii=False)
    try:
        with open("your_json_file", "w") as fp:
            json.dump(tojson , fp)
    except IOError:
        pass

