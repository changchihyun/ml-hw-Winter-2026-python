# module5_oop.py
# Reads N numbers, then searches for X and prints its 1-based index or -1.

class NumberStore:
    def __init__(self):
        self._nums = []

    def add_number(self, value: int) -> None:
        self._nums.append(value)

    def find_first_index_1based(self, target: int) -> int:
        """
        Returns the 1-based index of the first occurrence of target.
        If not found, returns -1.
        """
        for i, v in enumerate(self._nums, start=1):
            if v == target:
                return i
        return -1


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
