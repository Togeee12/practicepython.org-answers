# https://www.practicepython.org/exercise/2014/06/06/17-decode-a-web-page.html
import requests
from bs4 import BeautifulSoup


def wordcount(sentence):

    return len(sentence.split())


def extractarticles(website, number_of_words):

    url = website


r = requests.get(url)
r_html = r.text
soup = BeautifulSoup(r_html, features="lxml")
title_raw = soup.find_all(['h2', 'h3'])
title_strings = []
for e in title_raw:
    if e.string != None and wordcount(e.string) >= number_of_words:
        title_strings.append(e.string)
        title_strings = list(set(title_strings))
        print(*title_strings, sep="\n")

extractarticles(input("Please type in your website: "),
                int(input("Please type in the minimum number of words in the article title: ")))
