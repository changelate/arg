import argparse
import json
import os.path

parser = argparse.ArgumentParser()
parser.add_argument("--key", required=True)
parser.add_argument("--value")
Namespace = parser.parse_args()
key = Namespace.key
value = Namespace.value
d = {}

with open("../result.json", mode="a") as f:
    pass

if os.path.getsize("../result.json") == 0:
    with open("../result.json", mode="w", encoding="utf-8") as f:
        json.dump(d,f)

if value != None:
    with open("../result.json", mode="r", encoding="utf-8") as f:
        a = json.load(f)
    with open("../result.json", mode="w", encoding="utf-8") as f:
        a[key] = value
        json.dump(a,f)
try:
    if key != None and value == None:
        with open("../result.json", mode="r", encoding="utf-8") as f:
            b = json.load(f)
            print(b[str(key)])
except KeyError:
    print("\n")