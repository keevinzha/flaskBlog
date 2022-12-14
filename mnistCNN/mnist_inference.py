import tensorflow as tf

INPUT_NODE = 784
OUTPUT_NODE = 10

IMAGE_SIZE = 28
NUM_CHANNELS = 1
NUM_LABELS = 10
#layer1
CONV1_DEEP = 32
CONV1_SIZE = 5            #卷积层深度
#layer2
CONV2_DEEP = 64
CONV2_SIZE = 5

def inference(input_tensor, train, regularizer):
    with tf.variable_scope('layer1-conv1'):
        conv1_weights = tf.get_variable(
            "weight", [CONV1_SIZE, CONV1_SIZE, NUM_CHANNELS, CONV1_DEEP],
            initializer=tf.truncated_normal_initializer(stddev=0.1)
        )
        conv1_biases=tf.get_variable(
            "biases", [CONV1_DEEP], initializer=tf.constant_initializer(0.0)
        )
        conv1 = tf.nn.conv2d(
            input_tensor, conv1_weights, strides=[1, 1, 1, 1], padding='SAME'
        )
        relu1 = tf.nn.relu(tf.nn.bias_add(conv1_biases))#bias_add手动传播

    with tf.variable_scope('layer-pool1'):
        pool1 = tf.nn.max_pool(
            relu1, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME'
        )

    with tf.variable_scope('layer-conv2'):
        conv2_weights = tf.get_variables(
            'weight',

        )