#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Utils.py
# @Author: HuZejie
# @Date  : 2018/4/18
import pymysql

if __name__=='__main__':
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='course', charset='utf8')

    cursor = conn.cursor()

    sql ="INSERT INTO course(CouId,CouName,CouTeacher,CouSchool,CouEval,CouEvalAmount,CouAttendAmount,CouIsCountry) VALUES ('BIT-1001604004','大学物理典型问题解析—振动、波动与光学','','8007-北京理工大学','',0,1131,0)"

    try:
        cursor.execute(sql)
        conn.commit()
        print("successfully add one!")
    except:
        conn.rollback()

    conn.close()