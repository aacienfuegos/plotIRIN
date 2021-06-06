# Plot IRIN
This is a small program written in python to plot some stuff for one of my classes IRIN. 
It uses pandas, matplotlib and numpy.

## First Run
The first time you run the program it will prompt you for the path of the simulator and the experiments you want to plot.
After you enter the data, it will create a json file, which will use for the following executions.

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
⋅⋅⋅It will plot the best, the average and the worst fitness of each generation using the file _fitness.log_