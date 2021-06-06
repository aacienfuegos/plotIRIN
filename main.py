import os, subprocess
import json
import shutil, tempfile
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
            
def get_pfile(run_time):
    global path
    fd, temp_path = tempfile.mkstemp()
    pfile = path["exp_folder"] + "iriNeuronTesting.txt"
    shutil.copy(pfile, temp_path)

    # sed -i "s/RUN TIME.*/RUN TIME = 160/g" iriNeuronTesting.txt
    cmd = "sed -i 's/RUN TIME.*/RUN TIME = "+str(run_time) + "/g' "+temp_path
    os.system(cmd)
    
    return  fd, temp_path

def sim(exp_type, pfile):
    global path
    # ./irsim -v -E 21 -p expFiles/exp1/plot_param.txt -c expFiles/exp1/currentbest
    command = ["./irsim", "-v", "-E", str(exp_type),
                "-p", pfile,
                "-c", path["exp_folder"]+"currentbest"]
    p = subprocess.Popen(command, cwd=path["root_folder"])
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
    experiments = data["experiments"]
    run_time = data["run_time"]

    for exp in experiments:
        set_path(exp)
        clean()
        pfile, pfile_path = get_pfile(run_time)
        sim(exp_type[exp], pfile_path)

        fitness.plot(path)
        position.plot(path)
        sensors.plot(path)

    fitness.plot_all(path, experiments)
    
        
        
if __name__ == "__main__":
    main()