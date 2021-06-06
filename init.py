import os, json

def init_root_folder():
    default = os.getenv("HOME") + "/uni/IRIN/compulsory_2/evolutionIRIN"
    root_folder = input("Enter path of the simulator [default: " + default + "]: ") or default
    if(root_folder[-1]!='/'): root_folder += '/'
    if(os.path.isfile(root_folder+"irsim")):
        return root_folder
    else:
        print("Simulator not found")
        init_root_folder()
        
def init_names():
    fitness = input("Name for fitness log graph [default: fitness.png]: ") or "fitness.png"
    fitness_all = input("Name for all fitness log graph [default: fitness_all.png]: ") or "fitness_all.png"
    position = input("Name for positions graph [default: position.png]: ") or "position.png"
    position_random = input("Name for random positions graph [default: position_random.png]: ") or "position_random.png"
    sensors = input("Name for sensors graph [default: sensors.png]: ") or "sensors.png"
    
    names = {
        "fitness" : fitness,
        "fitness_all" : fitness_all,
        "position" : position,
        "sensors" : sensors,
    }
    return names

def init_experiments():
    experiments = input("Enter experiments to run: ").split()
    try:
        experiments[:] = [int(n) for n in experiments]
        return experiments
    except ValueError:
        print("Wrond format. Remember to enter NUMBERS separate by space")
        init_experiments()
        
def init_run_time():
    run_time = input("How many seconds do you want to simulate? [default: 160]: ") or 160
    try:
        run_time = int(run_time)
        return run_time
    except ValueError:
        print("Run time must be an INTEGER number")
        init_run_time()
    
def init_seed():
    seed = input("Enter seed for random generation [default: 12341231]: ") or 12341231
    try:
        seed = int(seed)
        return seed
    except ValueError:
        print("Seed must be an INTEGER number")
        init_run_time()
    
            

def init_data():
    root_folder = init_root_folder()
    names = init_names()
    experiments = init_experiments()
    run_time = init_run_time()
    seed = init_seed()
            
    data_dict = {
        "path" : {
            "root_folder" : root_folder
        },
        "names" : names,
        "experiments" : experiments,
        "run_time" : run_time,
        "seed" : seed
    }
    with open("data.json", 'w') as data:
        json.dump(data_dict, data, indent=4, sort_keys=True)