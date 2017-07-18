from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from sys import argv
import time
from selenium.common.exceptions import WebDriverException

MIN_ARGV = 2
DRIVER_PATH = 1
USAGE = "usage: search_ebay_script.py <chromedriver_path>"
DRIVER_EXCEPTION_MSG = "can't open chromedriver, make sure the <chromedriver_path> is correct"
SEARCH_ELEMENT_ID = "gh-ac"


def ebay_search(chromedriver_path, element_to_search):
    try:
        driver = webdriver.Chrome(chromedriver_path)
    except WebDriverException:
        print(DRIVER_EXCEPTION_MSG +
              "\nyour input chromedriver_path: " + chromedriver_path +
              "\n" + USAGE)
        exit(1)

    driver.get('http://www.ebay.com')
    search_element = driver.find_element_by_id(SEARCH_ELEMENT_ID)
    search_element.send_keys(element_to_search)
    search_element.send_keys(Keys.RETURN)
    time.sleep(10)
    driver.close()


# 'C:\Program Files\chromeDriver\chromedriver'

if __name__ == "__main__":
    if len(argv) > MIN_ARGV:
        # if chrome driver path includes white spaces
        chromedriver_path = " ".join(argv[1:len(argv)])
    elif len(argv) < MIN_ARGV:
        print("chromedriver path is needed\n" + USAGE)
        exit(1)
    else:
        chromedriver_path = argv[DRIVER_PATH]

    ebay_search(chromedriver_path, "Fujifilm X-T2")
