import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px

example = np.load("./Data/mixed_samples/0healthy.npy")

print(example.shape)

initial_plot = example[0]
print(initial_plot.shape)

#plt.plot(initial_plot)
#plt.show()

df = pd.DataFrame(initial_plot)
df.columns = ['x', 'y', 'z', 'colouring']

print(df.head())

fig = px.scatter_3d(df, x='x', y='y', z='z',
              color='colouring')
fig.show()

