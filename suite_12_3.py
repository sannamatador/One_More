import unittest
from M12_2 import TournamentTest
from M12_1 import RunnerTest

PR_test = unittest.TestSuite()
PR_test.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))
PR_test.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(PR_test)
