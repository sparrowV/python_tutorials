import csv

f = open("posts.csv","r")
output_f = open("output.csv","w",newline='')
reader = csv.reader(f)
writer = csv.writer(output_f,delimiter = "?")
for row in reader:
    print(row)
    writer.writerow(row)


f.close()