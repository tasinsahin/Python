import pandas as pd
import matplotlib.pyplot as plt
import pickle

from neuralprophet import NeuralProphet

# 1. Read in Data and Process Dates
df = pd.read_csv('findik2.csv')
df.head()
df.Location.unique()
df.columns
melb = df[df['Location']=='Melbourne']
melb['Date'] = pd.to_datetime(melb['Date'])
melb.head()
plt.plot(melb['Date'], melb['Temp3pm'])
plt.show()
melb['Year'] = melb['Date'].apply(lambda x: x.year)
melb = melb[melb['Year']<=2015]
plt.plot(melb['Date'], melb['Temp3pm'])
plt.show()
data = melb[['Date', 'Temp3pm']]
data.dropna(inplace=True)
data.columns = ['ds', 'y']
data.head()

# 2. Train Model
m = NeuralProphet()
model = m.fit(data, freq='D', epochs=1000)

# 3. Forecast Away
future = m.make_future_dataframe(data, periods=900)
forecast = m.predict(future)
forecast.head()

# 4. Save Model
with open('saved_model.pkl', "wb") as f:
    pickle.dump(m, f)
del m

# Load the model
with open('saved_model.pkl', "rb") as f:
    m = pickle.load(f)
future = m.make_future_dataframe(data, periods=9000)
forecast = m.predict(future)
forecast.head()

# Plotting without GUI (to display in terminal)
plt.switch_backend('agg')

# Visualize the forecast
plot1 = m.plot(forecast)
plt2 = m.plot_components(forecast)
