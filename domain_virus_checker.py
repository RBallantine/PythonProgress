'''
    Ronan Ballantine
    25/02/2022
    Domain Virus Checker

    Program checks a list of domain URLs against the
    virus total database using API requests. It retrieves
    a total malicious vote count and the IPv4 address
    of the domain. The results are then saved in a CSV file.

    Program currently being updated
'''

import requests
import csv


results = []

# Opens a CSV file containing a list of domain names
with open('domain_list1.csv', mode='r') as f:

    file = csv.reader(f)
    domains = list(file)

    # Requests domain information from Virus Total, for each domain on the list
    for domain in range(0, len(domains)):

        virus_total_url = f'https://www.virustotal.com/api/v3/domains/{domains[domain][0]}'

        headers = {
            "Accept": "application/json",
            "x-apikey": "ENTER YOUR API KEY HERE"
        }

        response = requests.request("GET", virus_total_url, headers=headers)
        json_response = response.json()

        # Stores the total malicous votes count for the domain
        malicious_count = json_response['data']['attributes']['last_analysis_stats']['malicious']

        # Searches the response information for the domains A record IPv4 Address (Only stores one address for now)
        for lists in range(0, len(json_response['data']['attributes']['last_dns_records'])):
            if json_response['data']['attributes']['last_dns_records'][lists]['type'] == 'A':
                ipv4_address = json_response['data']['attributes']['last_dns_records'][lists]['value']

        # Creates a tuple containing the domain name, malicious count and IPv4 address
        new_result = (domains[domain][0], malicious_count, ipv4_address)
        results.append(new_result)

# Creates a new CSV file and writes column headings and the stored data
csv_file = open('domain_list1_results.csv', mode='w', newline='')
csv_writer = csv.writer(csv_file, delimiter=',')
csv_writer.writerows([['Domain', 'Malicious Count', 'IPv4 Address']])
csv_writer.writerows(results)
csv_file.close()
