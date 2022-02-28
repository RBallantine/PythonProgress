'''
    Ronan Ballantine
    25/02/2022
    Domain Virus Checker
    
    Program checks a list of domain URLs against the 
    virus total database using API requests. It then 
    saves the results in a CSV file.
    
    Program not completed yet
'''

import requests
import csv


results = []

with open('domain_list1.csv', mode='r') as f:

    file = csv.reader(f)
    domains = list(file)

    for domain in range(1, len(domains)):

        virus_total_url = f'https://www.virustotal.com/api/v3/domains/{domains[domain][0]}'

        headers = {
            "Accept": "application/json",
            "x-apikey": "Enter your Virus Total API key here"
        }

        response = requests.request("GET", virus_total_url, headers=headers)
        json_response = response.json()

        malicious_count = json_response["data"]['attributes']['last_analysis_stats']['malicious']

        new_result = (domains[domain][0], malicious_count)
        results.append(new_result)

csv_file = open('domain_list1_results.csv', mode='a', newline='')
csv_writer = csv.writer(csv_file, delimiter=',')
csv_writer.writerows(results)
csv_file.close()
