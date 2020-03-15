# -*- coding: utf-8 -*-

import operator
from functools import reduce


class SimpleCalculator:
    def add(self, *args):
        return sum(args)

    def sub(self, a, b):
        return a - b

    def mul(self, *args):
        if not all(args):
            raise ValueError
        return reduce(operator.mul, args)

    def div(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return float("inf")

    def avg(self, it, lt=None, ut=None):
        _it = it[:]

        if lt:
            _it = [x for x in _it if x >= lt]

        if ut:
            _it = [x for x in _it if x <= ut]

        if not len(_it):
            return 0

        return sum(_it) / len(_it)
