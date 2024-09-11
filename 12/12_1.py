import rrr
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        r = rrr.Runner('Motya')
        for i in range(10):
            r.walk()
        self.assertEqual(r.distance, 50)

    def test_run(self):
        r = rrr.Runner('Kopgush')
        for i in range(10):
            r.run()
        self.assertEqual(r.distance, 100)

    def test_challenge(self):
        r = rrr.Runner('Motya')
        p = rrr.Runner('Kopgush')
        for i in range(10):
            r.walk()
            p.run()
        self.assertEqual(r.distance, 50)
        self.assertEqual(p.distance, 100)