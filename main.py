import math


class Solver:

    E = 1e-5

    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

    def solve(self) -> list:
        variables = (self.a, self.b, self.c)
        if any([math.isnan(x) for x in variables]):
            raise ValueError('Float NaN is not supported')
        if any([math.isinf(x) for x in variables]):
            raise ValueError('Float Inf is not supported')
        if -self.E < self.a < self.E:
            raise ValueError(f'Variable "a" cannot be zero')

        d = math.pow(self.b, 2) - 4 * self.a * self.c
        if d < -self.E:
            return []
        if d > self.E:
            return [
                (-self.b + math.sqrt(d)) / 2 * self.a,
                (-self.b - math.sqrt(d)) / 2 * self.a
            ]
        if -self.E < d < self.E:
            return [-self.b / 2 * self.a]
