#!/usr/bin/python

from lxml import html
import requests
import random
from threading import Thread

def scrape_quotes_on_page(i):
    global quotes

    website = 'http://danryckertjustsaid.tumblr.com/page/' + str(i)

    page = requests.get(website)
    tree = html.fromstring(page.content)

    quotes_on_this_page = tree[1].xpath('//article[@class="post text"]//h3//a/text()')
    quotes = quotes + quotes_on_this_page
    

print 'Welcome to The Dan Ryckert Quote Machine'

quotes = []

pages_to_scrape = 10

threads = [pages_to_scrape]

for i in range(len(threads)):
    threads[i] = Thread(target=scrape_quotes_on_page, args=(i+1,))
    threads[i].start()

for i in range(len(threads)):
    threads[i].join()

print quotes
    
random.seed()
print random.choice(quotes)

