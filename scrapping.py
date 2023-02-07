from selenium import webdriver
import pandas as pd
from urllib.request import urlopen

#driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

url = "http://olympus.realpython.org/profiles/aphrodite"

page = urlopen(url)

html_bytes = page.read()
html = html_bytes.decode("utf-8")

#content = driver.page_source
#df = pd.DataFrame({'Name':name,'PhoneNumber':numberPhone,'Street':street}) 
#df.to_csv('products.csv', index=False, encoding='utf-8')
