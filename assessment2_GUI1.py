# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 17:36:10 2019
@author: gy15cep
Bacterial Bomb
"""
#importing modules
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.animation 
import tkinter
import tkinter.messagebox
import random

#open raster file containing bomb location and read
f = open("wind.raster")
ground_zero = []
for line in f:
    parsed_line = str.split(line,",")
    data_line = []
    for value in parsed_line:
        data_line.append(float(value))
    ground_zero.append(data_line)
f.close()
##To check file has read, uncomment to display file
#matplotlib.pyplot.imshow(ground_zero)

##Check row and column numbers of file read in
#rowno = len(ground_zero)
#colno = len(ground_zero[0])
#print(rowno)
#print(colno)


#find xy of bomb point - with value of 255
y=-1
for row in ground_zero:
    y = y+1
    if sum(row) >0:
       break
x = ground_zero[y].index(255)
height = ground_zero[y][x]
#print(ground_zero[y][x]) 
#print(height)

def setup():
    """
    Function which defined the wind direction probabilities based on the GUI,
    initialises bacteria and feeds in the relevant lists and variables to Bacteria Class
    Returns:
        If sliders sum to 100, returns text showing percentages chosen,
        if less than 100 creates messagebox informing user to ammend sliders
    """
    global north_perc
    north_perc = (northscale.get()/100) #global variable defining north scale value, updated from GUI slider.
    global south_perc
    south_perc = (southscale.get()/100) #global variable defining south scale value, updated from GUI slider.
    global east_perc
    east_perc = (eastscale.get()/100) #global variable defining east scale value, updated from GUI slider.
    global west_perc
    west_perc = (westscale.get()/100) #global variable defining west scale value, updated from GUI slider.
    

    if 1 == (north_perc + south_perc + east_perc + west_perc):
        print ("Chance of going South = " + str(west_perc*100) + "%")
        print ("Chance of going East = " + str(east_perc*100) + "%")  
        print ("Chance of going South = " + str(south_perc*100) + "%") 
        print ("Chance of going North = " + str(north_perc*100) + "%")
        
        global num_of_bacteria
        num_of_bacteria = 5000
        global bacteria
        bacteria = []
        for i in range(num_of_bacteria):
            bacteria.append(Bacteria(ground_zero,height,y,x,north_perc,south_perc,east_perc,west_perc))
    else:
        tkinter.messagebox.showerror("Wind Direction Probabilities","Wind Direction probabilities do not add to 100%, please ammend sliders")
    
##Create agents and define their behaviours
class Bacteria() :
    def __init__ (self,ground_zero,height,y,x,north_perc,south_perc,east_perc,west_perc):
        """
        Function to initiate the agent 
        Params:
            ground_zero - 
            height - wolf class agent list
            location - sheep class agent list
            y - y variable from html in model.
            x - x variable from html in model.
            north_perc - 
            south_perc - 
            east_perc - 
            west_perc - 
            
        """
        self.ground_zero = ground_zero
        self.y = y
        self.x = x
        self.height = height
        self.north_perc = north_perc
        self.south_perc = south_perc
        self.east_perc = east_perc
        self.west_perc = west_perc
        
    def move(self):
        if self.height >0: #if height is greater than 0
                #wind direction blow
                wind_dir = random.random()
                if wind_dir <= west_perc:
                    self.x = self.x - 1
                    #print ("West")
                elif wind_dir <= (west_perc + north_perc):
                    self.y = self.y + 1
                    #print ("North")
                elif wind_dir <=(west_perc + north_perc + south_perc):
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
#    def check(self):
#        print (self.north_perc)
#        print (self.south_perc)
#        print (self.east_perc)
#        print (self.west_perc)

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
    bacteria_location = []
    
    for i in range(num_of_bacteria):
        carry_on = True
        #bacteria[i].check()
        for j in gen_function(): 
            bacteria[i].move()
            if bacteria[i].height == 0:
                carry_on = False
        bacteria_location.append([bacteria[i].y,bacteria[i].x])#attach final x y locations to bacteria_location    
    
    #add 1 to each xy in bacteria location list
    global out_of_range
    out_of_range = 0
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
        if y > 500 or x > 500:
            out_of_range = out_of_range + 1
        else:
            output[y][x] = output[y][x] + 1

    ##plot the output
    matplotlib.pyplot.imshow(output)
    matplotlib.pyplot.xlim([0,500]) 
    matplotlib.pyplot.ylim([500,0])
    canvas.draw()
    
    print(str(out_of_range) + " Bacteria fell outside of study area.")

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
    Determines the maximum value a slider can be, given the current values of all other sliders,
    before the sum of all slider values is 100 (%)
    Params:
        value - value of slider
    Returns:
        the maximum the relevant slider can be until the sum of all sliders is 100
    """
    percs = [float(northscale.get()), float(southscale.get()),float(eastscale.get()),float(westscale.get())]
    total = sum(percs)
    slider_max = (value + (100 - total))
    #print("slider max = " + str(slider_max))
    return slider_max

def north_max(value):
    """
    Sets the maximum limit of north slider based on max value determined by slider_max function.
    Params:
        value - value of north slider
    """
    northscale.configure(to=(slider_max(value)))
def south_max(value):
    """
    Sets the maximum limit of south slider based on max value determined by slider_max function.
    Params:
        value - value of north slider
    """
    southscale.configure(to=(slider_max(value)))
def east_max(value):
    """
    Sets the maximum limit of east slider based on max value determined by slider_max function.
    Params:
        value - value of east slider
    """
    eastscale.configure(to=(slider_max(value)))
def west_max(value):
    """
    Sets the maximum limit of west slider based on max value determined by slider_max function.
    Params:
        value - value of west slider
    """
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
        

##Create slider bars
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
    wrote something to add one to output in location specified by bacteria_location
Day 4 - got generator function working, produced text file of output
Day 5 - added anmation, update every bacteria ground but very computationally expensive and takes too long so removed
Day 6 - fixng the sliders to be max 100 for all 4, usability?? this is very tricky, attempting to fix
Day 7 - attempting to fix sliders again, function to set maximum value, YAY its working!
    added messagebox if sliders dont add to 100, integrated module so all in one script, issues with output file if
    x and y of bacteria is out of range

To do:
Allowing the user to set
    the number of particles
    move with max
    particle height
sum to check the total of outputs is equal to the total bacteria input
make sliders functions more efficient
change colour of output
do i need to feed in ground zero to bacteria class?
add in timer to update?
set axis to min max x and y
"""
