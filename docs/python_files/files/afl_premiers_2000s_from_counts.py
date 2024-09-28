import csv

# Function to extract premiership and runner-up data from 2000 onwards
def extract_grand_final_data(data):
    extracted_data = {}
    for entry in data:
        premiership_total = int(entry["Premierships Total"])
        runner_up_total = int(entry["Runners-up Total"])
        premiership_years = entry["Premierships Season(s)"].split(", ")
        runner_up_years = entry["Runners-up Season(s)"].split(", ")
        
        if premiership_total > 0:
            for year in premiership_years:
                if int(year) >= 2000:
                    index = int(year) - 2000
                    if index not in extracted_data:
                        extracted_data[index] = {
                            "Year": year,
                            "Premiership team": entry["Club"],
                            "Runner-up": None
                        }
                    else:
                        extracted_data[index]["Premiership team"] = entry["Club"]
        
        if runner_up_total > 0:
            for year in runner_up_years:
                if int(year) >= 2000:
                    index = int(year) - 2000
                    if index not in extracted_data:
                        extracted_data[index] = {
                            "Year": year,
                            "Premiership team": None,
                            "Runner-up": entry["Club"]
                        }
                    else:
                        extracted_data[index]["Runner-up"] = entry["Club"]
    return extracted_data

csv_path = 'docs/python_files/files/afl_premiers_counts.csv'
csv_path2 = 'docs/python_files/files/afl_premiers_2000s.csv'

with open(csv_path, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    extracted_data = extract_grand_final_data(csv_reader)
    
    # Sort the extracted data by Index in descending order
    sorted_extracted_data = dict(sorted(extracted_data.items(), key=lambda item: item[0], reverse=True))
    
    with open(csv_path2, 'w', newline='') as new_file:
        fieldnames = ["Index", "Year", "Premiership team", "Runner-up"]
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=',')
        csv_writer.writeheader()
        for index, data in sorted_extracted_data.items():
            row = {"Index": index, "Year": data["Year"], "Premiership team": data["Premiership team"], "Runner-up": data["Runner-up"]}
            csv_writer.writerow(row)

print("CSV file has been created successfully.")
