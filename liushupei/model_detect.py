from liushupei.preprocess.data_deal import rle_to_array, array_to_image
from PIL import Image
import pandas as pd
from keras.models import load_model
from keras import backend as K
import os


def IoU(y_true, y_pred):
    if K.max(y_true) == 0.0:
        return IoU(1 - y_true, 1 - y_pred)
    intersection = K.sum(y_true * y_pred, axis=[1, 2, 3])
    union = K.sum(y_true, axis=[1, 2, 3]) + K.sum(y_pred, axis=[1, 2, 3]) - intersection
    return 1 - K.mean(intersection / union, axis=0)


model = load_model("4_128_5.h5", custom_objects={'IoU': IoU})

results = pd.read_csv(r"E:\DataSet\airbus-ship-detection\segmentations.csv")
x, y_true = rle_to_array(Image.open(os.getcwd() + "\\data\\0a1a7f395.jpg"),
                         results["EncodedPixels"][results["ImageId"] == "0a1a7f395.jpg"])
x = x.reshape(1, 768, 768, 3) / 255
y_pre = model.predict(x)[0]
# y_pre[y_pre<0.0001]=0
# y_pre[y_pre>=0.0001]=1
array_to_image(y_true * 255, (768, 768))
array_to_image(y_pre * 255, (768, 768))

intersection = (y_true * y_pre).sum()
union = y_true.sum() + y_pre.sum()
print(intersection, union, intersection / (union - intersection))
