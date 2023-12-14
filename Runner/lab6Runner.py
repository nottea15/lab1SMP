import unittest

from BLL.Lab6.UnitTestCalculator import UnitTestsCalculator


class RunnerLab6:
    def run_tests(self):
        suite = unittest.TestLoader().loadTestsFromTestCase(UnitTestsCalculator)
        unittest.TextTestRunner().run(suite)

if __name__ == "__main__":
    RunnerLab6().run_tests()