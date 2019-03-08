#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module runs test on the conversion.py module."""

import conversions
import unittest


class KnownValues (unittest.TestCase):
    KnownTempsCFK =[[300.00, 572.00, 573.15],
                    [-10.00, 14.00, 263.15],
                    [-273.15, -459.67, 0.00],
                    [390.00, 734.00, 663.15],
                    [140.00, 284.00, 413.15],
                    [320.00, 608.00, 593.15],
                    [-150.00, -238.00, 123.15]]

    def testConvertCelsiusToKelvin(self):
        """convertCelsiusToKelvin should give known result with known input"""
        for degree in self.KnownTempsCFK:
            answer = conversions.convertCelsiusToKelvin(degree[0])
            self.assertEqual(degree[2], answer)


    def testConvertCelsiusToFahrenheit(self):
        """convertCelsiusToFahrenheit should give known result with known input"""
        for degree in self.KnownTempsCFK:
            answer = conversions.convertCelsiusToFahrenheit(degree[0])
            self.assertEqual(degree[1], answer)


    def testConvertFahrenheitToCelsius(self):
        """convertFahrenheitToCelsius should give known result with known input"""
        for degree in self.KnownTempsCFK:
            answer = conversions.convertFahrenheitToCelsius(degree[1])
            self.assertEqual(degree[0], answer)


    def testConvertFahrenheitToKelvin(self):
        """convertFahrenheitToKelvin should give known result with known input"""
        for degree in self.KnownTempsCFK:
            answer = conversions.convertFahrenheitToKelvin(degree[1])
            self.assertEqual(degree[2], answer)


    def testConvertKelvinToFahrenheit(self):
        """convertKelvinToFahrenheit should give known result with known input"""
        for degree in self.KnownTempsCFK:
            answer = conversions.convertKelvinToFahrenheit(degree[2])
            self.assertEqual(degree[1], answer)


    def testConvertKelvinToCelsius(self):
        """convertKelvinToCelsius should give known result with known input"""
        for degree in self.KnownTempsCFK:
            answer = conversions.convertKelvinToCelsius(degree[2])
            self.assertEqual(degree[0], answer)



if __name__ == "__main__":
    unittest.main()
