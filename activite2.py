
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

filename = 'ajustement.csv'
data = pd.read_csv(filename, sep=';')
x = data['x']
y = data['y']
ux = data['ux']
uy = data['uy']
plt.errorbar(x, y, xerr = ux, yerr = uy, fmt = 'none', capsize = 5, ecolor = 'blue')
plt.show()

import scipy.stats as stats

