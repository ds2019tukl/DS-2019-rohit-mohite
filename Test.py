import unittest

import pandas as pd


def minimum(d1):
    return d1.min()

def maximum(d1):
    return d1.max()


def avg(d1):
    return d1.mean()


class TestTimeMethods(unittest.TestCase):

    def test_min(self):

        data1 = {'col1': [1, 2, 4, 7, 9, 8, 5], 'col2': [10, 0, -1, 9, -8, 6, 2]}

        d1 = pd.DataFrame(data=data1)

        self.assertEqual(minimum(d1["col1"]), 1)

        self.assertEqual(minimum(d1["col2"]), -8)



    def test_avg(self):

        data1 = {'col1': [1, 6, 0, 2, 3, 4, 5], 'col2': [1, 7, 3, 5, 2, 10, 0]}

        d1 = pd.DataFrame(data=data1)

        self.assertEqual(avg(d1["col1"]), 3)

        self.assertEqual(avg(d1["col2"]), 4)



    def test_max(self):

        data1 = {'col1': [2, 5, 8, 9, 10, 15], 'col2': [-5, 0, -12, 1, 3, 5]}

        d1 = pd.DataFrame(data=data1)

        self.assertEqual(maximum(d1["col1"]), 15)

        self.assertEqual(maximum(d1["col2"]), 5)





if __name__ == '__main__':

    unittest.main()