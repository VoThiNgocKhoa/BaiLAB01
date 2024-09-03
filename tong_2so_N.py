# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 23:38:34 2024

@author: 84372
"""

N = int(input("Nhap so nguyen duong N co 2 chu so: "))
if 9 < N < 100:
    hang_chuc = N // 10
    hang_don_vi = N % 10
    tong_chu_so = hang_chuc + hang_don_vi
    print("Tong cac chu so cua N la: ", tong_chu_so)
else:
    print("khong hop le")
        
    
