# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 17:36:10 2019
@author: gy15cep
Bacterial Bomb
"""
#importing modules
import matplotlib
matplotlib.use('TkAgg')
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
start_y=-1
for row in ground_zero:
    start_y = start_y+1
    if sum(row) >0:
       break
start_x = ground_zero[start_y].index(255)
#height = ground_zero[y][x]
#print(ground_zero[y][x]) 
#print(height)

def setup():
    """
    Function which defines the wind direction probabilities, hiehgt and number of bacteria based on the GUI,
    initialises bacteria agents and feeds in the relevant lists and variables to bacteria.
    Only sets up the bacteria if the wind direvtion probabilities add up to 100.
    Returns:
        If sliders sum to 100, returns text showing percentages chosen, height and number of bacteria.
        If sliders sum to less than 100 creates messagebox informing the user to ammend sliders.
    """
    global north_perc
    north_perc = (northscale.get()/100) #global variable defining north scale value, updated from GUI slider.
    global south_perc
    south_perc = (southscale.get()/100) #global variable defining south scale value, updated from GUI slider.
    global east_perc
    east_perc = (eastscale.get()/100) #global variable defining east scale value, updated from GUI slider.
    global west_perc
    west_perc = (westscale.get()/100) #global variable defining west scale value, updated from GUI slider.
    
    global height
    height = (heightscale.get()) #global variable defining west scale value, updated from GUI slider.
    
    global num_of_bacteria
    num_of_bacteria = (bacteriascale.get()) #global variable defining west scale value, updated from GUI slider.

    if 1 == (north_perc + south_perc + east_perc + west_perc):
        print ("Chance of going South = " + str(west_perc*100) + "%")
        print ("Chance of going East = " + str(east_perc*100) + "%")  
        print ("Chance of going South = " + str(south_perc*100) + "%") 
        print ("Chance of going North = " + str(north_perc*100) + "%")
        print ("Height = " + str(height))
        print ("Number of Bacteria = " + str(num_of_bacteria))
        
        global bacteria
        bacteria = []
        for i in range(num_of_bacteria):
            bacteria.append(Bacteria(height,start_y,start_x,north_perc,south_perc,east_perc,west_perc))
        run_butt.configure(state='normal',fg = "red")

    else:
        tkinter.messagebox.showerror("Wind Direction Probabilities","Wind Direction probabilities do not add to 100%, please ammend sliders")

##Create agents and define their behaviours
class Bacteria() :
    def __init__ (self,height,y,x,north_perc,south_perc,east_perc,west_perc):
        """
        Function to initiate the agent 
        Params:
            height - the initial height the bacteria are starting at, defined by the user via the height slider in the GUI.
            y - y variable defining the y-coordinate of the bacterial bomb start location.
            x - x variable defining the x-coordinate of the bacterial bomb start location.
            north_perc - the probability of the bacteria moving northwards in any one movement, defined by the user via the north slider in the GUI. 
            south_perc - the probability of the bacteria moving southwards in any one movement, defined by the user via the south slider in the GUI.
            east_perc - the probability of the bacteria moving eastwards in any one movement, defined by the user via the east slider in the GUI.
            west_perc - the probability of the bacteria moving westwards in any one movement, defined by the user via the west slider in the GUI.
            
        """
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


def gen_function():
    """
    Function to keep running the model as long as the stopping conditions are not met.
    Stopping condition is if carry_on = true, carry on is triggered when bacteria height reaches 0 (ground).
    """
    a = 0
    global carry_on 
    while (carry_on) : #keep going as long as carry on = true (there are still sheep) and we still have iterations to go
        yield a			
        a = a + 1   

def update():
    """
    Function to run bacteria movement until they hit the ground, record the coordinates where each bacteria hits the ground.
    Creates an output array of 0's and add 1 to each coordinate for every time a bacteria landed there. Updates the GUI with
    final map of outputs.
    
    Returns:
        Text denoting the number of bacteria which fell outside of the area plotted on the GUI map and output file.
    """
    global carry_on
    global bacteria_location
    bacteria_location = []
    
    #Model bacteria movement until they hit ground (height = 0)
    for i in range(num_of_bacteria):
        carry_on = True
        #bacteria[i].check()
        for j in gen_function(): 
            bacteria[i].move()
            if bacteria[i].height == 0:
                bacteria_location.append([bacteria[i].y,bacteria[i].x])#attach final x y locations to bacteria_location       
                carry_on = False
        
    
    #create output array
    global out_of_range
    out_of_range = 0
    global output
    output = []
    for row in range(300):
        col = []
        for i in range (300):
            col.append(0)
        output.append(col)   # merge w creation
        
    #add 1 to each xy in bacteria location list    
    for i in range(len(bacteria_location)): #remove and merge
        y = bacteria_location[i][0]
        x = bacteria_location[i][1]
        if y > 299 or x > 299 or y < 0 or x < 0:
            out_of_range = out_of_range + 1
        else:
            output[y][x] = output[y][x] + 1
            
    output_butt.configure(state='normal', fg = "black")

    ##plot the output
    matplotlib.pyplot.imshow(output, cmap = 'Greens')
    matplotlib.pyplot.xlim([0,299]) 
    matplotlib.pyplot.ylim([299,0])
    canvas.draw()

    
    print(str(out_of_range) + " Bacteria fell outside of study area.")

def create_output():
    """
    Creates a txt file from the populated output array
    Returns:
        Prints text to inform user file has been created and where
    """
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
    print("output.txt created in same file directory as model. :)")


###########GUI###########
#set figure size
fig = matplotlib.pyplot.figure(figsize=(7, 7)) #change to 7,7 on computer
ax = fig.add_axes([0, 0, 1, 1])

#build main GUI window
root = tkinter.Tk() # build main window
root.wm_title("Tracking Biological Weapon Fallout") # set title
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=1)

def stop():
    """
    Function to top the GUI running and close the model window
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
    """
    Sets slider values to the defaults specified by the assignment brief
    """
    eastscale.set(75)     
    southscale.set(10)   
    northscale.set(10)   
    westscale.set(5)
    heightscale.set(255)
    bacteriascale.set(5000)
    
def reset_slider():
    """
    Sets slider values to 0
    """
    eastscale.set(0)     
    southscale.set(0)   
    northscale.set(0)   
    westscale.set(0)
    heightscale.set(0)
    bacteriascale.set(0)
        

##Create slider bars
northscale = tkinter.Scale(root, label = "North", from_=0,command=lambda _: north_max(northscale.get()), orient = 'horizontal', length = 200)
northscale.pack()
southscale = tkinter.Scale(root, label = "South", from_=0,command=lambda _: south_max(southscale.get()), orient = 'horizontal', length = 200)
southscale.pack()
eastscale = tkinter.Scale(root, label = "East", from_=0,command=lambda _: east_max(eastscale.get()), orient = 'horizontal', length = 200)
eastscale.pack()
westscale = tkinter.Scale(root, label = "West", from_=0,command=lambda _: west_max(westscale.get()), orient = 'horizontal', length = 200)
westscale.pack()

heightscale = tkinter.Scale(root, label = "Height", from_=1, to_=1000, orient = 'horizontal', length = 200)
heightscale.pack()
bacteriascale = tkinter.Scale(root, label = "Number of Bacteria", from_=1, to_=10000, orient = 'horizontal', length = 200)
bacteriascale.pack()

#GUI buttons
default_butt = tkinter.Button(root,text="Default slider Values", command=default_slider)
default_butt.pack(padx=5, pady=5,side='top')
reset_butt = tkinter.Button(root,text="Reset slider Values", command=reset_slider)
reset_butt.pack(padx=5, pady=5,side='top')
confirm_setup = tkinter.Button(root,text="Confirm Setup",fg="red", command=setup)
confirm_setup.pack(padx=5, pady=5,side='top')
run_butt = tkinter.Button(root,text="RUN",state='disabled', fg = "grey", command=update)
run_butt.pack(padx=5, pady=5,side='top')
output_butt = tkinter.Button(root,text="Create Output .txt",state='disabled', fg = "grey", command=create_output)
output_butt.pack(padx=5, pady=5,side='top')
quit_butt = tkinter.Button(root,text="QUIT", command=stop)
quit_butt.pack(padx=5, pady=5,side='top')


tkinter.mainloop() # Keep tkinter GUI window running


"""
__Development Log__
Day 1 - BASICS - Read in the data, find the cooridnates of bombing point, create random movements NESW and UpDown
Day 2 - BASIC LOOPING - create generator function to run until hits 0, create new module and move in movement functions,
    get this working with changeable num_of_bacteria var
Day 3 - Set up generator function to run iterations for each bacteria agent until height 0,
    wrote something to add one to output in location specified by bacteria_location
Day 4 - got generator function working, produced text file of output
Day 5 - added animation, update every bacteria contact with ground but very computationally expensive/takes too long so removed
Day 6 - fixing the sliders to be max 100 for all 4, usability?? this is tricky, attempting to fix
Day 7 - attempting to fix sliders again, trying a function to set maximum value instead of auto-adjust, YAY its working!
    added messagebox if sliders dont add to 100, integrated module so all in one script, tidied things up a bit and added
    some documentation/commenting, added height and bacteria number sliders and integrated to setup
Day 8 - wirintg studd and uml diagram



To do:
refresh button

add in timer to update? - time the time taken to process un the update function, print "time taken to model... X secs"

change gui so we can see the axis
change colour of output
set axis to min max x and y
print x and y ranges, max number of bacteria in one place

add text onto gui

user decide file name
"""
