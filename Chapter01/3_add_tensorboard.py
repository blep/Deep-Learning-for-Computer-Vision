from pathlib import Path
import tensorflow.compat.v1 as tf

tf.disable_v2_behavior()

LOG_DIR = Path(__file__).parent / 'training-log'

x = tf.placeholder(tf.float32, name='x')
y = tf.placeholder(tf.float32, name='y')
z = tf.add(x, y, name='sum')
session = tf.Session()
summary_writer = tf.summary.FileWriter(LOG_DIR, session.graph)
summary_writer.flush()
