# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 11:13:51 2018

@author: Turanga1
"""
from datetime import date

today = date.today()
class_end = date(2018,6,30)
class_start = date(2018,1,2)
progress = (today - class_start)/(class_end - class_start) * 100
print(class_end - today, "until class end. ", progress, "% of time elapsed")
