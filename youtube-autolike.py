from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import urllib.request
from bs4 import BeautifulSoup

def getUrlList(url):
    urllist=[]
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
        urllist.append('https://www.youtube.com' + vid['href'])
    return urllist

def autolike(urlList):
    driver = webdriver.Chrome()
    for url in urlList:
        youtube = driver.get(url)
        sleep(5)
        button = driver.find_element_by_xpath("//*[@id='top-level-buttons']/ytd-toggle-button-renderer[1]/a")
        ActionChains(driver).move_to_element(button).click(button).perform()

print(autolike(getUrlList('https://www.youtube.com/channel/UC3RtgbslbAvE-5FFBkSgpig/videos')))
