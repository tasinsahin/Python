# Gerekli kütüphaneleri içe aktarın
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Rastgele veri seti oluşturun (örnek olarak sıcaklık ve rüzgar hızı)
np.random.seed(42)
days = 100
temperature = np.random.uniform(0, 30, days)
wind_speed = np.random.uniform(0, 10, days)
humidity = np.random.uniform(0, 100, days)
precipitation = np.random.uniform(0, 10, days)
labels = temperature + 5 * wind_speed + 2 * humidity + 0.1 * precipitation + np.random.normal(0, 5, days)

# Veri setini görselleştirin
plt.scatter(temperature, labels)
plt.xlabel('Sıcaklık')
plt.ylabel('Hava Durumu Etiketi')
plt.show()

# Veri setini eğitim ve test setlerine ayırın
X = np.column_stack((temperature, wind_speed, humidity, precipitation))
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2, random_state=42)

# Random Forest Regresyon modelini oluşturun
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Test seti üzerinde tahmin yapın
predictions = model.predict(X_test)

# Modelin performansını değerlendirin
mse = mean_squared_error(y_test, predictions)
print(f'Mean Squared Error: {mse}')

# Tahminleri görselleştirin
plt.scatter(y_test, predictions)
plt.xlabel('Gerçek Etiketler')
plt.ylabel('Tahmin Edilen Etiketler')
plt.show()
