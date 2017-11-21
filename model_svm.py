import os
import joblib as jl
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.linear_model import LogisticRegression


files = os.listdir('dataset/')
x_data = []
y_data = []
for f in files:
    dataset = jl.load( os.path.join('dataset/', f) )
    x_data += dataset['x']
    y_data += dataset['y']


x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.2, random_state=42)
x_train, x_test, y_train, y_test = np.array(x_train), np.array(x_test), np.array(y_train), np.array(y_test)    


model = LogisticRegression()
model.fit(x_train, y_train)
score_test=model.score(x_test, y_test)


with open('log_svm.txt', 'w') as fw:
    fw.write('score_test:{0}\n'.format(score_test))



