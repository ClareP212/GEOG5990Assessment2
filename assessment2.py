# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 17:36:10 2019

@author: gy15cep

Bacterial Bomb

Build a program to do the following...

Pull in the data file and finds out the bombing point.
Calculates where 5000 bacteria will end up.
Draws a density map of where all the bacteria end up as an image and displays it on the screen.
Saves the density map to a file as text.

The basic algorithm is, for each particle, to move the particle up and along in a loop that picks randomly the way it will go.
When it hits the ground, you make a note of where it hit by incrementing a 2D array by one, and start with the next particle.

Additional marks are awarded for the following.
Allowing the user to set the number of particles and windspeed-based probabilities (for example, using scollbars in Jupyter Notebook).
"""



import random
#import matplotlib

#open raster rile and read
f = open("wind.raster")
ground_zero = []
for line in f:
    parsed_line = str.split(line,",")
    data_line = []
    for word in parsed_line:
        data_line.append(float(word))
    ground_zero.append(data_line) #append each row as list within environment list
f.close()
#display file
#matplotlib.pyplot.imshow(ground_zero)

#find xy of 255
y=-1
for row in ground_zero:
    y = y+1
    if sum(row) >0:
       break
x = ground_zero[y].index(255)
#print(ground_zero[y][x]) 

bacteria = [y,x]
print(bacteria)

#if height is greater than 0
#wind direction blow
wind_dir = random.random()
if wind_dir <= 0.05:
    bacteria[0] = bacteria[0] - 1
    print ("West")
elif wind_dir <= 0.15:
    bacteria[1] = bacteria[1] + 1
    print ("North")
elif wind_dir <= 0.25:
    bacteria[1] = bacteria[1] - 1
    print ("South")
else:
    bacteria[0] = bacteria[0] + 1
    print ("East")


#height aspect
#generator function with iterations?
#does height start at 255?


#turbulence
# if height >= 75:
turb = random.random()
if turb <= 0.2:
    print ("Up")
elif turb <= 0.3:
    print ("Stay")
else:
    print ("Down")
#else Down
    
    
    
    
#output file
#blank output list
output = []
for row in range(300):
    thing = []
    for i in range (300):
        thing.append(0)
    output.append(thing)
#add 1 to every x y with bacteria in it

#create txt and populate NOT WORKING
f = open("output.txt", 'w')
for line in open:
    f.write(line)
f.close()
