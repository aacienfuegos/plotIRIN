from asyncio.subprocess import STDOUT
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
    bg = path["root_folder"] + "frame/frame0001.ppm"
    cmd = "convert " + bg + " -gravity center -crop 774x774+0+0 +repage " + temp_path
    os.system(cmd)
    
    return fd, temp_path
    

def sim(exp_type, seed, pfile):
    global path
    
    DEVNULL = open(os.devnull, 'wb')
    
    # ./irsim -v -s 12341231 -E 21 -p expFiles/exp1/plot_param.txt -c expFiles/exp1/currentbest
    command = ["./irsim", "-v",
                "-s", str(seed),
                "-E", str(exp_type),
                "-p", pfile,
                "-c", path["exp_folder"]+"currentbest"
                ]
    p = subprocess.Popen(command, cwd=path["root_folder"], stdout=DEVNULL, stderr=STDOUT)
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
        clean()

        pfile, pfile_path = get_pfile(run_time, 0)
        bg, bg_path = get_bg()

        sim(exp_type[exp], seed, pfile_path)

        fitness.plot(path, names["fitness"])
        position.plot(path, names["position"], bg_path)
        sensors.plot(path, names["sensors"])

        os.close(pfile)
        os.close(bg)

    fitness.plot_all(path, names["fitness_all"], experiments)
    
        
        
if __name__ == "__main__":
    main()