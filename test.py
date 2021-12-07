from day6 import count
from unittest import TestCase


class Test(TestCase):

    def test_count(self):
        days = 18
        input = [3,4,3,1,2]
        output = [3,2,3,3,3]
        for i, inp in enumerate(input):
            assert count(inp, days) == output[i]

    def test_count_2(self):
        days = 17
        input =  [2, 3, 2, 0, 1]
        output = [3, 2, 3, 3, 3]
        for i, inp in enumerate(input):
            try:
                assert count(inp, days) == output[i]
            except AssertionError:
                self.fail(f"Failed fish n {i}")

    def test_count_3(self):
        days = 16
        input =  [1, 2, 1, 6, 0, 8]
        output = [3, 2, 3, 2, 3, 2]
        for i, inp in enumerate(input):
            try:
                assert count(inp, days) == output[i]
            except AssertionError:
                self.fail(f"Failed fish n {i}")

    def test_count_4(self):
        days = 15
        input =  [0, 1, 0, 5, 6, 7, 8]
        output = [3, 2, 3, 2, 2, 2, 1]
        for i, inp in enumerate(input):
            try:
                assert count(inp, days) == output[i]
            except AssertionError:
                self.fail(f"Failed fish n {i}")

    def test_count_5(self):
        days = 14
        input =  [6,0,6,4,5,6,7,8,8]
        output = [2, 2, 2, 2, 2, 2, 1,1,1]
        for i, inp in enumerate(input):
            try:
                assert count(inp, days) == output[i]
            except AssertionError:
                self.fail(f"Failed fish n {i}")

    def test_count_6(self):
        days = 17
        input = [3, 4, 3, 1, 2]
        output = [2, 2, 2, 3, 3]
        for i, inp in enumerate(input):
            assert count(inp, days) == output[i]