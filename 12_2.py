import ooo
import unittest


class TournamentTest(unittest.TestCase):

    def setUp(self):
        self.runner1 = ooo.Runner('Усэйн', 10)
        self.runner2 = ooo.Runner('Андрей', 9)
        self.runner3 = ooo.Runner('Ник', 3)

    @classmethod
    def setUpClass(self):
        self.all_results = {}


    def tearDown(self):
        print('\n')
        for place, runner in sorted(self.all_results.items()):
            print(f"Место {place}: {runner.name}")

    # @classmethod
    # def tearDownClass(self):
    #     for place, runner in sorted(self.all_results.items()):
    #         print(f"Место {place}: {runner.name}")

    def test_start1(self):
        tournament1 = ooo.Tournament(90, self.runner1, self.runner3)
        results = tournament1.start()
        self.all_results.update(results)
        self.assertTrue(self.all_results[max(self.all_results)] == self.runner3)

    def test_start2(self):
        tournament2 = ooo.Tournament(90, self.runner2, self.runner3)
        results = tournament2.start()
        self.all_results.update(results)
        self.assertTrue(self.all_results[max(self.all_results)] == self.runner3)

    def test_start3(self):
        tournament3 = ooo.Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament3.start()
        self.all_results.update(results)
        self.assertTrue(self.all_results[max(self.all_results)] == self.runner3)
