#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : CatchMoocByThread.py
# @Author: HuZejie
# @Date  : 2018/4/27
import threading
import time
from src.Catch import CatchMoocUrls, proxy
from src.Catch import CatchMoocCourse


def run_thread(q,proxys,i):
    count = 0
    while (q.empty()==False):
        CatchMoocCourse.CatchOneMoocCourse(q.get(),proxys[i])
        count+=1
        print(str(count))

def CatchMoocByThread():
    num=1
    threads = []
    proxys = []

    for i in range(num):
        proxys.append(proxy.getOneProxy())
    q = CatchMoocUrls.get_mooc_urls()  # get all moocs course's url
    for i in range (num):
        thing = threading.Thread(target=run_thread,args=(q,proxys,i))
        threads.append(thing)

    # 开始时间
    start = time.time()
    # 写个for让两件事情都进行
    for thing in threads:
        # setDaemon为主线程启动了线程matter1和matter2
        # 启动也就是相当于执行了这个for循环
        thing.setDaemon(True)
        thing.start()

    for thing in threads:
        thing.join()
    # 结束时间
    end = time.time()
    print("完成的时间为：" + str(end - start))


if __name__=='__main__':
    CatchMoocByThread()