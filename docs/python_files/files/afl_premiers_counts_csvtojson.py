# see: https://en.wikipedia.org/wiki/VFL/AFL_premiership_and_grand_final_statistics for data for csv

import csv
import json


def csv_to_json_file(csv_file_path, json_file_path, json_mainkey):
    json_array = []
    with open(csv_file_path, 'r', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            json_array.append(row)

    json_dict = {json_mainkey: json_array}
    with open(json_file_path, 'w', encoding='utf-8') as jsonf:
        json_str= json.dumps(json_dict, indent=4)
        jsonf.write(json_str)


# csv_path = "files/afl_premiers_counts.csv"
# json_path = "files/afl_premiers_counts.json"

csv_path = "docs/python_files/files/afl_premiers_counts.csv"
json_path = "docs/python_files/files/afl_premiers_counts.json"
json_mainkey = "premiers"
csv_to_json_file(csv_path, json_path, json_mainkey)
