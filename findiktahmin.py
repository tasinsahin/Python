import pandas as pd
from neuralprophet import NeuralProphet
import matplotlib.pyplot as plt

# CSV dosyasını okuyun
file_path = "path/to/your/file.csv"
data = pd.read_csv(file_path)

# 'ds' ve 'y' sütunlarını seçin
# 'ds' zaman damgasını ve 'y' sıcaklık değerini içermelidir
df = data[['dt_iso', 'temp']].rename(columns={'dt_iso': 'ds', 'temp': 'y'})

# NeuralProphet modelini oluşturun
model = NeuralProphet()

# Modeli eğitin
model.fit(df, freq="D")  # Frekansı, verinizin zaman aralığına uygun olarak ayarlayın

# Gelecekteki tarih aralığını belirtin (örneğin, 365 gün sonrası)
future = model.make_future_dataframe(df, periods=365)

# Tahminleri yapın
forecast = model.predict(future)

# Tahminleri ve gerçek verileri görselleştirin
fig = model.plot(forecast)
plt.show()
