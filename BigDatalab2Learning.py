import pandas as pd
import numpy as np
from skimage import io
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor

#подготовка данных
photos_path = 'C:/Users/NULS/Desktop/xhtym/projects/BigDatalab/photos/'

dataset = pd.read_csv('lab2Data.csv')

images = []
x = []

# #формирование x
for file in dataset['filename']:
    image = io.imread(f'photos/{file}')

    arr = np.array(image)
    x.append(np.reshape(arr, (1, 400 * 400 * 3))[0])

y = dataset['value'].values


X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

bst = XGBRegressor(learning_rate=0.1, n_estimators=100, objective='reg:linear')
bst.fit(X_train, y_train)

y_pred = bst.predict(X_test)
predictions = [round(value) for value in y_pred]

accuracy = accuracy_score(y_test, predictions)
print("Accuracy: %.2f%%" % (accuracy * 100.0))