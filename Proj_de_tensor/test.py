import tensorflow as tf
from tensorflow import keras
import requests

print(tf.__version__)
print(keras.__version__)
r=requests.get('https://coreyms.com')
print(r.ok)

real=constant([1, 5])
imag=constant([2, 4])
cmpx=tf.complex(real, imag)
print(cmpx.args)
