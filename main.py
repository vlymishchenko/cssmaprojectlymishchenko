import time
import HTMLParser
import logging

import selenium
from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support import expected_conditions as ec

logging.basicConfig(level=logging.INFO, filename="py_log.txt",filemode="a",
                    format="%(asctime)s %(levelname)s %(message)s")

options = Options()

options.add_experimental_option(
    'prefs',
    {
        # 'profile.managed_default_content_settings.javascript': 2,
        'profile.managed_default_content_settings.images': 2,
        'profile.managed_default_content_settings.mixed_script': 2,
        'profile.managed_default_content_settings.media_stream': 2,
        'profile.managed_default_content_settings.stylesheets': 2
    }
)
options.page_load_strategy = 'eager'
Browser = webdriver.Chrome(options=options)

start = time.time()
startresult = time.time()

# Browser = webdriver.Chrome()
Browser.get('https://stepn-market.guide/#result')

stop = time.time()
logging.info(f'startbrowser {stop-start}')

start = time.time()

SearchButton = Browser.find_elements(By.CSS_SELECTOR, 'button')

stop = time.time()
logging.info(f'searchbutton {stop-start}')

start = time.time()

SearchButton[-1].click()

stop = time.time()
logging.info(f'clickbutton {stop-start}')

time.sleep(5)

start = time.time()

with open('result.html', 'w', encoding='utf-8') as file:
    file.write(Browser.page_source)

pageNum = HTMLParser.searchForLastPage('result.html')

stop = time.time()
logging.info(f'createresultfile {stop-start}')


for i in range(pageNum):
    start = time.time()

    HTMLParser.HTMLParser('result.html')

    stop = time.time()
    logging.info(f'parser{i + 1}page{stop - start}')

    start = time.time()

    SearchButton = Browser.find_element(By.CSS_SELECTOR, '[aria-label="Next »"]')

    stop = time.time()
    logging.info(f'searchnextbutton {stop - start}')

    start = time.time()

    SearchButton.click()

    stop = time.time()
    logging.info(f'clicknextbutton {stop - start}')

    time.sleep(5)

    start = time.time()

    with open('result.html', 'w', encoding='utf-8') as file:
        file.write(Browser.page_source)
    print(''f'Collected information from {i+1} pages from {pageNum}. {pageNum - i - 1} pages left''')
    logging.info(f'Collected information from {i+1} pages from {pageNum}. {pageNum - i - 1} pages left')

    stop = time.time()
    logging.info(f'finalfor {i} page {stop - start}')

    # if i == 1:
    #     break

stopresult = time.time()
logging.info(f'finishparswork {stopresult-startresult}')

Browser.close()
Browser.quit()
