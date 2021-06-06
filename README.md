# Plot IRIN
This is a small program written in python to plot some stuff for one of my classes IRIN. 
It uses pandas, matplotlib and numpy.

## First Run
The first time you run the program it will prompt you for the path of the simulator and the experiments you want to plot.
After you enter the data, it will create a json file, which will use for the following executions.

# Directory Structure
Experiments MUST be saved inside the simulator folder using the following structure:
```
irsim
├── expFiles
    ├── best
    │   ├── best1000.log
    │   ├── best200.log
    │   ├── best2000.log
    │   ├── best4000.log
    │   ├── best500.log
    │   ├── best5000.log
    │   ├── best6000.log
    │   └── best8000.log
    ├── currentbest
    ├── fitness.log
    ├── fitness.png
    ├── iriNeuronTesting.txt
    ├── position.png
    └── sensors.png
```