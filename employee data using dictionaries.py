# -*- coding: utf-8 -*-
"""
Created on Tue Feb 1 07:36:22 2022

@author: Yusuf Gbedu
"""

employees= [{'name':"John Bellion",'age':26, 'department':"music"},
           {'name':"Aluta Junior",'age':36, 'department':"food"},
           {'name':"Drake Gbedu",'age':87, 'department':"rap"}]
for i in employees:
    print("Name: ", i['name'])
    print("AGE: : ", i['age'])
    print("DEPARTMENT: ", i['department'])
    print("*"*20)
