# see: https://en.wikipedia.org/wiki/VFL/AFL_premiership_and_grand_final_statistics for data for csv

import json

# json_path = "files/afl_premiers_counts.json"
# json_path2 = "files/afl_premiers_top.json"

json_path = "docs/python_files/files/afl_premiers_counts.json"
json_path2 = "docs/python_files/files/afl_premiers_top.json"

data_list = []
keys_to_keep = ["Club", "Premierships Total"]
mainkey = "premiers"
with open(json_path, encoding='utf-8') as f:
    json_data = json.load(f)
    # append data
    for entry in json_data[mainkey]:
        if int(entry["Premierships Total"]) >=13:
            entry_dict = {key: entry[key] for key in keys_to_keep}
            data_list.append(entry_dict)

data = {mainkey: data_list}
# Open a json writer, and use the json.dumps() function to dump data
with open(json_path2, 'w', encoding='utf-8') as f2:
    json.dump(data, f2, indent=4)
