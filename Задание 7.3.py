class Cell:
    def __init__(self, nums):
        self.nums = nums

    def make_order(self, rows):
        return "\n".join(["*" * rows for _ in range(self.nums // rows)]) + "\n" * (self.nums % rows)

    def __str__(self):
        return self.nums

    def __add__(self, other):
        return f"Общее кол-во *: {self.nums + other.nums}"

    def __sub__(self, other):
        return self.nums - other.nums if self.nums - other.nums > 0\
            else "Выситание невозможно"

    def __mul__(self, other):
        return f"Умножение {self.nums * other.nums}"

    def __truediv__(self, other):
        return f"Деление {round(self.nums / other.nums)}"

cell_1 = Cell(15)
print(cell_1.make_order(5))