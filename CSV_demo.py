import csv

with open('utilities/loanapp.csv', 'r') as csv_file:
    csvReader = csv.reader(csv_file, delimiter=',')
    names = []
    status = []
    for row in csvReader:
        print(row)
        names.append(row[0])
        status.append(row[1])
print(names)
print(status)
element_index = names.index('Jim')
print(f'The {names[element_index]} loan status is: {status[element_index]}')

with open('utilities/loanapp.csv', 'a', newline='') as csv_file:
    csvWriter = csv.writer(csv_file)
    csvWriter.writerow(['Maxim', 'Approved'])

with open('utilities/loanapp.csv', 'r') as csv_file:
    csvReader = csv.reader(csv_file, delimiter=',')

    for row in csvReader:
        print(row)
