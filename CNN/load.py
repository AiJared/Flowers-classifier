import os
import cv2
from PIL import Image
import numpy as np
# 

# 
data=[]
labels=[]
# 
# ----------------
# LABELS
# Daisy 0
# Dandelion 1
# Roses 2
# Sunflowers 3
# Tulips 4
# ----------------

# Daisy 0
daisy = os.listdir(os.getcwd() + "/CNN/data/daisy")
for x in daisy:
    imag=cv2.imread(os.getcwd() + "/CNN/data/daisy" + x)
    img_from_ar = Image.fromarray(imag, 'RGB')
    resized_image = img_from_ar.resize((180, 180))
    data.append(np.array(resized_image))
    labels.append(0)

# Dandeliion 1
dandenion = os.listdir(os.getcwd() + "/CNN/data/dandelion")
for x in dandenion:
    imag=cv2.imread(os.getcwd() + "/CNN/data/dandelion" + x)
    img_from_ar = Image.fromarray(imag, 'RGB')
    resized_image = img_from_ar.resize((180, 180))
    data.append(np.array(resized_image))
    labels.append(1)

# Roses 2
roses = os.listdir(os.getcwd() + "/CNN/data/roses")
for x in roses:
    imag=cv2.imread(os.getcwd() + "/CNN/data/roses" + x)
    img_from_ar = Image.fromarray(imag, 'RGB')
    resized_image = img_from_ar.resize((180, 180))
    data.append(np.array(resized_image))
    labels.append(2)

# Sunflowers 3
sunflowers = os.listdir(os.getcwd() + "/CNN/data/sunflowers")
for x in sunflowers:
    imag=cv2.imread(os.getcwd() + "/CNN/data/sunflowers" + x)
    img_from_ar = Image.fromarray(imag, 'RGB')
    resized_image = img_from_ar.resize((180, 180))
    data.append(np.array(resized_image))
    labels.append(3)

# Tulips 4
tulips = os.listdir(os.getcwd() + "/CNN/data/tulips")
for x in tulips:
    imag=cv2.imread(os.getcwd() + "/CNN/data/tulips" + x)
    img_from_ar = Image.fromarray(imag, 'RGB')
    resized_image = img_from_ar.resize((180, 180))
    data.append(np.array(resized_image))
    labels.append(4)


flowers=np.array(data)
labels=np.array(labels)
# 
np.save("animals",flowers)
np.save("labels",labels)