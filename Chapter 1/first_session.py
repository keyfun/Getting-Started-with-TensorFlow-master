# first_session.py
import os

import tensorflow as tf

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# a simple Python code
x = 1
y = x + 9
print(y)

x = tf.constant(1, name='x')
y = tf.Variable(x + 9, name='y')
print(y)
