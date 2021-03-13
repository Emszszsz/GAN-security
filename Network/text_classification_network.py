import numpy as np
import os
from tflite_model_maker import configs
from tflite_model_maker import ExportFormat
from tflite_model_maker import model_spec
from tflite_model_maker import text_classifier
from tflite_model_maker import TextClassifierDataLoader
import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf
assert tf.__version__.startswith('2')
tf.get_logger().setLevel('ERROR')
plt.style.use('ggplot')


data_dir = tf.keras.utils.get_file(
      fname='SST-2.zip',
      origin='https://dl.fbaipublicfiles.com/glue/data/SST-2.zip',
      extract=True)
data_dir = os.path.join(os.path.dirname(data_dir), 'SST-2')


def replace_label(original_file, new_file):
  df = pd.read_csv(original_file, sep='\t')

  label_map = {0: 'negative', 1: 'positive'}

  df.replace({'label': label_map}, inplace=True)

  df.to_csv(new_file)

replace_label(os.path.join(os.path.join(data_dir, 'train.tsv')), 'train.csv')
replace_label(os.path.join(os.path.join(data_dir, 'dev.tsv')), 'dev.csv')

mb_spec = model_spec.get('mobilebert_classifier')

train_data = TextClassifierDataLoader.from_csv(
      filename='train.csv',
      text_column='sentence',
      label_column='label',
      model_spec=mb_spec,
      is_training=True)
test_data = TextClassifierDataLoader.from_csv(
      filename='dev.csv',
      text_column='sentence',
      label_column='label',
      model_spec=mb_spec,
      is_training=False)

model = text_classifier.create(train_data, model_spec=mb_spec, epochs=3)

#model.summary()

loss, acc = model.evaluate(train_data)
x = range(1, len(acc) + 1)
plt.plot(x, acc, 'b', label='Training acc')

config = configs.QuantizationConfig.create_dynamic_range_quantization(optimizations=[tf.lite.Optimize.OPTIMIZE_FOR_LATENCY])
config.experimental_new_quantizer = True

model.export(export_dir='mobilebert/', quantization_config=config)

model.export(export_dir='mobilebert/', export_format=[ExportFormat.LABEL, ExportFormat.VOCAB])

accuracy = model.evaluate_tflite('mobilebert/model.tflite', test_data)
print('TFLite model accuracy: ', accuracy)

new_model_spec = model_spec.get('mobilebert_classifier')
new_model_spec.seq_len = 256

new_model_spec = model_spec.AverageWordVecModelSpec(wordvec_dim=32)

new_train_data = TextClassifierDataLoader.from_csv(
      filename='train.csv',
      text_column='sentence',
      label_column='label',
      model_spec=new_model_spec,
      is_training=True)

model = text_classifier.create(new_train_data, model_spec=new_model_spec)

model = text_classifier.create(new_train_data, model_spec=new_model_spec, epochs=20)

new_test_data = TextClassifierDataLoader.from_csv(
      filename='dev.csv',
      text_column='sentence',
      label_column='label',
      model_spec=new_model_spec,
      is_training=False)

loss, accuracy = model.evaluate(new_test_data)

x = range(1, len(accuracy) + 1)
plt.plot(x, accuracy, 'b', label='Test acc')
