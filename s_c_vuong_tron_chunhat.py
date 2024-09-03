# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 01:59:22 2024

@author: 84372
"""

import math

hinh = input("Nhập hình (v = vuông, n = chữ nhật, t = tròn): ")

if hinh == 'v':
    canh = float(input("Nhập cạnh hình vuông: "))
    chu_vi = canh * 4
    dien_tich = canh ** 2
    print(f"Chu vi: {chu_vi}, Diện tích: {dien_tich}")

elif hinh == 'n':
    chieu_dai = float(input("Nhập chiều dài: "))
    chieu_rong = float(input("Nhập chiều rộng: "))
    chu_vi = 2 * (chieu_dai + chieu_rong)
    dien_tich = chieu_dai * chieu_rong
    print(f"Chu vi: {chu_vi}, Diện tích: {dien_tich}")

elif hinh == 't':
    ban_kinh = float(input("Nhập bán kính hình tròn: "))
    chu_vi = 2 * math.pi * ban_kinh
    dien_tich = math.pi * ban_kinh ** 2
    print(f"Chu vi: {chu_vi}, Diện tích: {dien_tich}")

else:
    print("Hình không hợp lệ")