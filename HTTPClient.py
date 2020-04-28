# -*- Coding: utf-8 -*-

import urllib.request, urllib.error
from bs4 import BeautifulSoup

class HTTPClient:
    
    def __init__(self):
        pass

    def connect(self, _url):
        try:
            html = urllib.request.urlopen(_url)
            soup = BeautifulSoup(html, "lxml")
            return soup

        except urllib.error.HTTPError as e:
            print(e)

        except NameError as e:
            print(e)

        return ""