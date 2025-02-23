import sys
import os

# Add the directory two levels up to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))
from lib.solutions.SUM import sum_solution

from lib.solutions.CHK import checkout_solution


class TestSum():
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3

        assert checkout_solution.checkout("ABCDE") == 155
        assert checkout_solution.checkout("ABCDEABCDE") == 280
        assert checkout_solution.checkout("CCADDEEBBA") == 280

        assert checkout_solution.checkout("AFFF") == 70
        assert checkout_solution.checkout("FFF") == 20
        assert checkout_solution.checkout("ABBFFF") == 115
        assert checkout_solution.checkout("FFFFFF") == 40

        assert checkout_solution.checkout("G") == 20
        assert checkout_solution.checkout("H") == 10
        assert checkout_solution.checkout("I") == 35

        assert checkout_solution.checkout("HHHHHHHHHH") == 80

        assert checkout_solution.checkout("SYX") == 45
        assert checkout_solution.checkout("SSS") == 45

        assert checkout_solution.checkout("SYXSTZ") == 90

        assert checkout_solution.checkout("SYXA") == 95

        assert checkout_solution.checkout("KK") == 120
        assert checkout_solution.checkout("KKK") == 190
        assert checkout_solution.checkout("KKKK") == 240

        assert checkout_solution.checkout("SSSZ") == 65
        assert checkout_solution.checkout("ZZZS") == 65
        assert checkout_solution.checkout("STXS") == 62



