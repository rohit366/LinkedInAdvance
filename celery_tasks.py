from celery_app import celery

import time, random, os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from os.path import join, dirname
from dotenv import load_dotenv

# Load variables from .env
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

@celery.task(name='LinkedIn Advance.celery_tasks.send_async_message')
def send_async_message(url, messagetype, subject, message):
    """Background task to send a scheduled LinkedIn Message / InMail."""
    # Enable headless Chrome
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')

    browser = webdriver.Chrome("/mnt/c/Users/Lim/Anaconda2/chromedriver.exe", chrome_options=options)
    browser.get("https://linkedin.com/uas/login")

    emailElement = browser.find_element_by_id("session_key-login")
    emailElement.send_keys(os.getenv("EMAIL"))
    passElement = browser.find_element_by_id("session_password-login")
    passElement.send_keys(os.getenv("PASSWORD"))
    passElement.submit()

    time.sleep(random.uniform(15.9,20.9))

    browser.get(url)

    time.sleep(random.uniform(15.9,20.9))

    if messagetype == "message":
        messageButton = browser.find_element_by_css_selector('.pv-s-profile-actions')
        messageButton.click()

        time.sleep(random.uniform(5.9,8.9))

        messageText = browser.find_element_by_xpath('//*[@class="ember-text-area msg-messaging-form__message Sans-15px-black-85% ember-view"]')
        messageText.send_keys(message)

        time.sleep(random.uniform(5.9,8.9))

        submitButton = browser.find_element_by_css_selector('.msg-messaging-form__send-button')
        submitButton.click()

    elif messagetype == "inmail":
        moreButton = browser.find_element_by_css_selector('.pv-s-profile-actions__overflow-toggle')
        moreButton.click()

        time.sleep(random.uniform(5.9,8.9))

        sendInMailButton = browser.find_element_by_css_selector('.pv-s-profile-actions--send-in-mail')
        sendInMailButton.click()

        time.sleep(random.uniform(5.9,8.9))

        subjectText = browser.find_element_by_xpath('//*[@class="ember-text-field msg-inmail-compose-widget__subject ember-view"]')
        subjectText.send_keys(subject)

        messageText = browser.find_element_by_xpath('//*[@class="ember-text-area msg-messaging-form__message Sans-15px-black-85% ember-view"]')
        messageText.send_keys(message)

        time.sleep(random.uniform(5.9,8.9))

        submitButton = browser.find_element_by_css_selector('.msg-messaging-form__send-button')
        submitButton.click()

    browser.close()
