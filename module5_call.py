# module5_call.py
# Uses NumberStore from module5_mod.py to read input and search for X.

from module5_mod import NumberStore


def _read_positive_int(prompt: str) -> int:
    while True:
        try:
            n = int(input(prompt))
            if n > 0:
                return n
            print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter an integer.")


def _read_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")


def main() -> None:
    store = NumberStore()

    n = _read_positive_int("Enter N (positive integer): ")
    for i in range(1, n + 1):
        value = _read_int(f"Enter number #{i}: ")
        store.add_number(value)

    x = _read_int("Enter X (integer to search for): ")
    print(store.find_first_index_1based(x))


if __name__ == "__main__":
    main()
