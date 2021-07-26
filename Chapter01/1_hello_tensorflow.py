# This was tensorflow 1.0 import:
#import tensorflow as tf

import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

hello = tf.constant('Hello, TensorFlow!')
session = tf.Session()
print(session.run(hello))
