# make a prediction for a new image.
from numpy import argmax
import tensorflow as tf
# from keras.preprocessing import image
# from keras.utils import load_img, img_to_array
from keras.models import load_model

# load and prepare the image
def load_image(filename):
  
  img = tf.keras.utils.load_img(filename,  grayscale=True, target_size=(28, 28))
  img = tf.keras.utils.img_to_array(img)
#   try:
#     img = load_img(filename,  grayscale=True, target_size=(28, 28))
#     img = img_to_array(img)
#   except Exception as e:
#     img = image.load_img(filename,  grayscale=True, target_size=(28, 28))
#     img = image.img_to_array(img)
	# reshape into a single sample with 1 channel
  img = img.reshape(1, 28, 28, 1)
  # prepare pixel data
  img = img.astype('float32')
  img = img / 255.0
  return img

# load an image and predict the class
def detection(image_path):
  # load the image
  img = load_image(image_path)
  # load model
  model = load_model('final_model.h5')
  # predict the class
  predict_value = model.predict(img)
  digit = argmax(predict_value)
  print(digit)
  
  return digit
