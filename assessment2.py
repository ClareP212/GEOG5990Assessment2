# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 17:36:10 2019
@author: gy15cep
Student number 200931617

Assesment 2 of GEOG5990: Programming for Geographical Information Analysts: Core Skills

Tracking biological weapon fallout

Note
If not already enabled in spyder, run the below command in the spyder console to make a pop up window for the GUI
alternatively, this can be toggled in settings by going into tools>preferences>Ipython console>Graphics and selecting 'tkinter' in the Graphics backend section.
%matplotlib qt
"""
#importing libraries
import matplotlib
matplotlib.use('TkAgg')
import tkinter
import tkinter.messagebox
import random

#open raster file containing bomb location and find the x y coordinated of bomb point
ground_zero = []
row_count = -1

f = open("wind.raster") # open file
for row in f: 
    row_count = row_count +1
    parsed_line = str.split(row,",") # split each row at comma
    data_line = []
    for value in parsed_line:
        data_line.append(float(value)) # change each value to a float
    #print(sum(data_line))
    if sum(data_line) >0: # if the sum of the row is more than 0
        start_x = data_line.index(255) #note the x value of the 255
        start_y = row_count # note the y value of the row
    ground_zero.append(data_line)
f.close()

print("Bomb point x = " + str(start_x) + " , y = " + str(start_y))

##Check row and column numbers of file read in
#print ("rowno = " + str(len(ground_zero)))
#print ("colno = " + str(len(ground_zero[0])))


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
    north_perc = (northscale.get()/100) #global variable of north scale value, from GUI slider.
    global south_perc
    south_perc = (southscale.get()/100) #global variable of south scale value, from GUI slider.
    global east_perc
    east_perc = (eastscale.get()/100) #global variable of east scale value, from GUI slider.
    global west_perc
    west_perc = (westscale.get()/100) #global variable of west scale value, from GUI slider.
    
    global height
    height = (heightscale.get()) #global variable of height scale value, from GUI slider.
    
    global num_of_bacteria
    num_of_bacteria = (bacteriascale.get()) #global variable of bacteria number scale value, from GUI slider.
    
    global output_res
    output_res = (outputscale.get()) #global variable of bacteria number scale value, from GUI slider.

    if 1 == (north_perc + south_perc + east_perc + west_perc):
        print ("Chance of going South = " + str(west_perc*100) + "%")
        print ("Chance of going East = " + str(east_perc*100) + "%")  
        print ("Chance of going South = " + str(south_perc*100) + "%") 
        print ("Chance of going North = " + str(north_perc*100) + "%")
        print ("Height = " + str(height))
        print ("Number of Bacteria = " + str(num_of_bacteria))
        print ("Output Size = " + str(output_res) + "x" + str(output_res))
        
        global bacteria
        bacteria = []
        for i in range(num_of_bacteria):
            bacteria.append(Bacteria(height,start_y,start_x,north_perc,south_perc,east_perc,west_perc))
        run_butt.configure(state='normal',fg = "red")

    else:
        tkinter.messagebox.showerror("Wind Direction Probabilities","Wind direction probabilities do not add to 100%, please ammend sliders")

##Create agents and define their behaviours
class Bacteria() :
    def __init__ (self,height,y,x,north_perc,south_perc,east_perc,west_perc):
        """
        Function to initiate the bacteria agent, feeds in x, y, height and wind direction proportions from sliders.
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
        """
        Function to move agents according to the wind direction probabilities and turbulance.
        
        Params:
            height - the initial height the bacteria are starting at, defined by the user via the height slider in the GUI.
            y - y variable defining the y-coordinate of the bacterial bomb start location.
            x - x variable defining the x-coordinate of the bacterial bomb start location.
            north_perc - the probability of the bacteria moving northwards in any one movement, defined by the user via the north slider in the GUI. 
            south_perc - the probability of the bacteria moving southwards in any one movement, defined by the user via the south slider in the GUI.
            east_perc - the probability of the bacteria moving eastwards in any one movement, defined by the user via the east slider in the GUI.
            west_perc - the probability of the bacteria moving westwards in any one movement, defined by the user via the west slider in the GUI.

        """
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
    #create an empty output array
    global output
    output = []
    for row in range(output_res):
        col = []
        for i in range (output_res):
            col.append(0)
        output.append(col) 
            
    #Model bacteria movement until they hit ground (height = 0)
    global carry_on
    global out_of_range
    out_of_range = 0
    for i in range(num_of_bacteria): #for each bacteria
        carry_on = True
        #bacteria[i].check()
        for j in gen_function(): 
            bacteria[i].move() #move according to the wind directions and turbulance chance
            if bacteria[i].height == 0: # when height reaches 0
                if bacteria[i].y > (150 + (output_res/2)) or bacteria[i].x > (50 + (output_res/2)) or bacteria[i].y < (150 - (output_res/2)) or bacteria[i].x < (50 - (output_res/2)):
                    #if outside of limits, add one to out_of_range count
                    out_of_range = out_of_range + 1
                else:
                    #if not, add one at the coordinate of the output file where the bacteria landed
                    output[bacteria[i].y][bacteria[i].x] = output[bacteria[i].y][bacteria[i].x] + 1      
                carry_on = False # stop generator function, move on to next bacteria     
    
    #enable the output creation button
    output_butt.configure(state='normal', fg = "black")
    
    ##plot the output in the GUI
    matplotlib.pyplot.imshow(output, cmap = 'Greens')
    matplotlib.pyplot.xlim([(50 - (output_res/2)),(50 + (output_res/2))]) 
    matplotlib.pyplot.ylim([(150 - (output_res/2)),(150 + (output_res/2))])
    matplotlib.pyplot.axhline(y=150)
    matplotlib.pyplot.axvline(x=50)
    matplotlib.pyplot.tight_layout()
    canvas.draw()
    print("xmin =" + str((50 - (output_res/2))) + "xmax =" + str((50 + (output_res/2))))   
    print("ymin =" + str((150 - (output_res/2))) + "ymax =" + str((150 + (output_res/2))))   
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
fig = matplotlib.pyplot.figure(figsize=(7, 7), dpi = 100)
ax = fig.add_axes([0.05, 0.05, 0.9, 0.9])

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
        value - value of south slider
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
northscale = tkinter.Scale(root, label = "North", from_=0,command=lambda _: north_max(northscale.get()), orient = 'horizontal', length = 150)
northscale.pack()
southscale = tkinter.Scale(root, label = "South", from_=0,command=lambda _: south_max(southscale.get()), orient = 'horizontal', length = 150)
southscale.pack()
eastscale = tkinter.Scale(root, label = "East", from_=0,command=lambda _: east_max(eastscale.get()), orient = 'horizontal', length = 150)
eastscale.pack()
westscale = tkinter.Scale(root, label = "West", from_=0,command=lambda _: west_max(westscale.get()), orient = 'horizontal', length = 150)
westscale.pack()

heightscale = tkinter.Scale(root, label = "Height", from_=1, to_=500, orient = 'horizontal', length = 150)
heightscale.pack()
bacteriascale = tkinter.Scale(root, label = "Number of Bacteria", from_=1, to_=10000, orient = 'horizontal', length = 150)
bacteriascale.pack()
outputscale = tkinter.Scale(root, label = "Size of output file", from_=300, to_=800, orient = 'horizontal', length = 150, resolution=100)
outputscale.set(700)
outputscale.pack()

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

