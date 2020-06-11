#!/bin/env python3
#encoding:utf-8

import re
from lxml import etree

class PageParser():
    def __init__(self,):
        print('init PageParser')
        self.titleRR = re.compile('<title>(.*)</title>')
        self.ahrefRR = re.compile('<a\s+.*?href="(.*?)">')

    def getTitle(self, content, pageInfo):
        headSection = content[content.find('<head>'):content.find('</head>')+7]
        headXml = etree.HTML(headSection)

        title = headXml.xpath('//title')

        if len(title) > 1:
            print('title length {}'.format(len(title)))
            for i in title:
                print('title is {}'.format(i.text))

        for i in title:
            pageInfo.setTitle(i.text.strip())


        results = self.titleRR.findall(content)
        for i in results:
            pageInfo.setTitle(i.strip())

    def getKeywords(self, content, pageInfo):
        headSection = content[content.find('<head>'):content.find('</head>')+7]
        headXml = etree.HTML(headSection)

        kwNodes = headXml.xpath('//meta[@name="keywords"]')
        
        for node in kwNodes:
            kwStr = node.get('content', '')
            kws = kwStr.split(',')
            pageInfo.addKeywords(kws)

    def parse(self, content, pageInfo, baseHost):

        self.getTitle(content, pageInfo)

        self.getKeywords(content, pageInfo)

        freshUrls = []
        hrefs = self.ahrefRR.findall(content)
        for href in hrefs:
            if href.startswith('http'):
                freshUrls.append(href)
            else:
                freshUrls.append(baseHost+href)


if __name__ == '__main__':
    pp = PageParser()
