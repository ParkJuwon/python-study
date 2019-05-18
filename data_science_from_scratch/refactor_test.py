import math


class Solver:
    def roots(self):
        a = 3
        b = 25
        c = 46
        sqrt = math.sqrt(b**2 - 4 * a * c)
        root1 = (-b + sqrt) / (2 * a)
        root2 = (-b - sqrt) / (2 * a)
        return root1, root2


print Solver().roots()
