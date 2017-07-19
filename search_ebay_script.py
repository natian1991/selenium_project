from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from sys import argv
import time


MIN_ARGV = 2
DRIVER_PATH = 1
USAGE = "usage: search_ebay_script.py <chromedriver_path>"
DRIVER_EXCEPTION_MSG = "can't open chromedriver, make sure the <chromedriver_path> is correct"
SEARCH_ELEMENT_ID = "gh-ac"


def ebay_search(chromedriver_path, product_to_search):
    """
    searching product on ebay using selenium webdriver
    on chrome browser
    :param chromedriver_path: user's chromedriver path
    :param product_to_search: the product to search
    """
    try:

        driver = webdriver.Chrome(chromedriver_path)  # open browser

    except WebDriverException:

        print(DRIVER_EXCEPTION_MSG +
              "\nyour input chromedriver_path: " + chromedriver_path +
              "\n" + USAGE)
        exit(1)

    driver.get('http://www.ebay.com')
    search_element = driver.find_element_by_id(SEARCH_ELEMENT_ID)  # find the search element
    search_element.send_keys(product_to_search)  # set in the product name
    search_element.send_keys(Keys.RETURN)  # 'hit' enter
    time.sleep(10)
    driver.close()

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
