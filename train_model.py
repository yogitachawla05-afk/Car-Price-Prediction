import pandas as pd

print("Car Price Prediction Model Training Started...")

# Dataset Loading
data = pd.read_csv("car_data.csv")

print(data.head())

print("Model Training Completed.")
