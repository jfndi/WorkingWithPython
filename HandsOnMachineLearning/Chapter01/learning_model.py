import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
from sklearn.linear_model import LinearRegression

#
# Download and prepare the data.
#
data_root = os.path.dirname(os.path.abspath(__file__))
lifesat = pd.read_csv(data_root + "\\lifesat.csv")
X = lifesat[["GDP per capita (USD)"]].values
y = lifesat[["Life satisfaction"]].values

#
# Visualize the data.
#
print("Plotting")
lifesat.plot(kind='scatter', grid=True,
             x="GDP per capita (USD)", y="Life satisfaction")
plt.axis([23_500, 62_500, 4, 9])
plt.show()

#
# Select a linear model.
#
model = LinearRegression()

#
# Train the model.
#
model.fit(X, y)

#
# Make a prediction.
#
X_new = [[37_655.2]]
print(model.predict(X_new))
