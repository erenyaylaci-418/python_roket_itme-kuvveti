# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 12:12:38 2020

@author: eren yaylaci
"""
p= int(input("aracın momentumu:"))
m= int(input("aracın kütlesi:"))

e= (p*p)/(2*m)

h= e/(10*m)

a= str(h)
b="aracın çıkabileceği yükseklik:"
print(b+a)
