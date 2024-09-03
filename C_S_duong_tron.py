# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 00:22:46 2024

@author: 84372
"""

import math
ban_kinh = float(input("Nhập bán kính của hình tròn: "))
C = 2 * math.pi * ban_kinh
S = math.pi * (ban_kinh**2)
print(f"Chu vi hình tròn là {C} ") 
print(f"Diện tích hình tròn là {S} ")
