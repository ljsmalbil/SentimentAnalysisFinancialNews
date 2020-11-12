# https://raw.githubusercontent.com/sinmaniphel/py_isear_dataset/master/isear.csv
import pandas as pd

from py_isear.isear_loader import IsearLoader

attributes = ['EMOT','SIT']
target = ['TROPHO','TEMPER']
loader = IsearLoader(attributes, target, True)
data = loader.load_isear('Isear.csv')
data.get_data() # returns attributes
data.get_target() # returns target
data.get_freetext_content() # returns the text content of the database

print(data)