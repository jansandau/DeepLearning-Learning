import tensorflow as tf
#tf.logging.set_verbosity(tf.logging.ERROR)

import numpy as np

celsius_q = np.array([-40, -10, 8, 15, 22, 38], dtype = float)
fahrenheit_a = np.array([-40, 14 , 48, 58, 72, 100], dtype =float)

for i, c in enumerate(celsius_q):
  print("{} degrees Celsius = {} degress Fahrenheit".format(c, fahrenheit_a[i]))

#Create Model 
model = tf.keras.Sequential([
  tf.keras.layers.Dense(units=1, input_shape=[1])

])

model.compile(loss="mean_squared_error", optimizer=tf.keras.optimizers.Adam(0.1))

history = model.fit(celsius_q, fahrenheit_a, epochs=500, verbose=False)
print("Finished")

import matplotlib.pyplot as plt

plt.xlabel('Epoch Number')
plt.ylabel('loss Magnitude')
plt.plot(history.history['loss'])