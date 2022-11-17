from tensorflow import keras
from tensorflow.keras import optimizers
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing import image_dataset_from_directory
from tensorflow.keras.layers import Dense, Conv2D, Flatten, Rescaling, MaxPool2D
import cv2 as cv
import numpy as np



train_data = image_dataset_from_directory("train", validation_split=0.2, subset="training", seed=42, image_size=(200, 200), batch_size=50)

cpt = 0
class_name = train_data.class_names
num_class = 2
model = Sequential()
model.add(Rescaling(1./255, input_shape=(200, 200, 3)))
model.add(Conv2D(128, 4, activation='relu'))
model.add(MaxPool2D())
model.add(Conv2D(64, 4, activation='relu'))
model.add(MaxPool2D())
model.add(Conv2D(32, 4, activation='relu'))
model.add(MaxPool2D())
model.add(Conv2D(16, 4, activation='relu'))
model.add(MaxPool2D())
model.add(Flatten())
model.add(Dense(64, activation='relu'))
model.add(Dense(num_class, activation='softmax'))
imagman = cv.imread("train\\man\\6580.jpg")
imagwoman = cv.imread("train\\woman\\5582.jpg")
imagman = cv.resize(imagman, (200, 200))
imagwoman = cv.resize(imagwoman, (200, 200))
imgman = np.expand_dims(imagman, axis=0)
imgwoman = np.expand_dims(imagwoman, axis=0)
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['sparse_categorical_accuracy'])
print(model.summary())
print(class_name)
print(model.predict(imgman), ": man1")
print(model.predict(imgwoman), ": woman1")

print(model.predict(imgman), ": man1")
print(model.predict(imgwoman), ": woman1")
cv.imshow("man1", imagman)
cv.imshow("woman1", imagwoman)
while True:
    key = cv.waitKey(1)
    if key == ord(" "):
        break

def get_model():
    return model
if __name__ == '__main__':
    model.fit(train_data, validation_data=train_data, epochs=10)