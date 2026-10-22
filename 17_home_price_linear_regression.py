import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
# Create a local dataset
df = pd.DataFrame({
    'area': [1000, 1200, 1500, 1800, 2000,
             2200, 2500, 2800, 3000, 3200,
             3500, 3800, 4000, 4200, 4500,
             4800, 5000, 5200, 5500, 6000],
    'price': [150000, 180000, 225000, 270000, 300000,
              330000, 375000, 420000, 450000, 480000,
              525000, 570000, 600000, 630000, 675000,
              720000, 750000, 780000, 825000, 900000]
})
print("Home Price Dataset:")
print(df.head(5))
X = df[['area']]
y = df['price']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
reg = linear_model.LinearRegression()
reg.fit(X_train, y_train)
y_pred = reg.predict(X_test)
print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))
print("R2 score:", r2_score(y_test, y_pred))
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
# Plot 1: Regression Line
reg.fit(X, y)
plt.figure(figsize=(8, 5))
plt.scatter(df['area'], df['price'], color='green',
            marker='D', label='Actual Prices')
plt.plot(df['area'], reg.predict(X), color='red',
         label='Regression Line')
plt.title('Home Price Prediction using Linear Regression')
plt.xlabel('Area')
plt.ylabel('Price')
plt.legend()
plt.grid()
plt.show()
# Plot 2: Prediction Errors
errors = y_test - y_pred
plt.figure(figsize=(8, 5))
plt.scatter(y_pred, errors, color='purple')
plt.axhline(y=0, color='red', linestyle='--')
plt.title('Prediction Errors')
plt.xlabel('Predicted Price')
plt.ylabel('Error')
plt.grid()
plt.show()
# Predict prices for new areas
area_df = pd.DataFrame({
    'area': [1000, 1600, 2100, 3300, 5000, 6500]
})
area_df['prices'] = reg.predict(area_df[['area']])
print("\nPredicted Home Prices:")
print(area_df)
