import pandas as pd
import json


with open(r"./SBIN_daily_data.json", "r") as f:
    data = json.loads(f)

    

print(data)