# Getting a list of all the links from a platform (Instagram) on a certain topic between a certain timeframe'
# Use google search engineering tools to find links (Instagram posts)
# Use selenium (Head automation browser) to get the top 200 links

# importing selenium and all its liabilities
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv


def get_all_links(uri):
    # initializing the server and preparing the browser
    service = Service(executable_path="/Users/aadit/GoogleSuperTimelineScrapper/chromedriver")  # locating chromedriver in the repo to execute the server
    driver = webdriver.Chrome(service=service)

    driver.get(uri)

    # waiting for a specific HTML element on the webpage to laod before performing further tasks
    WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.CLASS_NAME, "eqAnXb")))  # container on the webpage that holds all links

    # for i in range(5):
    #     driver.execute_script("window.scrollBy(0, 1000);")
    #     time.sleep(1)  # ToDo see extra sleep statement
    #

    linkList = []
    flag = 0

    while True:
        element = driver.find_elements(By.CLASS_NAME, "zReHs")  # class name of all DIVs containing links
        len_el = len(element)
        print(len(element))

        pin = 0

        # extracting the links from the html on the webpage
        for eli in element:
            link = eli.get_attribute("href")
            linkList.append(link)  # adding all links to this list
            print(link)  # ToDo view testing print statement

            # Each google page has approx 10 links.
            # So this code is mostly useless. But still helpful to prevent bot detection
            pin += 1
            if pin > 20:
                break

        # Setting up a try statement in case element not found causes a crash
        try:
            # finding the next page button on the google page and clicking it after scrapping all the links
            next_button = driver.find_element(By.CLASS_NAME, "LLNLxf")
            next_page = next_button.get_attribute("href")
            driver.get(next_page)

            # stopping the code after reaching page 20. P.S. getting 210 links from each search (approx)
            # another measure to prevent bot recognition by google
            flag += 1
            if flag >= 4:
                break

            continue

        except EC:
            # exiting if no more "next pages" are found. AKA we have already scrapped all links on this issue
            break

    # Terminating our server
    driver.quit()

    return linkList


# # search varible contains the google URL (URL data includes: site, search words, hashtags, date-before, date-after
# search = "https://www.google.com/search?q=site:tiktok.com+%22%23budlight%22+after:2023-04-01+before:2023-04-14&sca_esv=a99f4f1e2fb679d4&sxsrf=AHTn8zps5n1EF4Qr5vp3ukRupttIkcuMpA:1745596694597&ei=FrELaJeeJJKtptQP7suC0AM&start=0&sa=N&sstk=Af40H4U_QC2PCgjPmOZRD3KgtmOCqmk6HPw0i22ExDqKrN6XfP3NzSRTK-e7ZehR5VYdvCXr_8hbS_BEhskbzHiCkzkikPwl0rSLGZn4-lqir8hAUhMhMSUwsIV2OnGBm_Ce&ved=2ahUKEwiXgZy3xvOMAxWSlokEHe6lADo4ChDx0wN6BAgJEAI&biw=1440&bih=785&dpr=2"
#
# # running the method
# links = get_all_links(search)
#
# print(len(links))
# print()
# print(links)

# # adding the links into a csv file
# csv_file = "allLinks.csv"
#
# with open(csv_file, mode='w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(links)
#

