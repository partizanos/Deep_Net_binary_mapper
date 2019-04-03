import helpers
# print("Deep Net Binary Mapper")
folder_original = helpers.cwd()  + "/codes/original";
folder_modified = helpers.cwd()  + "/codes/modified";


import numpy as np
from PIL import Image
def readImage(folderAbsolutePath: str, fileName: str) -> np.array:
    im = Image.open(folder + "/" fileName)
    p = np.array(im)
    return im

# map original to modified

# Each binary symbol is formed by 6 × 6 pixels.

# from tensorflow.keras.models import Sequential
#
# model = Sequential()
#
# TODO tensorflo.keras
# from keras.layers import Dense
#
# model.add(Dense(units=64, activation='relu', input_dim=100))
# model.add(Dense(units=10, activation='softmax'))
#
#
# model.compile(loss='categorical_crossentropy',
#               optimizer='sgd',
#               metrics=['accuracy'])
#
# # model.compile(loss=keras.losses.categorical_crossentropy,
# #               optimizer=keras.optimizers.SGD(lr=0.01, momentum=0.9, nesterov=True))
#
# # x_train and y_train are Numpy arrays --just like in the Scikit-Learn API.
# model.fit(x_train, y_train, epochs=5, batch_size=32)
