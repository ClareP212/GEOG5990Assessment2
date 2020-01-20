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
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.animation 
import tkinter
import random

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

##Check file has reas, uncomment to display file
#matplotlib.pyplot.imshow(ground_zero)

##Check row and column numbers of file read in
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
num_of_bacteria = 5000



def setup():
    
    global east_chance
    east_chance = eastscale.get() #global variable defining the number of sheep, updated from GUI sheep slider.
    print ("Chance of going East = " + str(east_chance))
    global south_chance
    south_chance = southscale.get() #global variable defining the number of wolves, updated from GUI wolf slider.
    print ("Chance of going South = " + str(south_chance))  
    
    
    
    for i in range(num_of_bacteria):
        bacteria.append(bacteriaframework.Bacteria(ground_zero,height,location,y,x))
    
####output file####
#blank output list
#update output file in module?

            
def gen_function():
    """
    Function to keep running the model as long as the stopping conditions are not met.
    Stopping condition is if carry_on = true, carry on is trigegred when agent height reaches 0 (ground).
    """
    a = 0
    global carry_on 
    while (carry_on) : #keep going as long as carry on = true (there are still sheep) and we still have iterations to go
        yield a			
        a = a + 1   

def update():
    global carry_on
    global bacteria_location
    
    for i in range(num_of_bacteria):
        carry_on = True
        for j in gen_function(): 
            bacteria[i].move()
            if bacteria[i].height == 0:
                carry_on = False
    #attach final x y locations to bacteria_location        
        bacteria_location.append([bacteria[i].y,bacteria[i].x])
    #add 1 to each xy in bacteria location list
    global output
    output = []
    for row in range(500):
        thing = []
        for i in range (500):
            thing.append(0)
        output.append(thing)   # merge w creation
    
    for i in range(len(bacteria_location)): #remove and merge
        y = bacteria_location[i][0]
        x = bacteria_location[i][1]
        output[y][x] = output[y][x] + 1

    ##plot the output
    matplotlib.pyplot.imshow(output)
    canvas.draw()
    #matplotlib.pyplot.xlim([250,500]) 
    #matplotlib.pyplot.ylim([100,200])


def create_output():
    #create txt and populate it with values
    global output
    f = open("output.txt", 'w')
    for row in output:
        #f.write(str(row))
        for thing in row:
            f.write(str(thing))
            f.write(', ')
        f.write('\n')
    f.close

###########GUI###########
    
##GUI functions
    #set figure size
fig = matplotlib.pyplot.figure(figsize=(5, 5)) #change to 7,7 on computer
ax = fig.add_axes([0, 0, 1, 1])

#build main GUI window
root = tkinter.Tk() # build main window
root.wm_title("Model") # set title
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=1)

def stop():
    """
    Function to top the model running and close the model window
    """
    root.destroy()




##GUI Sliders
#slider functions
def slider_max(value):
    """
    Function to set the slider scales to max 100
    """
    percs = [float(northscale.get()), float(southscale.get()),float(eastscale.get()),float(westscale.get())]
    total = sum(percs)
    slider_max = (value + (100 - total))
    print("slider max = " + str(slider_max))
    return slider_max

def north_max(value):
    northscale.configure(to=(slider_max(value)))
def south_max(value):
    southscale.configure(to=(slider_max(value)))
def east_max(value):
    eastscale.configure(to=(slider_max(value)))
def west_max(value):
    westscale.configure(to=(slider_max(value)))
        
def default_slider():
    eastscale.set(75)     
    southscale.set(10)   
    northscale.set(10)   
    westscale.set(5) 
def reset_slider():
    eastscale.set(0)     
    southscale.set(0)   
    northscale.set(0)   
    westscale.set(0)
        

##slider bars
#wind east dir
northscale = tkinter.Scale(root, label = "North", from_=0,command=lambda _: north_max(northscale.get()), orient = 'horizontal', length = 200,resolution = 5)
northscale.pack()
southscale = tkinter.Scale(root, label = "South", from_=0,command=lambda _: south_max(southscale.get()), orient = 'horizontal', length = 200,resolution = 5)
southscale.pack()
eastscale = tkinter.Scale(root, label = "East", from_=0,command=lambda _: east_max(eastscale.get()), orient = 'horizontal', length = 200,resolution = 5)
eastscale.pack()
westscale = tkinter.Scale(root, label = "West", from_=0,command=lambda _: west_max(westscale.get()), orient = 'horizontal', length = 200,resolution = 5)
westscale.pack()


#GUI buttons
default_slider = tkinter.Button(root,text="Default slider Values", command=default_slider)
default_slider.pack(padx=5, pady=20,side='left')
default_slider = tkinter.Button(root,text="Reset slider Values", command=reset_slider)
default_slider.pack(padx=5, pady=20,side='left')
confirm_setup = tkinter.Button(root,text="Confirm Setup",fg="red", command=setup)
confirm_setup.pack(padx=5, pady=20,side='left')
run_butt = tkinter.Button(root,text="RUN",fg="red", command=update)
run_butt.pack(padx=5, pady=10,side='left')
run_butt = tkinter.Button(root,text="QUIT",fg="red", command=stop)
run_butt.pack(padx=5, pady=0,side='left')

#keep animation window running
tkinter.mainloop()


"""
Day 1 - Read in the data, find the cooridnates of bombing point, create random movements NESW and UpDown
Day 2 - create generator function to run until hits 0, create new module and move in movement functions,
    get this working with changeable num_of_bacteria var, scrap generator function
Day 3 - Set up generator function to run iterations for each agent until height 0,
    wrote something to add one to output in location specified by bacteria_location - needs running and checking (at work)
Day 4 - got generator function working, produced text file of output
Day 5 - added anmation, update every bacteria ground but very computationally expensive and takes too long so removed
Day 6 - fixng the sliders to be max 100 for all 4, usability?? this is very tricky, attempting to fix
Day 7 - attempting to fix sliders again, function to set maximum value

To do:
GUI and animation
Allowing the user to set
    the number of particles
    windspeed-based probabilities (for example, using scollbars in Jupyter Notebook)., move with max
    particle height
sum to check the total of outputs is equal to the total bacteria input
move bacteriaframework to here
"""
