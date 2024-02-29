SQLiFinder
SQLiFinder is a simple tool designed to detect SQL injection vulnerabilities in a given website. The tool utilizes a combination of web crawling and payload injection to identify potential vulnerabilities. This repository consists of four main components:

main.py: The main script that launches the graphical user interface (GUI) for SQLiFinder.

sqlifinder.py: The core functionality for scanning SQL injection vulnerabilities. It accepts a domain as input and scans for potential vulnerabilities, displaying the results in the GUI.

crawler.py: A simple web crawler that extracts links from a given webpage.

extractor.py: An extractor module that identifies potential SQL injection points in crawled URLs.

requester.py: A module responsible for making HTTP requests to the specified URLs.

How to Use SQLiFinder
Prerequisites
Python 3
Required Python packages (install using pip install -r requirements.txt)
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/SQLiFinder.git
cd SQLiFinder
Install the required packages:

bash
Copy code
pip install -r requirements.txt
Running SQLiFinder
Execute the main script:

bash
Copy code
python main.py
The GUI will appear, prompting you to enter the target domain and choose whether to include subdomains in the scan.

Click the "Start Scan" button to initiate the scan.

The results will be displayed in the scrolled text area, indicating whether SQL injection vulnerabilities were found.

Payloads
The tool uses a set of predefined payloads stored in payloads.txt. You can customize or expand this file with additional payloads as needed.
