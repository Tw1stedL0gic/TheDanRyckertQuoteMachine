#!/usr/bin/python

from lxml import html
import requests
import random
import threading
from threading import Thread

def scrape_quotes_on_page(i):
    global quotes
    global quote_lock
    
    website = 'http://danryckertjustsaid.tumblr.com/page/' + str(i)

    page = requests.get(website)
    tree = html.fromstring(page.content)

    quotes_on_this_page = tree[1].xpath('//article[@class="post text"]//h3//a/text()')

    quote_lock.acquire()
    quotes = quotes + quotes_on_this_page
    quote_lock.release()
    



quotes = []

pages_to_scrape = 30

quote_lock = threading.RLock()
threads = []

for i in range(pages_to_scrape):
    threads.append(Thread(target=scrape_quotes_on_page, args=(i+1,)))
    threads[i].start()

for i in range(pages_to_scrape):
    threads[i].join()
    
random.seed()


print '.=======================================================================================.'
print '    Welcome to The Dan Ryckert Quote Machine                                             '
print '      ' + random.choice(quotes)
print '\'=======================================================================================\''
