from asyncio.subprocess import STDOUT
import os, subprocess
import json
import shutil, tempfile

from numpy import append
import init
import fitness, position, sensors

exp_type = [None]
for i in range(10): exp_type.append(21)     # static
for i in [8,10]: exp_type[i] = 24   # dynamic


def set_path(exp):
    global path
    # path = {"root_folder" : home + "uni/IRIN/compulsory_2/evolutionIRIN/"}
    path["exp_folder"] = path["root_folder"] + "expFiles/exp" + str(exp) + "/"
    path["data_folder"] = path["root_folder"] + "outputFiles/"

def clean():
    global path
    for f in os.listdir(path["data_folder"]):
        if(f != "README.md"):
            os.remove(path["data_folder"] + f)
    for f in os.listdir(path["root_folder"] + "frame/"):
        if(f != "README.md"):
            os.remove(path["root_folder"] + "frame/" + f)
            
def get_pfile(run_time, random):
    global path
    fd, temp_path = tempfile.mkstemp()
    pfile = path["exp_folder"] + "iriNeuronTesting.txt"
    shutil.copy(pfile, temp_path)

    # sed '/RUN TIME/ s/[^=]\{1,\}$/ 160/; /RANDOM POSITION/ s/[^=]\{1,\}$/ 1/;'
    cmd = "sed -i '"
    cmd += "/RUN TIME/ s/[^=]\{1,\}$/ " + str(run_time) + "/; "
    cmd += "/RANDOM POSITION/ s/[^=]\{1,\}$/ " + str(random) + "/;"
    cmd += "' " + temp_path
    os.system(cmd)
    
    return  fd, temp_path

def get_bg():
    global path
    fd, temp_path = tempfile.mkstemp()
    
    # shutil.copy("background.png", temp_path)
    bg = path["root_folder"] + "frame/frame0002.ppm"
    cmd = "convert " + bg + " -gravity center -crop 774x774+0+0 +repage " + temp_path
    os.system(cmd)
    
    return fd, temp_path
    

def sim(exp_type, seed, render, run_time, random):
    global path
    clean()

    pfile, pfile_path = get_pfile(run_time, random)
    
    DEVNULL = open(os.devnull, 'wb')
    
    # ./irsim -v -s 12341231 -E 21 -p expFiles/exp1/plot_param.txt -c expFiles/exp1/currentbest
    command = ["./irsim"]
    if(not render): command.append("-v")
    command.extend(["-s", str(seed),
                    "-E", str(exp_type),
                    "-p", pfile_path,
                    "-c", path["exp_folder"]+"currentbest"
                    ])
                
    p = subprocess.Popen(command, cwd=path["root_folder"], stdout=DEVNULL, stderr=DEVNULL) 
    p.wait()

def main():
    global path

    try:
        with open("data.json") as f: data = json.load(f)
    except IOError:
        init.init_data()
        with open("data.json") as f: data = json.load(f)
    finally:
        f.close()
        
    path = data["path"]
    names = data["names"]
    experiments = data["experiments"]
    run_time = data["run_time"]
    seed = data["seed"]


    for exp in experiments:
        set_path(exp)

        for random in range(2):
            # Get bg image
            sim(exp_type[exp], seed, True, 0.1, random)
            bg, bg_path = get_bg()

            # Simulate exp
            sim(exp_type[exp], seed, False, run_time, random)
            filename = "position" 
            if(random): filename += "_random"
            position.plot(path, names[filename], bg_path)
            
            if(not random): sensors.plot(path, names["sensors"])

        fitness.plot(path, names["fitness"])

        os.close(bg)

    # fitness.plot_all(path, names["fitness_all"], experiments)
    
        
        
if __name__ == "__main__":
    main()