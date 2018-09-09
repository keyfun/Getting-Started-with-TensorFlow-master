# handling tensors second example
import matplotlib.image as mp_image
import matplotlib.pyplot as plt
import tensorflow as tf

# STEP 1 --- PREPARE THE DATA
filename = "packt.jpeg"
input_image = mp_image.imread(filename)

# dimension
print('input dim = {}'.format(input_image.ndim))
# shape
print('input shape = {}'.format(input_image.shape))

height, width, depth = input_image.shape

plt.imshow(input_image)
plt.show()

x = tf.Variable(input_image, name='x')
model = tf.initialize_all_variables()

with tf.Session() as session:
    x = tf.transpose(x, perm=[1, 0, 2])
    session.run(model)
    result = session.run(x)

plt.imshow(result)
plt.show()
