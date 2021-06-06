import pandas as pd
import matplotlib.pyplot as plt

def plot(path, name):
    df = pd.read_csv(path["exp_folder"] + "fitness.log", sep=" \t ", header=3, names=["gen", "best", "avg", "worst"], engine='python')

    plt.figure()

    # df.plot(x="gen", y="best")
    df.plot(x="gen")

    plt.savefig(path["exp_folder"] + name, bbox_inches='tight')


def plot_all(path, name, experiments):
    fig, ax = plt.subplots()
    
    for exp in experiments:
        path["exp_folder"] = path["root_folder"] + "expFiles/exp" + str(exp) + "/"
        names = ["gen", "best_exp"+str(exp), "avg_exp"+str(exp), "worst_exp"+str(exp)]
        df = pd.read_csv(path["exp_folder"] + "fitness.log", sep=" \t ", header=3, names=names, engine='python')
        df.plot(x="gen", y=names[1], ax=ax)

    plt.savefig(path["root_folder"] + "expFiles/" + name, bbox_inches='tight')
        