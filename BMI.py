# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 00:34:00 2024

@author: 84372
"""

import math 
weight = float(input("Nhập cân nặng của bạn(kg): "))
height = float(input("Nhập chiều cao của bạn(m): "))
if weight > 0:
    height > 0 
    BMI = weight / (height ** 2)
    print(f"Số đo kiểm tra sức khỏe BMI của bạn là {BMI} ")
else:
    print("Không hợp lệ")