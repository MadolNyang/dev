from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests
import re

def get_urls(word):
    url = f"https://hanja.dict.naver.com/#/search?query={word}"
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    urls = []
    for link in soup.select('a.hanja_link'):
        href = link['href']
        if 'entry/ccko' in href:
            urls.append(link['href'])
    driver.quit()
    return urls

def get_img_url(link):
    url = f"https://hanja.dict.naver.com/{link}"
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    urls = []
    for link in soup.find_all(src=re.compile(r"^https://ssl.pstatic.net/dicimg/cckodict/aniSVG")):
        urls.append(link.attrs['src'])
    driver.quit()
    return urls

def get_img_file(link):

# word = input("단어를 입력하세요: ")
urls = get_urls("韓")
print("검색결과 url 리스트:")
for url in urls:
    print(url)
    img_urls = get_img_url(url)
    print("이미지 url 리스트:")
    for img_url in img_urls:
        print(img_url)


