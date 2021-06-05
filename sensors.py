import pandas as pd
import matplotlib.pyplot as plt

def plot(path):
    df = pd.read_csv(path["data_folder"] + "robotSensors", index_col=False, sep=" ", header=None, names=["t", "light", "bluelight", "redlight", "groundmemory", "redbattery"])

    fig, ax = plt.subplots(2)
    df.plot(x="t", y="light", color="tab:orange", ax=ax[0])
    df.plot(x="t", y="bluelight", color="tab:blue", ax=ax[0])
    df.plot(x="t", y="groundmemory", color="tab:brown", ax=ax[0])

    df.plot(x="t", y="redlight", color="tab:red", ax=ax[1])
    df.plot(x="t", y="redbattery", color="tab:green", ax=ax[1])
    plt.savefig(path["exp_folder"] + "sensors" + ".png", bbox_inches='tight')