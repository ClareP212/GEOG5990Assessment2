# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 17:36:10 2019

@author: gy15cep
"""

#Bacterial Bomb

import random


x = random.random()

if x <= 0.05:
    print ("West")
elif x <= 0.15:
    print ("North")
elif x <= 0.25:
    print ("South")
else:
    print ("East")

print (x)

