'''
    Ronan Ballantine
    CSV reading and writing
    23/02/2022
'''

import csv

# Creates a csv file in 'write' mode
csv_file = open('new_csv_file.csv', mode='w', newline='')

# Variable used to write to csv file
csv_writer = csv.writer(csv_file, delimiter=',')

# Write a single row
csv_writer.writerow(['ID', 'Name', 'Age', 'City', 'IP Address'])

# Write multiple rows to the file (must have the same no. of columns)
csv_writer.writerows([['1', 'John', '23', 'Dublin', '163.168.68.132'],
                      ['2', 'Ciara', '35', 'New York', '97.212.102.79'],
                      ['3', 'Tom', '43', 'Warsaw', '158.152.84.62'],
                      ['4', 'Debs', '28', 'London', '148.54.165.62'],
                      ['5', 'Rose', '52', 'Belfast', '103.65.95.26']])

# Close file when finished
csv_file.close()

# Open created csv file
with open('new_csv_file.csv') as data:

    # Read csv data
    csv_data = csv.reader(data)

    # Reformat into list of lists
    data_rows = list(csv_data)

    ip_addresses = []

    for row in data_rows:
        print(row)

        # Acquire a list of IP addresses
        ip_addresses.append(row[4])

    print('\n')
    print(*ip_addresses, sep='\n')
