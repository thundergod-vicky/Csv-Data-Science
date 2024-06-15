import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

def train():
    data = pd.read_csv("employment quarter.csv")
    return data

df = train()
print(df.shape)      

def load():
    data = pd.read_csv("titenic.csv")
    return data

df = load()
print(df.shape)      

sns.boxplot(x=df["Age"])
plt.show()