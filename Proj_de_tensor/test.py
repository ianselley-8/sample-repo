import tensorflow as tf
from tensorflow import keras
import requests

print(tf.__version__)
print(keras.__version__)
r=requests.get('https://coreyms.com')
print(r.ok)
