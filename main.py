import os, subprocess
import fitness, position, sensors

exp_type = [None]
for i in range(10): exp_type.append(21)
for i in [8,10]: exp_type[i] = 24

def get_path(exp):
    home = os.getenv("HOME") + "/"
    path = {
        "root_folder" : home + "uni/IRIN/compulsory_2/evolutionIRIN/",
    }
    path["exp_folder"] = path["root_folder"] + "expFiles/exp" + str(exp) + "/"
    path["data_folder"] = path["root_folder"] + "outputFiles/"
    
    return path

def clean(path):
    for f in os.listdir(path["data_folder"]):
        if(f != "README.md"):
            os.remove(path["data_folder"] + f)

def sim(path, exp_type):
    # ./irsim -v -E 21 -p expFiles/exp1/plot_param.txt -c expFiles/exp1/currentbest
    command = ["./irsim", "-v", "-E", str(exp_type),
                "-p", path["exp_folder"]+"plot_param.txt",
                "-c", path["exp_folder"]+"currentbest"]
    p = subprocess.Popen(command, cwd=path["root_folder"])
    p.wait()

def main():
    experiments = [1, 3, 7, 8]

    for exp in experiments:
        path = get_path(exp)
        clean(path)
        sim(path, exp_type[exp])

        fitness.plot(path)
        position.plot(path)
        sensors.plot(path)
        
        
if __name__ == "__main__":
    main()