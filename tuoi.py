# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 00:08:54 2024

@author: 84372
"""
nam_sinh = int(input("Nhập năm sinh của bạn: "))
if 0 < nam_sinh < 2022:
    nam_hien_tai = int(input("Nhập năm hiện tại "))
    tuoi = nam_hien_tai - nam_sinh
    print(f"Bạn năm nay {tuoi} tuổi ")
else:
    print("Không hợp lệ! Mời nhập lại năm sinh")
