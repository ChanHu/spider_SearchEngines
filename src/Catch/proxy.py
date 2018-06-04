#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : proxy.py
# @Author: HuZejie
# @Date  : 2018/4/27

import requests

def get_proxy():
    return requests.get("http://39.106.119.213:5010/get/").content

def delete_proxy(proxy):
    requests.get("http://39.106.119.213:5010/delete/?proxy={}".format(proxy))

def getOneProxy():
    # ....
    retry_count = 5
    proxy = get_proxy()
    while retry_count > 0:
        try:
            html = requests.get('https://httpbin.org/ip', proxies={"http": "http://"+str(proxy)[2::]})
            # html = requests.get('https://www.baidu.com', proxies={"http": "http://" + "45.119.112.34: 44311"})
           # html = requests.get('driver.get('http://httpbin.org/ip')')
            # 使用代理访问
            print("proxy is :"+"http://"+str(proxy)[2::])
            print(html.text)
            return str("http://"+str(proxy)[2::])
        except Exception:
            retry_count -= 1
    # 出错5次, 删除代理池中代理
    delete_proxy(proxy)
    return None

if __name__=='__main__':
    getOneProxy()
