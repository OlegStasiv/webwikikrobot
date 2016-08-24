# coding=utf-8
import logging
import os
from pyvirtualdisplay import Display
import urllib3

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver

from wikiapi import WikiApi

urllib3.disable_warnings()
logging.captureWarnings(True)

wiki = WikiApi()
wiki = WikiApi({'locale': 'uk'})
results = wiki.find('ThinkMObiles')
article = wiki.get_article(results[0])
# article.summary
text_file = open("New.txt", "w")
text_file.write((article.content).encode('utf-8'))
text_file.close()

test1filehandle = open('Old.txt', 'r')
test2filehandle = open('New.txt', 'r')
test3filehandle = open('some_output_file.txt', 'w')
test1list = test1filehandle.readlines()
test2list = test2filehandle.readlines()
k = 1
for i, j in zip(test1list, test2list):
    if i != j:
        test3filehandle.write("Line Number:" + str(k) + ' ')
        test3filehandle.write(i.rstrip("\n") + ' ' + j)
    k = int(k)
    k = k + 1
test3filehandle.close()

try:
    if os.stat('some_output_file.txt').st_size > 0:
        print "All good"
        #display = Display(visible=1, size=(800, 600))
        #display.start()
        # chromedriver = "/home/lego/Downloads/Botter-master/chromedriver"
        # os.environ["webdriver.chrome.driver"] = chromedriver
        driver = webdriver.Chrome()
        mytitle = "ThinkMobiles — Вікіпедія"
        a = driver.get("https://uk.wikipedia.org/wiki/ThinkMobiles")
        content =  driver.title
        assert mytitle in content.encode("utf-8")
        # elem = driver.find_element_by_name("q")
        # elem.send_keys("pycon")
        # elem.send_keys(Keys.RETURN)
        # assert "No results found." not in driver.page_source
        driver.close()
        #display.stop()
    else:
        print "empty file"
except OSError:
    print "No file"
