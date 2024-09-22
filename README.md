# Captcha Solver Python
 This Python application automates login to a CAPTCHA-protected website using Selenium for browser automation and 2Captcha for solving CAPTCHAs. It captures the CAPTCHA image, retrieves the solution, and submits the login form automatically.
Features
Automatically navigates to the specified URL.
Captures and solves the CAPTCHA image.
Submits the login form with the retrieved solution.

Requirements
Python 3.x
Selenium
2Captcha Python Client
Chrome WebDriver (make sure it matches your Chrome version)

You need to fill in lines 31 and 38 before running the program.
Here's the part of the code where you need to enter the URL and your API key:

# Define constants
website_url = 'WRITE_THE_URL_HERE'  # Replace with the actual URL
api_key = os.getenv('APIKEY_2CAPTCHA', 'YOUR_API_KEY')  # Replace with your actual key
