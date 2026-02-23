import numpy as np


def read_pos_int(msg: str) -> int:
    """Read a positive integer from user input."""
    while True:
        s = input(msg).strip()
        try:
            v = int(s)
            if v <= 0:
                print("Please enter a positive integer.")
                continue
            return v
        except ValueError:
            print("That was not an integer. Try again.")


def read_float(msg: str) -> float:
    """Read a real number (float) from user input."""
    while True:
        s = input(msg).strip()
        try:
            return float(s)
        except ValueError:
            print("That was not a valid number. Try again.")


def knn_regression_1d(x_train: np.ndarray, y_train: np.ndarray, X: float, k: int) -> float:
    """
    k-NN regression for 1D input feature.
    Prediction = average of y values of k nearest x values (by L2 distance).
    """
    # In 1D, L2 distance = abs difference
    dists = np.abs(x_train - X)

    # indices of k smallest distances
    idx = np.argsort(dists)[:k]

    # average the corresponding y's
    return float(np.mean(y_train[idx]))


def main():
    N = read_pos_int("Enter N (positive integer): ")
    k = read_pos_int("Enter k (positive integer): ")

    # store points in NumPy arrays (as required: use NumPy as much as possible)
    x_train = np.empty(N, dtype=float)
    y_train = np.empty(N, dtype=float)

    for i in range(N):
        x_train[i] = read_float(f"Point {i+1} - x: ")
        y_train[i] = read_float(f"Point {i+1} - y: ")

    X = read_float("Enter X: ")

    if k > N:
        print(f"Error: k ({k}) cannot be greater than N ({N}).")
        return

    y_pred = knn_regression_1d(x_train, y_train, X, k)
    print(y_pred)


if __name__ == "__main__":
    main()
