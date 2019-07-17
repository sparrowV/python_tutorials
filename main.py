import csv
import collections

def analyzeCounts(d):
    result = {}
    total = 0
    for key1 in d:
        for elem in d[key1]:
            if(elem in result):
                result[elem]+=d[key1][elem]
            else:
                result[elem]=d[key1][elem]
            total+=d[key1][elem]

    return result,total





def write_total(counts_list,total,f):
    f.write("All")
    f.write("\n")
    print("--------------","sdsd")
    print(counts_list)
    d = counts_list
    counts_list =s = [(k, d[k]) for k in sorted(d, key=d.get, reverse=True)]

    print(counts_list)
    for key in counts_list:
        persent = int(key[1]/total*100)
        f.write(key[0]+":"+str(key[1])+"/"+str(persent)+"%")
        f.write("\n")
    f.write("Total: "+str(total)+"/100%")
    f.write("\n")
    f.write("\n")

def get_sum(category):
    total = 0
    for elem in category:
        total+=elem[1]
    return total
def writeCategories(category,header):
    f.write(header)
    f.write("\n")
    total = get_sum(category)
    for key in category:
        persent = int(key[1] / total * 100)
        f.write(key[0] + ":" + str(key[1]) + "/" + str(persent) + "%")
        f.write("\n")
    f.write("Total: "+str(total)+"/100%")
    f.write("\n")
    f.write("\n")





def computeNum(row):
    counter = -1
    for elem in row:
        if (elem != ""):
            counter += 1
    return counter


def num_to_text(num):
    if (num == 1):
        return "one"
    if (num == 2):
        return "two"
    if (num == 3):
        return "three"
    if (num == 4):
        return "four"
    if (num == 5):
        return "five"
    if (num == 6):
        return "six"
    if (num == 7):
        return "seven"
    if (num == 8):
        return "eight"
    if (num == 9):
        return "nine"


def parse():
    result = {}
    with open('data.csv', newline='') as f:
        reader = csv.reader(f)
        i = 0
        properties = []
        for row in reader:
            temp = []

            elem_count = computeNum(row)

            if (elem_count <= 0):
                continue
            elem_count = num_to_text(elem_count)
            temp_properties = ""
            for j in range(0, len(row)):
                elem = row[j]
                # print(elem,"elem")
                if (i == 0):
                    properties.append(elem)
                else:
                    if (elem != "" and j!=0):
                        temp_properties+=properties[j]+","


            if(temp_properties == ""):
                i += 1
                continue
            if (elem_count in result):

                if (temp_properties in result[elem_count]):
                    result[elem_count][temp_properties] += 1
                else:
                    result[elem_count][temp_properties] = 1
            else:
                result[elem_count] = {}
                result[elem_count][temp_properties] = 1
            print(temp)
            i += 1
        print(properties)
    print(result)
    return result

d = parse()
counts_list,total = analyzeCounts(d)
print("-----------------------------------")
print(counts_list)
print(d)
with open("output.txt","w") as f:
    write_total(counts_list,total,f)
    print("herere",d)
    for elem in d:

        sorted_list = s = [(k, d[elem][k]) for k in sorted(d[elem], key=d[elem].get, reverse=True)]
        print(elem)
        writeCategories(sorted_list,elem)