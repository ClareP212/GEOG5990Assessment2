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
- select bacteria number, release height, output resolution and the probability of each wind direction (north, south, east and west). The sum of all four wind directions should equal to 100%.
- press the confirm setup button, if total wind probabilities sums to below 100, a message box will appear asking to ammend the wind sliders.
- press the RUN button.
- wait and enjoy!
- press the output.txt button if you wish to create a txt containing an array of the outputs.
- press the QUIT button when you wish to close the animation window, you may also need to stop the kernel (with the stop button) and close the figure pop up screen (via usual x on top right window).

### Expected Outputs
- x and y of bombing point location printed in console
- When wind sliders are moved, the max values will change so a sum greater than 100 cannot occur.
- When the confirm setup button is pressed, if wind probabilities sum to 100% the run button is enabled and the wind probabilities, height and number of bacteria selected will print in the console. If total wind probabilities sums to below 100, a message box will appear asking user to ammend the wind sliders.
- After Run button is pressed the output.txt button is enabled and the model runs, displaying the output in the GUI and the number of bacteria that fell outside of the area is printed in the console.
- When the output.txt button is pressed, a .txt file is created containing a numerical array of the outputs. A message confirming this has been created prints in the console.
- QUIT button closes the GUI window.

### Known Issues
- sliders occasionally get stuck on 0, need to stop and restart the programme and it will work again.
- smaller heights and larger output sizes result in small bacteria spread on image displayed in GUI

## Future Development
- refresh button within the GUI so the user does not have to close GUI and rerun the programme if they want to try new parameters.
- user decides file name and directory

## License
[Click Here for License](https://github.com/ClareP212/GEOG5990Assessment2/blob/master/LICENSE)

## Acknowledgements
Some base code from:
https://www.geog.leeds.ac.uk/courses/computing/study/core-python/
