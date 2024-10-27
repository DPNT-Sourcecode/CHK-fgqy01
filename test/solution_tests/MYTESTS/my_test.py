import sys
import os

# Add the directory two levels up to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))
from lib.solutions.SUM import sum_solution

class TestAll():
    def TestAll(self):
        assert sum_solution.compute(1, 2) == 3

