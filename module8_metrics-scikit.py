import numpy as np
from sklearn.metrics import precision_score, recall_score

# ask user how many points
n = int(input("Enter N (number of points): "))

# create numpy array to store (x,y)
points = np.zeros((n, 2), dtype=int)

# read points one by one
for i in range(n):
    print("Point", i + 1)

    x = int(input("Enter x (true label, 0 or 1): "))
    y = int(input("Enter y (predicted label, 0 or 1): "))

    points[i][0] = x
    points[i][1] = y

# separate true labels and predicted labels
y_true = points[:,0]
y_pred = points[:,1]

# calculate metrics using sklearn
precision = precision_score(y_true, y_pred, zero_division=0)
recall = recall_score(y_true, y_pred, zero_division=0)

# print results
print("Precision:", round(precision, 2))
print("Recall:", round(recall, 2))
