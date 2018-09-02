import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf

a = tf.placeholder("int32")
b = tf.placeholder("int32")

y = tf.multiply(a, b)

sess = tf.Session()

print sess.run(y, feed_dict={a: 2, b: 5})
