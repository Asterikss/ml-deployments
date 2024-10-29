import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.metrics import r2_score

print("Starting training")

coll_dist = pd.read_csv("CollegeDistanceCleaned.csv")

X = coll_dist.drop("score", axis=1)
y = coll_dist["score"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

def within_10_percent_accuracy(y_true, y_pred):
    tolerance = 0.1
    within_tolerance = np.abs(y_pred - y_true) <= (tolerance * np.abs(y_true))
    accuracy = np.mean(within_tolerance) * 100
    return accuracy

gbr = GradientBoostingRegressor(n_estimators=200, learning_rate=0.1, max_depth=3)
gbr.fit(X_train, y_train)

print("Training completed")

y_pred = gbr.predict(X_test)

with open("results.txt", "w") as f:
    f.write(f"MAE: {mean_absolute_error(y_test, y_pred)}\n")
    f.write(f"MSE: {mean_squared_error(y_test, y_pred)}\n")
    f.write(f"r2 score: {r2_score(y_test, y_pred)}\n")
    f.write(f"Accuracy within +-10%: {within_10_percent_accuracy(y_test, y_pred)}%\n")
