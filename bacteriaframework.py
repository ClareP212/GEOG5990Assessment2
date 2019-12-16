# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 16:01:14 2019

@author: gy15cep
"""
import random
#create agents and define their behaviours
class Bacteria() :
    def __init__ (self,ground_zero,height,location,y,x):
        self.ground_zero = ground_zero
        self.y = y
        self.x = x
        self.height = height
        
    def move(self):
        if self.height >0: #if height is greater than 0
                #wind direction blow
                wind_dir = random.random()
                if wind_dir <= 0.05:
                    self.x = self.x - 1
                    #print ("West")
                elif wind_dir <= 0.15:
                    self.y = self.y + 1
                    #print ("North")
                elif wind_dir <= 0.25:
                    self.y = self.y - 1
                    #print ("South")
                else:
                    self.x = self.x + 1
                    #print ("East")  
            
                #turbulence
                if self.height >= 75:
                    turb = random.random()
                    if turb <= 0.2:
                        self.height = self.height + 1
                        #print ("Up")
                    elif turb <= 0.3:
                        self.height = self.height
                        #print ("Stay")
                    else:
                        self.height = self.height - 1     
                        #print ("Down")
                else:
                    self.height = self.height - 1     
                    #print ("Down") 
        #print (self.x & self.y)

            