# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 23:25:57 2024

@author: 84372
"""

a = int(input("nhap vao so nguyen duong a :"))
b = int(input("nhap vao so nguyen duong b :"))
if a > 0 and b > 0:
    phan_nguyen = a // b
    phan_du = a % b
    print("ket qua chia lay phan nguyen :", phan_nguyen)
    print("ket qua chia lay phan du :", phan_du)
else:
    print("phep tinh khong hop le")

    
