# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 23:52:48 2024

@author: 84372
"""

time = input("Nhập giờ phút giây theo định dạng (hh:mm:ss): ")
hh = int(time[:2])
mm = int(time[3:5])
ss = int(time[6:])
quy_doi = hh*3600 + mm*60 + ss
print(f"Quy đổi ra giây: {quy_doi} giây")
    
    