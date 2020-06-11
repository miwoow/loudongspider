#!/bin/env python3
#encoding:utf-8

class PageInfo():
    def __init__(self,):
        print('init pageinfo')
        self.title = ''
        self.keywords = set()

    def setTitle(self, title):
        self.title = title

    def addKeywords(self, keywords):
        self.keywords.update(keywords)

    def output(self,):
        print(self.title)
        print(self.keywords)


if __name__ == '__main__':
    pi = PageInfo()
