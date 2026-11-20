import matplotlib.pyplot as plt
import numpy as np


data = np.genfromtxt('June-2021-Provo-River-Streamflow-Rates.csv', delimiter=',', dtype=str, skip_header=1)

x = data[:, 0].astype('datetime64[m]')
y_1 = data[:, 1].astype(float)
y_2 = data[:, 2].astype(float)
y_3 = data[:, 3].astype(float)
y_4 = data[:, 4].astype(float)
y_5 = data[:, 5].astype(float)


plt.plot(x, y_1, color='purple', label='10163000')
plt.plot(x, y_2, color='teal', label='10155200')
plt.plot(x, y_3, color='green', label='10155500')
plt.plot(x, y_4, color='orange', label='10154200')
plt.plot(x, y_5, color='orangered', label='10155000')
plt.title('Provo River Streamflow Data (2021)')
plt.xlabel('Date')
plt.ylabel('Flowrate (cfs)')
plt.xticks(rotation=45)
plt.legend(title='Site Numbers')
plt.grid(True)
plt.show()

