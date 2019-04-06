from typing import Dict, List
from PIL import Image
import os
import numpy as np
import autoencoder

folder_original = os.getcwd() + "/codes/original/"
folder_modified = os.getcwd() + "/codes/modified/"
folders = [folder_original, folder_modified]


def readBmpImage(ImageAbsolutePath: str) -> np.array:
    im = Image.open(ImageAbsolutePath)
    p = np.array(im)
    return p


def getImagesList(folder_name: str) -> List:
    imagesFilenames: List[str] = os.listdir(folder_name)
    (imagesFilenames).sort()
    imagesFullPathNames: List[str] = [
        folder_name + im for im in imagesFilenames
    ]
    assert imagesFullPathNames[0] == folder_name + "code_dm_0001_imag.bmp"
    assert imagesFullPathNames[-1] == folder_name + "code_dm_0150_imag.bmp"

    images = [readBmpImage(im) for im in imagesFullPathNames]
    return np.array(images)

def getImagesDataModified():
    train = imagesPerFolder[folder_modified][:120]
    test = imagesPerFolder[folder_modified][120:-1]
    return (train, test)

def getImagesDataOriginal():
    train = imagesPerFolder[folder_original][:120]
    test = imagesPerFolder[folder_original][:-1]
    return (train, test)

imagesPerFolder: dict = {folder: getImagesList(folder) for folder in folders}

x_train = imagesPerFolder[folder_modified][:120]
x_train_test = imagesPerFolder[folder_modified][120:]
x_noise = imagesPerFolder[folder_original][:120]
x_noise_test = imagesPerFolder[folder_original][120:]

autoencoder.runAutoencoder(
    x_train,
    x_train_test,
    x_noise,
    x_noise_test
)