import sys
import os

# Add the directory two levels up to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

class TestSum():
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3
