import unittest
import ooo

class TournamentTest(unittest.TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = ooo.Runner("Усэйн", speed=10)
        self.runner2 = ooo.Runner("Андрей", speed=9)
        self.runner3 = ooo.Runner("Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        for place, runner in sorted(cls.all_results.items()):
            print(f"Место {place}: {runner.name}")

    def test_tournament_usain_nik(self):
        tournament = ooo.Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        self.all_results.update(results)

        # Проверка, что Ник занимает последнее место
        self.assertTrue(self.all_results[max(self.all_results)] == "Ник")

    def test_tournament_andrey_nik(self):
        tournament = ooo.Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results.update(results)

        # Проверка, что Ник занимает последнее место
        self.assertTrue(self.all_results[max(self.all_results)] == "Ник")

    def test_tournament_usain_andrey_nik(self):
        tournament = ooo.Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results.update(results)

        # Проверка, что Ник занимает последнее место
        self.assertTrue(self.all_results[max(self.all_results)] == "Ник")

if __name__ == "__main__":
    unittest.main()