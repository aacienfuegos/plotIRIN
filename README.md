# Plot IRIN
This is a small program written in python to plot some stuff for one of my classes IRIN. 
It uses pandas, matplotlib and numpy.

## First Run
The first time you run the program it will prompt you for the path of the simulator, the experiments you want to plot and the run time to simulate.


After you enter the data, it will create a json file, which will use for the following executions.
If you want to change this data you can either change the json file or delete it and the program will prompt you to introduce the data again

## Directory Structure
Experiments MUST be saved inside the simulator folder using the following structure:
```
irsim
├── expFiles
    ├── exp1
        ├── best
        │   ├── best1000.log
        ├── currentbest
        ├── fitness.log
        ├── iriNeuronTesting.txt
```

## Graphs
At the moment these functions are availible:
* Fitness:
 
    It will plot the best, the average and the worst fitness of each generation using the file _fitness.log_


    Also, there is a graph with the best fitness of each experiment
* Position:

    Plot a map of the scenarion with the positions of the robot. 
* Sensors
   1. Light Sensor, Blue Light Sensor and Ground Memory
   2. Red Light Sensor and Red Battery