#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : calcaulateScore.py
# @Author: HuZejie
# @Date  : 2018/6/4
import pymysql


def calculate():
    #put it into mysql
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='course', charset='utf8')

    cursor = conn.cursor()

    sql="SELECT * FROM course"

    try:
        cursor.execute(sql)
        conn.commit()
        data=cursor.fetchall()
    except:
        conn.rollback()

    for d in data:
        # print(d[0]+"   "+d[1]+"     "+d[3])
        if(d[3]!=None):
            id=d[0]
            school=d[3]
            eval = d[4]
            evalamount = d[5]
            attendamount = d[6]
            isCountry = d[7]

            while (school[0] != '-'):
                school = school[1::]
            school = school[1::]
            # get shoolscore

            sql2 = "SELECT id FROM college WHERE name = '%s'" % school
            try:
                cursor.execute(sql2)
                conn.commit()
                data2=cursor.fetchone()
                print("school id ++++++++++++++"+data2[0])
            except:
                conn.rollback()


            if(data2 != None):
                score=(600-int(data2[0]))/ 600 * 30 + eval * evalamount / 5000 * 30 + attendamount / 10000 * 20 + isCountry * 20
            else:
                score=eval * evalamount / 5000 * 30 + attendamount / 10000 * 20 + isCountry * 20

            print(score)

            sql="UPDATE course SET CouScore = '%f' WHERE CouId='%s'"%(score,id)

            try:
                cursor.execute(sql)
                conn.commit()
                print("successfully update one!")
            except:
                conn.rollback()
        else:
            id = d[0]
            eval = d[4]
            evalamount = d[5]
            attendamount = d[6]
            score=eval*evalamount/2000*60+attendamount/1000*40;
            print(score)
            sql = "UPDATE course SET CouScore = '%f' WHERE CouId='%s'" % (score, id)

            try:
                cursor.execute(sql)
                conn.commit()
                print("successfully update one!")
            except:
                conn.rollback()

    conn.close()

if __name__=='__main__':
    calculate()