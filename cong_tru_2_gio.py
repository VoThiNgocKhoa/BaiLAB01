# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 23:44:03 2024

@author: 84372
"""

hh1 = int(input("Nhập giờ: "))
mm1 = int(input("Nhập phút: "))
ss1 = int(input("Nhập giây: "))
time_1 = hh1 * 3600 + mm1 *60 + ss1
hh2 = int(input("Nhập giờ: "))
mm2 = int(input("Nhập phút: "))
ss2 = int(input("Nhập giây: "))
time_2 = hh2 * 3600 + mm2 *60 + ss2
tong = time_1 + time_2
a = tong // 3600
b = tong % 3600 //60
c = tong % 3600 % 60
print(f"Tổng 2 giờ là: {a} giờ {b} phút {c} giây")
if time_1 > time_2:
    hieu = time_1 - time_2
    a1 = hieu // 3600
    b1 = hieu % 3600 //60
    c1 = hieu % 3600 % 60
    print(f"Hiệu 2 giờ là: {a1} giờ {b1} phút {c1} giây")
else:
    hieu = time_2 - time_1
    a2 = hieu // 3600
    b2 = hieu % 3600 //60
    c2 = hieu % 3600 % 60
    print(f"Hiệu 2 giờ là: {a2} giờ {b2} phút {c2} giây")

