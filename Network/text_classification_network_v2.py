import numpy as np

import tensorflow_datasets as tfds
import tensorflow as tf
import pandas as pd

tfds.disable_progress_bar()

import matplotlib.pyplot as plt

def plot_graphs(history, metric):
  plt.plot(history.history[metric])
  plt.plot(history.history['val_'+metric], '')
  plt.xlabel("Epochs")
  plt.ylabel(metric)
  plt.legend([metric, 'val_'+metric])


test = np.array(pd.read_csv('test.csv'))
train = np.array(pd.read_csv('train.csv'))

for example, label in train.take(1):
  print('text: ', example.numpy())
  print('label: ', label.numpy())

