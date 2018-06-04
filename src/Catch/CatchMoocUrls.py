#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : CatchMoocUrls.py
# @Author: HuZejie
# @Date  : 2018/4/25
from queue import Queue
from selenium import webdriver
from pyquery import PyQuery as pq
from selenium.webdriver.chrome.options import Options

def get_mooc_urls():
    urls=Queue(100000)
    CoursesUrl="https://www.icourse163.org/category/all"
    # chrome = webdriver.PhantomJS(executable_path="D:\Program Files (x86)\phantomjs-2.1.1-windows\\bin\phantomjs.exe")
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome = webdriver.Chrome(executable_path="D:\Program Files\chromedriver_win32\\chromedriver.exe", chrome_options=chrome_options)
    chrome.get(CoursesUrl)
    doc = pq(chrome.page_source)
    # print(doc)
    # executable_path为你下载phantomjs的地址
    # page_source为当前页面的源代码
    # print(doc)

    #find max page
    pagenum=doc(".ux-pager_itm ")
    t = (pagenum.text())

    maxpagenum = 0
    i = -1
    while (t[i] != " "):
        maxpagenum += (ord(t[i]) - ord("0")) * pow(10, -i - 1)
        i -= 1
    # print(t)
    print(maxpagenum)
    # maxpagenum=1
    #add the rest url
    i = 1
    while (i <= maxpagenum):
        print("----------------------------------------------------------------")
        print("p %d Eval" % i)
        i += 1
        chrome.find_element_by_link_text("下一页").click()
        doc3 = pq(chrome.page_source)
        # print(chrome.page_source)
        url = doc3(".u-clist.f-bg.f-cb.f-pr.j-href.ga-click")
        for u in url:
            s = u.attrib['data-href']
            print(s)
            if (s[0] == '/'):
                urls.put("https://www.icourse163.org" + s)

    return urls

if __name__=='__main__':
    get_mooc_urls()