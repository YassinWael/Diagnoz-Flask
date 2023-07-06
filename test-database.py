#used for sending test request to learn-more , 200 for successful and 500 for failure
from ini_database import Diseases_dict
from icecream import ic
import requests
broken = []
for i in Diseases_dict:
    req = str(requests.get(f'http://127.0.0.1:5000/learnmore/{i}'))
    if '500' in req:
        broken.append(i)
    else:
        print(req)

ic(broken)