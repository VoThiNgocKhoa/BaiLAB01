# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 01:14:12 2024

@author: 84372
"""

so_xe = (input("Nhập số xe gồm 4 chữ số: "))
if len(so_xe) == 4 and so_xe.isdigit():
    tong_so = (int(so_xe[0]))+(int(so_xe[1]))+(int(so_xe[2]))+(int(so_xe[3]))
    tong_nut = tong_so%10 
    print(f"Số xe của bạn là: {tong_nut} nút ")
else:
    print("không hợp lệ! Vui lòng nhập số xe gồm 4 chữ số")

   
   