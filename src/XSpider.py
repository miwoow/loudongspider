#!/bin/env python3
#encoding:utf-8

import requests
from PageInfo import PageInfo
from PageParser import PageParser
import urllib

class XSpider():
    def __init__(self,):
        print('init xspider')
        self.StartUrl = ''
        self.PageInfo = PageInfo()
        self.FreshUrls = []
        self.BaseHost = ''
        self.headers = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
                }

    def _get(self, url):
        req = requests.get(url=url, headers=self.headers)
        return req

    def _post(self, url):
        pass

    def initWithStartUrl(self, url):
        self.StartUrl = url
        hostInfo =  urllib.parse.urlparse(url)
        self.BaseHost = hostInfo.scheme+'://'+hostInfo.netloc
        self.FreshUrls.append(url)

    def start(self,):

        urls = self.FreshUrls
        self.FreshUrls = []
        for url in urls:
            req = self._get(url)
            pp = PageParser()
            pp.parse(req.text, self.PageInfo, self.BaseHost)
        self.PageInfo.output()



if __name__ == '__main__':
    spider = XSpider()
    spider.initWithStartUrl('https://paper.seebug.org/')
    spider.start()
