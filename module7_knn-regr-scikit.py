# module7_knn-regr-scikit.py

import numpy as np
from sklearn.neighbors import KNeighborsRegressor


def main():
    # Read N
    while True:
        try:
            N = int(input("Enter N (positive integer): "))
            if N > 0:
                break
            else:
                print("N must be positive.")
        except ValueError:
            print("Please enter a valid integer.")

    # Read k
    while True:
        try:
            k = int(input("Enter k (positive integer): "))
            if k > 0:
                break
            else:
                print("k must be positive.")
        except ValueError:
            print("Please enter a valid integer.")

    # Create NumPy arrays for training data
    x_values = np.zeros(N)
    y_values = np.zeros(N)

    # Read N points
    for i in range(N):
        while True:
            try:
                x_values[i] = float(input(f"Point {i+1} - x: "))
                break
            except ValueError:
                print("Invalid number. Try again.")

        while True:
            try:
                y_values[i] = float(input(f"Point {i+1} - y: "))
                break
            except ValueError:
                print("Invalid number. Try again.")

    # Compute variance of labels (training y)
    variance = np.var(y_values)
    print(variance)

    # Read test X
    while True:
        try:
            X_test = float(input("Enter X: "))
            break
        except ValueError:
            print("Invalid number. Try again.")

    if k > N:
        print("Error: k cannot be greater than N.")
        return

    # scikit-learn expects 2D feature arrays
    X_train = x_values.reshape(-1, 1)
    X_test_array = np.array([[X_test]])

    # Create and train model (Euclidean distance is default)
    model = KNeighborsRegressor(n_neighbors=k)
    model.fit(X_train, y_values)

    prediction = model.predict(X_test_array)

    print(float(prediction[0]))


if __name__ == "__main__":
    main()
