import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
import xgboost as xg

# прочитываем данные
weather_data = pd.read_csv('data (1)/температура.csv',sep=';')

print(weather_data.info())

homes_harr = pd.read_csv('data (1)/характеристики_домов.csv',sep=';')

print(homes_harr.info())

volume_of_heat = pd.read_csv('data (1)/объём_теплоты.csv',sep=';')

volume_of_heat = volume_of_heat.drop(volume_of_heat[volume_of_heat['is_unreliable'] == 0].index)
print(volume_of_heat.info())

# объединяем данные по одному признаку
data = pd.merge(volume_of_heat, homes_harr, on='address_uuid', how='inner')

# обрабатываем для объединения по дате
weather_data['date_start'] = pd.to_datetime(weather_data['date_start'])
weather_data['date'] = weather_data['date_start'].dt.date
weather_data = weather_data.drop(['date_start','date_end'],axis=1)

data['date'] = pd.to_datetime(data['date'])
weather_data['date'] =  pd.to_datetime(weather_data['date'])

# объединяем
final_data = pd.merge(data, weather_data, on='date', how='inner')


# сохраняем
final_data.to_csv('final.csv')

# обрабока финального датасета
print(final_data.isna().sum())

final_data['temp'] = final_data['temp'].str.replace(',', '.').astype(float)
final_data['temp_max'] = final_data['temp_max'].str.replace(',', '.').astype(float)
final_data['temp_min'] = final_data['temp_min'].str.replace(',', '.').astype(float)
print(final_data.isna().sum())
final_data = final_data.dropna()
# фичи и лейблы для обучения

X = final_data
X = X.drop(['address_uuid','is_unreliable','value'],axis=1)

# обработка даты
X['date'] = pd.to_datetime(X['date'])
X['year'] = X['date'].dt.year
X['month'] = X['date'].dt.month
X['day'] = X['date'].dt.day

X = X.drop(['date'], axis=1)

# обработка типа стены
dummies = pd.get_dummies(X['wall_type'], prefix='wall_type')

X = pd.concat([X, dummies], axis=1)

X = X.drop('wall_type', axis=1)

y = final_data['value']

print(X.info())

model = xg.XGBRegressor(n_estimators=1000, max_depth=100, eta=0.1, subsample=0.7, colsample_bytree=0.8)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=123)

# Обучение модели
model.fit(X_train, y_train)


predictions = model.predict(X_test)
df = metrics.mean_absolute_error(y_test,predictions)

print(df)