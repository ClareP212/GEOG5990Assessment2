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


import bacteriaframework
#import matplotlib

#open raster rile and read
f = open("wind.raster")
ground_zero = []
for line in f:
    parsed_line = str.split(line,",")
    data_line = []
    for value in parsed_line:
        data_line.append(float(value))
    ground_zero.append(data_line) #append each row as list within environment list
f.close()
#display file
#matplotlib.pyplot.imshow(ground_zero)

#rowno = len(ground_zero)
#colno = len(ground_zero[0])
#print(rowno)
#print(colno)

#find xy of 255
y=-1
for row in ground_zero:
    y = y+1
    if sum(row) >0:
       break
x = ground_zero[y].index(255)

#print(ground_zero[y][x]) 
height = ground_zero[y][x]
#print(height)
#bacteria = [y,x,height] #' remove when agent based is working
#print(bacteria)
location = []
bacteria = []
bacteria_location = []
num_of_bacteria = 3

for i in range(num_of_bacteria):
    bacteria.append(bacteriaframework.Bacteria(ground_zero,height,location,y,x))

for i in range(num_of_bacteria):
    carry_on = True
    for j in gen_function(): 
        bacteria[i].move()
        if bacteria[i].height == 0:
            carry_on = False

#attach final x y locations to bacteria_location
for i in range(num_of_bacteria):
    bacteria_location.append([bacteria[i].y,bacteria[i].x])
    print(bacteria[i].height)

print(bacteria_location)

def gen_function():
    """
    Function to keep running the model as long as the stopping conditions are not met.
    Stopping conditions are:
    """
    a = 0
    global carry_on 
    while (carry_on) : #keep going as long as carry on = true (there are still sheep) and we still have iterations to go
        yield a			
        a = a + 1   

 #output file
#blank output list
output = []
for row in range(300):
    thing = []
    for i in range (300):
        thing.append(0)
    output.append(thing)       
        
#add 1 to each xy in bacteria location list
for i in bacteria_location:
    y = bacteria_location[i][0]
    x = bacteria_location[i][1]
    output[y][x] = output[y][x] + 1

matplotlib.pyplot.imshow(output)

#create txt and populate   NOT WORKING
#f = open("output.txt", 'w')
#for line in open:
#    f.write(line)
#f.close
"""
Day 1 - Read in the data, find the cooridnates of bombing point, create random movements NESW and UpDown
Day 2 - create generator function to run until hits 0, create new module and move in movement functions,
    get this working with changeable num_of_bacteria var, scrap generator function
Day 3 - Set up generator function to run iterations for each agent until height 0,
    wrote something to add one to output in location specified by bacteria_lcoation - needs runnign and checking (at work)

To do:
get output to produce txt file output.
GUI and animation
"""
