import pandas as pd
import matplotlib.pyplot as plt

def plot(path):
    df = pd.read_csv(path["exp_folder"] + "fitness.log", sep=" \t ", header=3, names=["gen", "best", "avg", "worst"])

    plt.figure()

    # df.plot(x="gen", y="best")
    df.plot(x="gen")

    plt.savefig(path["exp_folder"] + "fitness" + ".png", bbox_inches='tight')
