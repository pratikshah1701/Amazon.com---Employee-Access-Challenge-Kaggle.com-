import pandas as pd


import pandas as pd
import matplotlib.pyplot as plt

df_train= pd.read_csv('https://raw.githubusercontent.com/vidushidikshit/Machine_Learning/master/train_amazon.csv')
#df_train
df_threshold = pd.read_csv('0.3.csv')
#print(df_threshold)
df_threshold.plot(x='RESOURCE', y='ACTION', style='ro')
df_train.plot(x='RESOURCE', y='ACTION', style='o')


plt.show()
