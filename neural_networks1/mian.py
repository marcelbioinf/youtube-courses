import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt


data = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = data.load_data()

#print(train_images[1])

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

train_images = train_images / 255.0
test_images = test_images / 255.0

#plt.imshow(train_images[7], cmap=plt.cm.binary)
#plt.show()

#we have 60000 images in train image array. Each image is a 28x28 matrix representing pixels in a way that each value of a matrix is one pixel (28x28 values in rgb scale) nad we have 28 rows
#so now we have to flatten our data to single list so its easier to work with - it will be a 784 (28x28) sized list.
#so input layer will be contained of 784 neurons
#output layer will be 0-9 (10) because we have 10 different classes of pictures
#hidden layaer will be made of 128 neurons

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28,28)),
    keras.layers.Dense(128, activation="relu"),
    keras.layers.Dense(10, activation="softmax")
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=5)   #epoch is how many time each image from train images is fed to neural network

test_loss, test_acc = model.evaluate(test_images, test_labels)

print(f'tested accuracy: {test_acc}')

prediction = model.predict(test_images)

#print(class_names[np.argmax(prediction[0])])

plt.figure(figsize=(5,5))
for i in range(5):
    plt.grid(False)
    plt.imshow(test_images[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[test_labels[i]])
    plt.title(class_names[np.argmax(prediction[i])])
    plt.show()