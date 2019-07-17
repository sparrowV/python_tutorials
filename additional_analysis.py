import csv


def computeNum(row):
    counter = -1
    for elem in row:
        if (elem != ""):
            counter += 1
    return counter

def countRowForMost(f,feature):
    reader = csv.reader(f)
    result = 0
    i = 0
    properties = []
    for row in reader:


        counter = 0
        contains = False

        for j in range(len(row)):
            if (i == 0):
                properties.append(row[j])
            else:
                elem = row[j]

                if(elem != "" and properties[j] == feature):
                    contains = True

                if(elem != ""):
                    counter+=1

        if(counter ==2 and  contains):
            result+=1

        i+=1
    f.seek(0)
    return result
def parse(f):
    result = {}
    total_rows = -1
    reader = csv.reader(f)
    i = 0
    properties = []
    for row in reader:
        total_rows+=1
        temp = []

        elem_count = computeNum(row)

        if (elem_count <= 0):
            continue

        temp_properties = ""
        for j in range(0, len(row)):
            elem = row[j]
            # print(elem,"elem")
            if (i == 0):
                properties.append(elem)
            else:
                if (elem != "" and j!=0):
                    if(properties[j] in result):
                        result[properties[j]]+=1
                    else:
                        result[properties[j]] = 1

        i += 1
    f.seek(0)
    return result,total_rows

def validate(feature,temp_result,sorted_values):
    for elem in temp_result:
        if(sorted_values.index(feature) < sorted_values.index(elem)):
            return False
    return True

def getCountForFeature(f,feature,sorted_values):
    i = 0
    reader = csv.reader(f)
    properties = []
    result = 0
    for row in reader:
        temp = []

        elem_count = computeNum(row)

        if (elem_count <= 0):
            continue

        temp_result = []
        for j in range(0, len(row)):
            elem = row[j]
            # print(elem,"elem")
            if (i == 0):
                properties.append(elem)
            else:
                if (elem != "" and j != 0):
                    temp_result.append(properties[j])
        i+=1
        if(feature in temp_result and  validate(feature,temp_result,sorted_values) ):
            result+=1
    return result

def write_in_file(output,sorted_values,num_count_for_most,f,total_rows,sorted_list):
    per = int(num_count_for_most/total_rows*100)
    output.write(sorted_values[0]+"("+str(sorted_list[0][1])+")"+": +"+str(num_count_for_most)+" = "+str(num_count_for_most)+"/"+str(per)+"%")
    output.write("\n")
    previous_count = num_count_for_most
    str_for_other = ""
    i = 1
    for feature in sorted_values[1:]:
        count = getCountForFeature(f,feature,sorted_values)
        f.seek(0)
        percent = int((count + previous_count)/total_rows * 100)
        if(feature != "Other"):
            output.write(feature+"("+str(sorted_list[i][1])+") "+  " : +"+str(count)+" = "+str(count+previous_count)+"/"+str(percent)+"%")
            output.write("\n")
            previous_count += count
        else:
            str_for_other = feature+"("+str(sorted_list[i][1])+") "+": +"+str(count)+" = "+str(count+previous_count)+"/"+str(percent)+"%"

        i+=1
    # output.write(str_for_other+"\n")
    # other_total = total_rows -
    # output.write("Other"+"("+)
    output.write("[Remaining]"+ " : "+str(total_rows - previous_count)+"\n")
    output.write("\n\n")
    output.write("Total Rows: "+str(total_rows))




with open('sample_data.csv', newline='') as f:
    res ,total_rows= parse(f)
    print(res)
    reader = csv.reader(f)
    f.seek(0)
    sorted_list = sorted(res.items(), key=lambda kv: kv[1],reverse=True)
    sorted_values = list(map(lambda x:x[0],sorted_list))
    num_count_for_most = countRowForMost(f,sorted_values[0])
    with open("out.txt","w") as out:
        write_in_file(out,sorted_values,num_count_for_most,f,total_rows,sorted_list)



