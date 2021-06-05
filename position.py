import pandas as pd
import numpy as np
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt

def plot(path):
    df = pd.read_csv(path["data_folder"] + "robotPosition", sep=" ", header=None, names=["t", "x", "y", "theta"])
    df_sensors = pd.read_csv(path["data_folder"] + "robotSensors", index_col=False, sep=" ", header=None, names=["t", "light", "bluelight", "redlight", "groundmemory", "redbattery"])
    df_battery = pd.read_csv(path["data_folder"] + "robotBattery", sep=" ", header=None, names=["t", "lowBattery"])

    df["color"] = np.where(df_sensors["groundmemory"]==1, "blue", "white")
    df["color"] = np.where(df_battery["lowBattery"]==1, "red", df["color"])

    bg = plt.imread("background.png")

    fig, ax = plt.subplots()
    ax.set(xlim=(-1.5, 1.5), ylim=(-1.5, 1.5))
    ax.imshow(bg, extent=[-1.5, 1.5, -1.5, 1.5])
    df.plot(kind="scatter", x="x", y="y", color=df["color"], s=0.5, colorbar=False, ax=ax)
    plt.axis('off')
    plt.savefig(path["exp_folder"] + "position" + ".png", bbox_inches='tight')