from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import matplotlib.pyplot as plt

from generate_points import generate_data

X_train, y_train, X_test, y_test = generate_data(num_points = 20000, train_perc=20, plot=False)

model = Sequential()


