#from GetVideos import links

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import json

service = Service(executable_path="/Users/aadit/GoogleSuperTimelineScrapper/chromedriver")
driver = webdriver.Chrome(service=service)


def get_all_comments(uri):
    print("\n" + uri + "\n")
    driver.get(uri)

    WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.CLASS_NAME, "x9f619")))
    time.sleep(60)  # ToDo added a sleep statement here

    comments_list = []

    while True:
        try:
            add_button = driver.find_element(By.XPATH, ".x9f619 .xjbqb8w .x78zum5 .x168nmei .x13lgxp2 .x5pf9jr .xo71vjh .xdj266r .xat24cr ,x1n2onr6 .x1plvlek .xryxfnj .x1c4vz4f .x2lah0s .xdt5ytf .xqjyukv .x1qjc9v5 .x1oa3qoh .xl56j7k")
            add_button.click()
        except EC:
            break

    element = driver.find_elements(By.CLASS_NAME, "xt0psk2")

    for el in element:
        text = el.text
        print(text)
        comments_list.append(text)

    return comments_list


all_comments = []

links = ["https://www.instagram.com/coreyrforrester/reel/Cq8WzSBNsuR/",
         "https://www.instagram.com/p/CqoNMPLA2KD/?locale=en_GB&hl=en",
         "https://www.instagram.com/reel/CqqjVy2pwpY/",]

for link in links:
    comments = get_all_comments(link)
    all_comments.append(comments)

driver.quit()

with open("output.json", 'w') as f:
    json.dump(all_comments, f, indent=4)