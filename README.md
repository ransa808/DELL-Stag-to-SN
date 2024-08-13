# DELL Service Tag to Serial Number Converter

This script allows you to convert Dell service tags to their corresponding serial numbers by querying Dell's support website. Please note that this script is dependent on Dell’s website structure, and any changes to the website might require updates to the script.

## Author
Ran Salman

## Requirements

The script requires Python 3 and the following Python libraries:

- `browser_cookie3`: To retrieve cookies from your browser for Dell's website.
- `requests`: To make HTTP requests to the Dell website.
- `re`: For regular expression operations (included in Python’s standard library).
- `json`: For handling JSON data (included in Python’s standard library).
- `csv`: For exporting the results to a CSV file (included in Python’s standard library).

### Installing Dependencies

You can install the required dependencies using pip:

```bash
pip install browser_cookie3 requests
```

How to Run the Script
---------------------

1.  **Ensure Browser is Logged In:**
    
    *   Make sure you are logged into the Dell support website in your Chrome browser. The script relies on cookies from your browser session to access the Dell API.
        
2.  Run the Script:
       
    *   Open a terminal or command prompt in the directory where the script is saved.
        
    *   Run the script with Python:
     ```bash
      python dell_service_tag_to_serial.py
    ```
       OR
     ```bash
      python3 dell_service_tag_to_serial.py
    ```
3.  **Input Service Tags:**
    
    *   When prompted, enter the Dell service tags separated by commas (e.g. ABC1234, DEF5678, GHI9012).
        
    *   The script will fetch the corresponding serial numbers.
        
4.  **Output:**
    
    *   The results will be displayed in a table format in the terminal.
        
    *   The results will also be exported to a CSV file named dell\_serial\_numbers.csv in the same directory as the script.
        

Troubleshooting
---------------

*   **Cookies Not Found:**
    
    *   If the script cannot retrieve the cookies from Chrome, ensure that you are logged into the Dell support website and try running the script again.
        
*   **Script Fails Due to Website Changes:**
    
    *   This script depends on the current structure of Dell's website. If the website changes, the script may need to be updated. Check the regular expression for extracting the serial number or the API endpoint URL if issues arise.
        

License
-------

This project is open source and available under the MIT License.