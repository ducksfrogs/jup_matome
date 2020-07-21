import numpy as np
import scipy as sp
import pandas as pd
from pandas import DataFrame, Series

import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

prob_be_data = np.array([])
coin_data = np.array([0,0,1,0,0,1,1])

for i in np.unique(coin_data):
    p = len(coin_data[coin_data == i]) / len(coin_data)
    print(i, "が出る確率", p)
    prob_be_data = np.append(prob_be_data, p)


plt.bar([0,1], prob_be_data, align='center')
plt.xticks([0,1],['head','tail'])
plt.grid(True)

np.random.seed(0)
x = np.random.binomial(30,0.5,1000)
plt.hist(x)
plt.grid(True)
