'''
    Ronan Ballantine
    CSV puzzle
    23/02/2022
    
    Task: Grab the Google Drive link from the .csv file
    The .csv file can be found in the PythonProgress repo
'''

import csv

with open('csv_puzzle.csv') as f:

    file = csv.reader(f)

    # Format file as a list
    contents = list(file)

    # Used to view data
    # print(*contents, sep='\n')

    hidden_url = []

    # Append the character in each row
    for row, char in enumerate(contents):
        hidden_url.append(char[row])

# Join list of characters to create a string
hidden_url = ''.join(hidden_url)

print(hidden_url)
