import tensorflow.compat.v1 as tf

tf.disable_v2_behavior()

x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)

z = x + y

session = tf.Session()

values = {x: 5.0, y: 4.0}

result = session.run([z], values)
print(result)
