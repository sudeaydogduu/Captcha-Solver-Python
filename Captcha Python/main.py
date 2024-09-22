from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import twocaptcha


def open_website(url):
    browser = webdriver.Chrome()
    browser.get(url)
    return browser


def download_captcha_image(browser, captcha_element_id, file_path):
    captcha_element = browser.find_element(By.ID, captcha_element_id)
    captcha_element.screenshot(file_path)


def get_captcha_solution(api_key, image_path):
    solver = twocaptcha.TwoCaptcha(api_key)

    try:
        result = solver.normal(image_path)
        return result['code']
    except Exception as error:
        print(f"Error solving captcha: {error}")
        return None


def process_login():
    website_url = 'WRITE_THE_URL_HERE'  # Replace with the actual URL
    captcha_image_path = 'captcha_example.jpg'
    captcha_element_id = 'capthcaLogin_IMG'
    captcha_input_id = 'capthcaLogin_TB_I'
    submit_button_class = 'dxeTextBoxSys dxeTextBox form-control loginTextStyle'

    # Fetch the API key for 2Captcha from environment variables
    api_key = os.getenv('APIKEY_2CAPTCHA', 'YOUR_API_KEY')  # Replace 'YOUR_API_KEY' with the actual key

    browser = open_website(website_url)

    download_captcha_image(browser, captcha_element_id, captcha_image_path)

    captcha_code = get_captcha_solution(api_key, captcha_image_path)


    if captcha_code:
        browser.find_element(By.ID, captcha_input_id).send_keys(captcha_code)

        submit_button = browser.find_element(By.CLASS_NAME, submit_button_class)
        submit_button.click()

        time.sleep(60)
    else:
        print("Failed to solve captcha.")


if __name__ == "__main__":
    process_login()
