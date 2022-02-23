'''
    Ronan Ballantine
    23/02/2022

    Exercise tests shutil, unzipping files,
    os module directory walk through and locating
    a phone number pattern using regex.

    The zipped folder containing the instructions, sub folders, and text files can be found in the PythonProgress repository
'''

import shutil
import re
import os

shutil.unpack_archive('C:\\Users\\Ronan\\Downloads\\unzip_me_for_instructions.zip')

with open('extracted_content\\Instructions.txt') as f:
    content = f.read()
    print(content)

'''\n
This is the printed instructions from above:
Good work on unzipping the file!
You should now see 5 folders, each with a lot of random .txt files.
Within one of these text files is a telephone number formated ###-###-#### 
Use the Python os module and regular expressions to iterate through each file, open it, and search for a telephone number.
Good luck!'''

# Phone number digit pattern
pattern = r'\d{3}-\d{3}-\d{4}'


# Searches for the number pattern within the files contents
def locate_number(file_path, search_pattern):
    with open(file_path, 'r') as f:
        text = f.read()

        if re.search(search_pattern, text):
            return re.search(search_pattern, text)
        else:
            return ''


results = []

# Walks through the files within the extracted content folder
for folder, sub_folders, files in os.walk(os.getcwd() + '\\extracted_content'):

    for file in files:
        full_path = folder + '\\' + file
        results.append((locate_number(full_path, pattern), file))

# Prints the located number pattern and the name of the file it was found in
for content, file in results:
    if content != '':
        print(f'\n {content.group()} was found in file {file}')
