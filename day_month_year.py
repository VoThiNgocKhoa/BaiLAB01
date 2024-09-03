# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 15:29:34 2024

@author: 84372
"""

day = int(input("Nhập ngày: "))
month = int(input("Nhập tháng: "))
year = int(input("Nhập năm sinh: "))
day_format_a = f"{day}/{month}/{year}"
print(day_format_a)
day_format_b = f"{day}/{month}/{year%100}"
print(day_format_b)
day_format_c = f"{year}/{month}/{day}"
print(day_format_c)
day_format_reverse_b = f"{year%100}/{month}/{day}"
print(day_format_reverse_b)


