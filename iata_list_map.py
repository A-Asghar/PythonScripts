import csv


# myDict = {}
# line = 0
# with open('codes.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     for row in csv_reader:
#     	print(f'"{row[0]}": "{row[1]}",')

# print(myDict)



with open('iata.csv', encoding="utf8") as csv_file1:
    csv_reader1 = csv.reader(csv_file1, delimiter=',')
    for row in csv_reader1:
    	line +=1
    	print(f'"{row[3]}": ["{row[0]}","{row[2]}","{row[1]}","{myDict[row[1]]}"]')

print(line, ' lines processed')