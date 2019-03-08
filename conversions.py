#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module does some tempature conversions."""


def convertCelsiusToKelvin(temp_C):
    kelvin = float(temp_C) + 273.15
    return round(kelvin, 2)


def convertCelsiusToFahrenheit(temp_C):
    fahrenheit = (float(temp_C) * (1.8)) + 32
    return round(fahrenheit,2)


