from typing import Callable, List

import codewars_test as test

def euler_sol(fun: Callable[[float, List[float]], float], order: int, step: float, num_steps: int, *initial: float) -> float:
    try:
        x = 0
        y = list(initial) + [0]
        for _ in range(num_steps):
            y[order] = fun(x, y[:-1])
            x += step
            for i in range(order):
                y[i] += step * y[i + 1]

        return y[0]
    except:
        raise ValueError("Invalid input")

@test.describe("Example tests")
def example_tests():
    
    @test.it("Higher-order tests")
    def higher_order():
        test.assert_approx_equals(euler_sol(lambda x,args:-args[0], 2, 0.0314159, 100, 1, 0), -1.0505596963)
        test.assert_approx_equals(euler_sol(lambda x,args:args[1], 2, 0.002, 500, 2, 1), 3.71556852065)
