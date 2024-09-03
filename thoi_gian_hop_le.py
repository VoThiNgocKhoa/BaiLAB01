# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 00:58:20 2024

@author: 84372
"""

hh = int(input("Nhập giờ: "))
mm = int(input("Nhập phút: "))
ss = int(input("Nhập giây: "))
if (0 <= hh <= 23) and (0 <= mm <= 59) and (0 <= ss <= 59):
    print("Thời gian hợp lệ")
else: 
    print("Thời gian không hợp lệ")
   
