import argparse
import json
import csv
import os
import sys

parser = argparse.ArgumentParser()
parser.add_argument(
    "--filename",
    type=str,
    required=True
)

json_filepath = parser.parse_args().filename
csv_filepath = json_filepath.replace(".json", ".csv")

if not os.path.isfile(os.path.join("./", json_filepath)): 
    sys.exit("Файла не существует")
elif not json_filepath.endswith(".json"):
    sys.exit("Файл должен быть json")

with open(json_filepath, "rb") as f:
    data = json.load(f)

with open(csv_filepath, "w+", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)