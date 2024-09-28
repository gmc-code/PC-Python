import csv

# csv_path = 'files/afl_premiers_2000s.csv'
# csv_path2 = 'files/afl_premiers_2000s_tabbed.csv'

csv_path = 'docs/python_files/files/afl_premiers_2000s.csv'
csv_path2 = 'docs/python_files/files/afl_premiers_2000s_tabbed.csv'

with open(csv_path, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open(csv_path2, 'w', newline='') as new_file:
        fieldnames = ["Year", "Premiership team"]
        csv_writer = csv.DictWriter(new_file,
                                    fieldnames=fieldnames,
                                    delimiter='\t')
        csv_writer.writeheader()
        for line in csv_reader:
            fieldnames_dict = {key: line[key] for key in fieldnames}
            csv_writer.writerow(fieldnames_dict)
