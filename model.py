# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

df = pd.read_csv('s.csv', sep='\t')
input = df.drop('Test_result', axis='columns')
target = df['Test_result']
input1 = input.drop(['Question','Clear marks'], axis='columns')
from sklearn import tree
model = tree.DecisionTreeClassifier()
model.fit(input1, target)
model.score(input1, target)


import pickle
from sklearn.externals import joblib
joblib.dump(model, 'model_joblib.pkl')
mp = joblib.load('model_joblib.pkl')