import csv

with open('sample_data.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)