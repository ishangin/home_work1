from itertools import combinations_with_replacement
from typing import Any

import pytest
from main import Solver


@pytest.mark.parametrize(
    'a, b, c, result', [
        pytest.param(1.0, 0.0, 1.0, [], id='x^2+1=0'),
        pytest.param(1.0, 0.0, -1.0, [1.0, -1.0], id='x^2-1=0'),
        pytest.param(1.0, 2.0, 1.0, [-1.0], id='x^2+2x+1=0'),
        pytest.param(0.0, 1.0, 1.0, ValueError, id='a=0'),
        pytest.param(
            1.0, 2.0001, 1.0001, [-1.00005], id='1.0001*x^2+2.0001*x+1=0'
        ),
    ]
)
def test_solve(a: float, b: float, c: float, result: Any):
    if type(result) == type and issubclass(result, Exception):
        with pytest.raises(result):
            Solver(a, b, c).solve()
    else:
        assert precision(Solver(a, b, c).solve(), result)


@pytest.mark.parametrize(
    'vals', [
        pytest.param((1.0, float('nan'), float('inf'), float('-inf')), id='nan +inf -inf')
    ]
)
def test_nan_infinity(vals: list):
    abc = list(combinations_with_replacement(vals, 3))[1:]
    for val in abc:
        with pytest.raises(ValueError):
            Solver(*val).solve()


def precision(roots: list, expected: list) -> bool:
    e = Solver.E
    if len(expected) == 0:
        return len(roots) == 0
    if len(expected) == 1:
        return (expected[0] - e) < roots[0] < (expected[0] + e)
    if len(expected) == 2:
        return (
                ((expected[0] - e) < roots[0] < (expected[0] + e)) and
                ((expected[1] - e) < roots[1] < (expected[1] + e))
        )
