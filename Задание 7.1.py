a = [[4, 4, 5], [0, 3, 4], [2, 3, 4]]
b = [[2, 1, 1], [1, 2, 3], [8, 0, 1]]


class Matrix:
    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
        return "\n".join(map(str, self.lists))

    def __add__(self, other):
        c = []
        for i in range(len(self.lists)):
            c.append([])
            for j in range(len(self.lists[0])):
                c[i].append(self.lists[i][j] + other.lists[i][j])
        return "\n".join(map(str, c))



matrix_1 = Matrix(a)
matrix_2 = Matrix(b)
print(f"Матрица 1\n{matrix_1}\n{'-' * 20}")
print(f"Матрица 2\n{matrix_2}\n{'-' * 20}")
print(f"Матрица 1 + Матрица 2\n{matrix_1 + matrix_2}")
