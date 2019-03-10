#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This runs test on the conversion.py & conversions_refactored.py modules."""

import conversions
import conversions_refactored
import unittest


class KnownValues (unittest.TestCase):
    """This class test Known temperature values against the temperature
    conversion functions in conversions.py module."""
    KnownTempsCFK =[[300.00, 572.00, 573.15],
                    [-10.00, 14.00, 263.15],
                    [-273.15, -459.67, 0.00],
                    [390.00, 734.00, 663.15],
                    [140.00, 284.00, 413.15],
                    [320.00, 608.00, 593.15],
                    [-150.00, -238.00, 123.15]]


    def testConvertCelsiusToKelvin(self):
        """convertCelsiusToKelvin should give known result with known input."""
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
        """convertFahrenheitToKelvin should give known result with known input."""
        for degree in self.KnownTempsCFK:
            answer = conversions.convertFahrenheitToKelvin(degree[1])
            self.assertEqual(degree[2], answer)


    def testConvertKelvinToFahrenheit(self):
        """convertKelvinToFahrenheit should give known result with known input."""
        for degree in self.KnownTempsCFK:
            answer = conversions.convertKelvinToFahrenheit(degree[2])
            self.assertEqual(degree[1], answer)


    def testConvertKelvinToCelsius(self):
        """convertKelvinToCelsius should give known result with known input."""
        for degree in self.KnownTempsCFK:
            answer = conversions.convertKelvinToCelsius(degree[2])
            self.assertEqual(degree[0], answer)


class testConvert(unittest.TestCase):
    """This class defines the test  for the convert function in
    conversions_refactored.py."""


    def testConvertTempurature(self):
        """convert() should give known temperature result with known input."""
        self.assertEqual(conversions_refactored.convert(
            'celsius', 'kelvin', 300), 573.15)
        self.assertEqual(conversions_refactored.convert(
            'celsius', 'fahrenheit', 390), 734.00)
        self.assertEqual(conversions_refactored.convert(
            'fahrenheit', 'celsius', -238), -150.00)
        self.assertEqual(conversions_refactored.convert(
            'fahrenheit', 'kelvin', 734), 663.15)
        self.assertEqual(conversions_refactored.convert(
            'kelvin','fahrenheit', 0), -459.67)
        self.assertEqual(conversions_refactored.convert(
            'kelvin','celsius', 413.15), 140.00)



    def testConvertDistance(self):
        """convert() should give known distance result with known input."""
        self.assertEqual(conversions_refactored.convert('miles', 'yards',
                                                        5), 8800.00)
        self.assertEqual(conversions_refactored.convert('miles', 'meters',
                                                        100), 160934)
        self.assertEqual(conversions_refactored.convert('yards', 'meters',
                                                        16), 14.63)
        self.assertEqual(conversions_refactored.convert('yards', 'miles',
                                                        25), 0.01)
        self.assertEqual(conversions_refactored.convert('meters', 'yards',
                                                        50), 54.68)
        self.assertEqual(conversions_refactored.convert('meters', 'miles',
                                                        50), 0.03)

    def testConvertToSelf(self):
        """convert() should return same known value inputted when fromUnit is
        the same as toUnit."""
        self.assertEqual(conversions_refactored.convert('celsius', 'celsius',
                                                        300), 300)
        self.assertEqual(conversions_refactored.convert('fahrenheit', 'fahrenheit',
                                                        14), 14)
        self.assertEqual(conversions_refactored.convert('kelvin', 'kelvin',
                                                        0), 0)
        self.assertEqual(conversions_refactored.convert('miles', 'miles',
                                                        10), 10)
        self.assertEqual(conversions_refactored.convert('yards', 'yards',
                                                        3), 3)
        self.assertEqual(conversions_refactored.convert('meters', 'meters',
                                                        5), 5)


    def testConversionNotPossibleError(self):
        """convert() should raise ConversionNotPossible error when trying to
        convert incompatible units."""
        self.assertRaises(conversions_refactored.ConversionNotPossible,
                          conversions_refactored.convert, 'fahrenheit',
                          'miles', 608)
        self.assertRaises(conversions_refactored.ConversionNotPossible,
                          conversions_refactored.convert, 'yards',
                          'celsius', 12)
        self.assertRaises(conversions_refactored.ConversionNotPossible,
                          conversions_refactored.convert, 'kelvin',
                          'meters', 0)


if __name__ == "__main__":
    unittest.main()
