import tensorflow as tf

input1=tf.placeholder(tf.float32)
input2=tf.placeholder(tf.float32)

output=tf.multiply(input1,input2)

with tf.Session() as sess:
    # placeholder 参数需要在run时动态传入
    print(sess.run(output,feed_dict={input1:[7.], input2:[3.]}))