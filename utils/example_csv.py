from .helpers import get_file_path
import csv
import json
from pathlib import Path
import os

import csv
def get_login_csv(csv_file= "data_login.csv"):
    #csv_file=get_file_path(csv_file,"data")
    csv_file = Path(__file__).parent.parent / "data" / csv_file
    #current_file = os.path.dirname(__file__)
    #csv_file = os.path.join(current_file, "..","data",csv_file)
    #csv_file = os.path.abspath(csv_file)
    casos = []
    with open(csv_file, newline="" ) as h:
        read = csv.DictReader(h)
        for i in read:
            username = i['username']
            password = i['password']
            login_example = i["login_example"].lower() =="true"
            casos.append((username, password,login_example))
    return casos

def get_login_json(json_file="data_login.json"):
    json_file = Path(__file__).parent.parent / "data" / json_file
    casos = []
    with open(json_file) as j:
        datos = json.load(j)
        for i in datos:
            username = i['username']
            password = i['password']
            login_example = i["login_example"]
            casos.append((username, password, login_example))
    return casos