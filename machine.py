#!/usr/bin/python

from lxml import html
import requests
import random

def scrape_quotes_on_page(i):
    website = 'http://danryckertjustsaid.tumblr.com/page/' + str(i)

    page = requests.get(website)
    tree = html.fromstring(page.content)

    quotes_on_this_page = tree[1].xpath('//article[@class="post text"]//h3//a/text()')

    return quotes_on_this_page


print 'Welcome to The Dan Ryckert Quote Machine'

quotes = []

for i in range(1, 10):
    quotes_on_this_page = scrape_quotes_on_page(i)
    if len(quotes_on_this_page):
        quotes = quotes + quotes_on_this_page
    
random.seed()
print random.choice(quotes)

