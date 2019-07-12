from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from bs4 import BeautifulSoup
from urllib.error import URLError
import urllib.request
import argparse
import sys

def parse_cli_args(args):
        parser = argparse.ArgumentParser()
        parser.add_argument('-u', '--url', description='URL de acesso', action='store', required=True)
        arg_parsed = parser.parse_args(args)
        return arg_parsed


def getUrlList(url):
    urllist=[]
    response = urllib.request.urlopen(url)
    try:
        html = response.read()    
    except ValueError:
        print('Invalid URL', file=sys.stderr)
        sys.exit(1)
    except URLError:
        print('URL not found', file=sys.stderr)
        sys.exit(1)

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

if __name__ == "__main__":
        cli_args = parse_cli_args(sys.argv[1:])
        url = cli_args.url
        print(autolike(getUrlList(url)))
        # print(autolike(getUrlList('https://www.youtube.com/channel/UC3RtgbslbAvE-5FFBkSgpig/videos')))