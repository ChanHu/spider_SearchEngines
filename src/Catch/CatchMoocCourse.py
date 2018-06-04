#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : CatchMoocCourse.py
# @Author: HuZejie
# @Date  : 2018/4/24

# catch mooc course to "course".txt
import pymysql
from pyquery import PyQuery as pq
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.proxy import ProxyType
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def CatchOneMoocCourse(CouUrl,Oneproxy):
    # print(Oneproxy[7::])
    #
    # service_args = [
    #     '--proxy='+Oneproxy[7::],
    # ]
    # fireFoxOptions = webdriver.FirefoxOptions()
    # fireFoxOptions.set_headless()
    # brower = webdriver.Firefox(firefox_options=fireFoxOptions,service_args=service_args)

    # chrome_options = Options()
    # chrome_options.add_argument("--headless")
    #
    # chrome = webdriver.Chrome(executable_path="D:\Program Files\chromedriver_win32\\chromedriver.exe", chrome_options=chrome_options)
    # chrome=webdriver.PhantomJS(executable_path="D:\Program Files (x86)\phantomjs-2.1.1-windows\\bin\phantomjs.exe")
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome = webdriver.Chrome(executable_path="D:\Program Files\chromedriver_win32\\chromedriver.exe",
                              chrome_options=chrome_options)
    chrome.get(CouUrl)
    doc=pq(chrome.page_source)

    # executable_path为你下载phantomjs的地址
    # page_source为当前页面的源代码
    # print(doc)

    chrome.find_element_by_id("review-tag-button").click()
    doc2=pq(chrome.page_source)

    # CouId=CouUrl[34::]
    CouId=CouUrl
    print("\nCouId:\n"+CouId)
    CouName=doc('.course-title.f-ib.f-vam')
    print("\ncourse name :\n"+CouName.text()+"\n")

    CouIsCountry=doc('.tag.f-f0.f-pr.ga-click')
    print("\n是否为国家精品课程：\n"+CouIsCountry.text())

    RealCouIsCountry=0
    if(CouIsCountry.text()=="国家精品"):
        RealCouIsCountry=1
    print(RealCouIsCountry)

    # CouTeacher=doc('.m-teachers ')
    # print("\ncourse teachers:\n"+CouTeacher.text())

    CouAttendAmount=doc('.course-enroll-info_course-enroll_price-enroll_enroll-count')
    if(CouAttendAmount.text()==""):
        realAmount=0
    else:
        realAmount=int(CouAttendAmount.text()[2:-3:])
    print("\nattendAmount:\n"+str(realAmount))

    CouSchool=doc('.ga-click.m-teachers_school-img.f-ib')
    print("\nschool: \n"+CouSchool.attr("data-label"))

    realSchool=CouSchool.attr("data-label")
    while(realSchool[0]!='-'):
        realSchool=realSchool[1::]
    realSchool = realSchool[1::]
    print(realSchool)

    CouEval=doc2('.ux-mooc-comment-course-comment_head_rating-scores')
    if (CouEval.text() == ""):
        realEval = 0
    else:
        realEval = float(CouEval.text())
    print("\nEval: \n"+str(realEval))

    CouEvalAmount=doc2('#review-tag-num')
    if(CouEvalAmount.text()==""):
        realEvalAmount=0
    else:
        realEvalAmount=int(CouEvalAmount.text()[1:-1:])
    print("\nEvalAmount: \n"+str(realEvalAmount))

    #put it into mysql
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='course', charset='utf8')


    cursor = conn.cursor()

    sql2="SELECT id FROM college WHERE name = '%s'" % realSchool

    try:
        cursor.execute(sql2)
        conn.commit()
        data=cursor.fetchone()
        print("school id ++++++++++++++"+data[0])
    except:
        conn.rollback()

    #eval CouScore
    if(data != None):
        CouScore=(600-data[0])/600*30+realEval*realEvalAmount/5000*30+realAmount/10000*20+RealCouIsCountry*20
    else:
        CouScore=realEval*realEvalAmount/5000*30+realAmount/10000*20+RealCouIsCountry*20


    sql = "INSERT INTO course(CouId,CouName,CouTeacher,CouSchool,CouEval,CouEvalAmount,CouAttendAmount,CouIsCountry,CouScore) " \
          "VALUES ('%s','%s','%s','%s',%f,%d,%d,%d,%f)" \
          %(CouId,CouName.text(),"",realSchool,realEval,realEvalAmount,realAmount,RealCouIsCountry,CouScore)



    try:
        cursor.execute(sql)
        conn.commit()
        print("successfully add one!")
    except:
        conn.rollback()

    conn.close()
    chrome.close()
if __name__=='__main__':
    CatchOneMoocCourse("https://www.icourse163.org/course/NJNU-1001753089","")