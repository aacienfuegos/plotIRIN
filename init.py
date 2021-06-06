import os, json

def init_root_folder():
    root_folder = input("Enter path of the simulator: ")
    if(root_folder[-1]!='/'): root_folder += '/'
    if(os.path.isfile(root_folder+"irsim")):
        return root_folder
    else:
        print("Simulator not found")
        init_root_folder()

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
    
            

def init_data():
    root_folder = init_root_folder()
    root_folder = "/home/aacienfuegos/uni/IRIN/compulsory_2/evolutionIRIN/"
    experiments = init_experiments()
    run_time = init_run_time()
            
    data_dict = {
        "path" : {
            "root_folder" : root_folder
        },
        "experiments" : experiments,
        "run_time" : run_time
    }
    with open("data.json", 'w') as data:
        json.dump(data_dict, data, indent=4, sort_keys=True)