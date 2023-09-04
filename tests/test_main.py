#!/usr/bin/env python
# -*- coding: utf-8 -*-

from simple_calculator.main import SimpleCalculator


def test_add_two_numbers():
    calculator = SimpleCalculator()

    result = calculator.add(4, 5)

    assert result == 9
