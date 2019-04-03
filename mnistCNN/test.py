import tensorflow as tf
filter_weight = tf.get_variable(
    'weights', [5, 5, 3, 16],
    initializer=tf.truncated_normal_initializer(stddev=0.1)
)
biases = tf.variable(
    'biases', [16], initializer=tf.constant_initializer(0.1)
)
'''

'''
#定义一个卷积层
conv = tf.nn.conv2d(
    input, filter_weight, strides=[1, 1, 1, 1], padding='SAME'
)
#给每一个节点添加偏置项
bias = tf.nn.bias_add(conv, biases)

actived_conv= tf.nn.relu(bias)
#ksize提供过滤器尺寸
pool = tf.nn.max_pool(actived_conv, ksize=[1, 3, 3, 1],
                      strides=[1, 2, 2, 1], padding='SAME')