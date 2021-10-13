import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
data=pd.read_csv('Iris.csv')
print(data.head())
X=data.drop(['Id','Species'],axis=1)
y=data['Species']

from sklearn.ensemble import RandomForestClassifier

model=RandomForestClassifier(n_estimators=200)

model.fit(X,y)

pickle.dump(model, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))

print(model.predict([[4.2,3.2,1.7,0.9]]))

