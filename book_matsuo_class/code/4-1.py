import numpy as np
import scipy as sp
import pandas as pd
from pandas import DataFrame, Series


import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

np.random.seed(0)

dice_data = np.array([1,2,3,4,5,6])
print("１つだけランダムに抽出:", np.random.choice(dice_data, 1))


calc_steps = 1000

dice_rolls = np.random.choice(dice_data, calc_steps)

for i in rage(1,7):
    p = len(dice_rolls[dice_rolls==i]) / calc_steps
    print(i, 'が出る確率', p)
