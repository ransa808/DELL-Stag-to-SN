# DELL Service Tag to Serial Number Converter, the script depends on Dell’s website structure, and if it fails, updates to the script to align with any changes will be needed
# Author: Ran Salman

import browser_cookie3
import requests
import json
import re
import csv

# Regex pattern to match the serial number in the returned URL
pattern = r"serialnumber/(\w+)/"

# Retrieve cookies from Brave browser for the dell.com domain
print('Trying to read cookies from Chrome browser')
cookies = browser_cookie3.chrome(domain_name='dell.com')
if not cookies:
    raise RuntimeError("Cannot get Cookie Jar for Dell.com from Chrome, Please open Chrome and login to Dell https://www.dell.com/support/home/en-il")

# Base URL for Dell (not used directly in this script)
dell_url = 'https://www.dell.com/en-il/lp'


def parseSN(url):
    # Extract the serial number using the regex pattern
    match = re.search(pattern, url)
    if match:
        serial_number = match.group(1)
        return serial_number
    else:
        raise ValueError("Serial Number not found.")


def send_request(s_tag):
    # URL for the API endpoint that validates the service tag
    url = "https://www.dell.com/support/search/en-il/entryselection/ValidateEntityJSON"

    # Headers required for the request
    headers = {
        "Content-Type": "application/json; charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "Referer": "https://www.dell.com/support/home/en-il",
    }

    # Payload with the service tag and additional information
    payload = json.dumps({
        "appName": "mastheadSearch",
        "IsSevenCharTag": True,
        "Selection": s_tag
    })

    # Send the POST request to the Dell website with the cookies and headers
    response = requests.post(url, headers=headers, data=payload, cookies=cookies)
    response.raise_for_status()  # Raise an error if the request was unsuccessful

    return response.json()  # Return the JSON response


def main():
    # User input for service tags, expects a comma-separated string
    input_tags = input("Enter the service tags separated by commas (,): ")

    # Split the input string into individual service tags, stripping any extra spaces
    stags = [tag.strip() for tag in input_tags.split(',')]
    if stags == ['']:
        print("No service tags provided. Exiting.")
        return
    # List to hold results for printing and CSV export
    results = []

    # Process each service tag
    for stag in stags:
        try:
            # Send the request and parse the serial number from the response
            data = send_request(stag)
            sn = parseSN(data['LookupResults'][0]['TargetUrl'])
            results.append([stag, sn])
        except Exception as e:
            # Handle any errors, such as invalid service tags or failed requests
            print(f"An error occurred with service tag {stag}: {e}")

    # Print the results in a table format
    print("\nService Tag\t\tSerial Number")
    print("-" * 40)
    for result in results:
        print(f"{result[0]}\t\t\t{result[1]}")

    # Export the results to a CSV file
    with open('dell_serial_numbers.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Service Tag", "Serial Number"])
        writer.writerows(results)

    # Notify the user that the results have been exported
    print("\nResults have been exported to dell_serial_numbers.csv")


# Entry point of the script
if __name__ == '__main__':
    main()
