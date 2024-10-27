import sys
import os

# Add the directory two levels up to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))
from lib.solutions.SUM import sum_solution

from lib.solutions.CHK import checkout_solution


class TestAll():
    def TestAll(self):
        assert sum_solution.compute(1, 2) == 3

        assert checkout_solution.checkout("ABCDE") == 155
        assert checkout_solution.checkout("ABCDEABCDE") == 280
        assert checkout_solution.checkout("CCADDEEBBA") == 280
