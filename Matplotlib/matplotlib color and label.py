import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.plot([1,2,3],[4,5,6],label='SeriesA')
plt.plot([1,2,3],[6,5,4],label='SeriesB')
plt.plot([1,2,3],[5,5,5],color='purple',linestyle='--',marker='o')
plt.legend()
plt.show()
