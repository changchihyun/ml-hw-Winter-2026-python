# module5_mod.py
# Contains the class for storing and searching numbers.

class NumberStore:
    def __init__(self):
        self._nums = []

    def add_number(self, value: int) -> None:
        self._nums.append(value)

    def find_first_index_1based(self, target: int) -> int:
        for i, v in enumerate(self._nums, start=1):
            if v == target:
                return i
        return -1
