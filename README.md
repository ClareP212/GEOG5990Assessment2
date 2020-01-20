# GEOG5990 Assessment 2
This is *Assessment 2* of *GEOG5990*, for student number __200931617__. The code in this repository is a model of bacterial weapon fallout given user-specified wind direction probabilities, height and number of bacteria.
The code can produce a .txt array of where the bacteria from the model landed.

### Repository Contents
- LICENSE
- README.md
- assessment2.py
- wind.raster

## Getting Started
install python

install anaconda (optional)

## Running the Model
### Running from spyder
- open assessment2.py in spyder
- press run button for assessment2 script

### Running from Command Prompt
 - Open Command Prompt
 - navigate to the directory to where the model files are stored
 - enter 'python assessment2.py'
 
### GUI
- select bacteria number, release height and the probability of each wind direction (north, south, east and west). The total should sum to 100% (max values will change so a sum greater than 100 cannot occur).
- press the confirm setup button, this will print the wind probabilities, height and number of bacterie selected. If total wind probabilities sums to below 100, a message box will appear asking to ammend the wind sliders.
- press the RUN button.
- enjoy!
- press the output.txt button if you with to create a txt containing an array of the outputs.
- press the QUIT button when you wish to close the animation window, you may also need to stop the kernel (with the stop button) and close the figure pop up screen (via usual x on top right window).

### Expected Outputs
TBC

### Checks
TBC

###Known Issues
- sliders go a bit weird sometimes

## ToDo
TBC

## License
[Click Here for License](https://github.com/ClareP212/GEOG5990Assessment2/blob/master/LICENSE)

## Acknowledgements
Some base code from:
https://www.geog.leeds.ac.uk/courses/computing/study/core-python/
