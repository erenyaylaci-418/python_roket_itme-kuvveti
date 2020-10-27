# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 12:33:43 2020

@author: erenyaylaci
"""
t= int(input("rokete uygulanan itmenin süresi(saniye):")) 
     
f= int(input("rokete uygulanan kuvvet(Newton):"))

fnet= f-10
I= fnet*t
m= int(input("roketin kütlesi:"))
e= (I*I)/(2*m)
h= (e/(10*m))/1000

a= "roketin çıkabileceği yükseklik:"
b=str(h)
c="km"
print(a+b+c)


