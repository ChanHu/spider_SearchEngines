# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # @File  : CatchMoocEval.py
# # @Author: HuZejie
# # @Date  : 2018/4/24
# from selenium import webdriver
# from pyquery import PyQuery as pq
# import  time
#
# chrome=webdriver.PhantomJS(executable_path="D:\Program Files (x86)\phantomjs-2.1.1-windows\\bin\phantomjs.exe")
# chrome.get("https://www.icourse163.org/course/CUIT-1002260004")
# doc=pq(chrome.page_source)
# # executable_path为你下载phantomjs的地址
# # page_source为当前页面的源代码
# # print(doc)
#
# time.sleep(2)
#
# chrome.find_element_by_id("review-tag-button").click()
# doc2=pq(chrome.page_source)
#
# CouName=doc('#g-body .f-cb .f-fl.course-title-wrapper ')
# print("course name :"+CouName.text()+"\n")
#
# teacher=doc('#g-body .m-teachers ')
# print("course teachers:\n"+teacher.text())
#
# attendAmount=doc('#course-enroll-info .course-enroll-info_course-enroll_price-enroll_enroll-count')
# print("attendAmount:"+attendAmount.text())
#
#
# school=doc('#g-body .m-teachers s.m-teachers_school-img f-ib')
# print(school.text())
#
# comment=doc2("#g-body .ux-mooc-comment-course-comment_comment-list")
# print("\nEval:\n"+comment.text())
#
#
# maxpage=doc2("#g-body .ux-mooc-comment-course-comment_pager .ux-pager_itm a")
# t=(maxpage.text())
# maxpagenum=0
# i=-1
# while(t[i]!=" "):
#     maxpagenum+=(ord(t[i])-ord("0"))*pow(10,-i-1)
#     i-=1
# print(t)
# print(maxpagenum)
#
# i=1
# while(i<=maxpagenum):
#     print("----------------------------------------------------------------")
#     print("p %d Eval" % i)
#     i += 1
#     chrome.find_element_by_link_text("下一页").click()
#     doc3=pq(chrome.page_source)
#     print(doc3("#g-body .ux-mooc-comment-course-comment_comment-list").text()+"\n")

#
#
#
# # db = pymysql.connect("localhost","root","123456","course")
# #
# # cursor = db.cursor()
# #
# # sql = "INSERT INTO course(CouName,CouTeacher,CouSchool,CouEval,CouStar,CouAttendAmount,CouIsCountry) " \
# #       "VALUES ('%s','%s','%s','%s','%d','%d',%d)" %()
# # try:
# #     cursor.execute(sql)
# #     db.commit()
# #     print("successfully add one!")
# # except:
# #     db.rollback()
# #
# # db.close()
