#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module does some tempature conversions."""


def convertCelsiusToKelvin(temp_C):
    """This function converts Celsius to Kelvin."""
    kelvin = float(temp_C) + 273.15
    return round(kelvin, 2)


def convertCelsiusToFahrenheit(temp_C):
    """This function converts Celsius to Fahrenheit."""
    fahrenheit = (float(temp_C) * (1.8)) + 32
    return round(fahrenheit,2)


def convertFahrenheitToCelsius(temp_F):
    """This function converts Fahrenheit to Celsius."""
    celsius = (float (temp_F) - 32) * 5/9
    return round(celsius, 2)


def convertFahrenheitToKelvin(temp_F):
    """This function converts Fahrenheit to Kelvin."""
    kelvin = (float(temp_F) + 459.67) * 5/9
    return round(kelvin, 2)


def convertKelvinToFahrenheit(temp_K):
    """This function converts Kelvin to Fahrenheit."""
    fahrenheit = (float(temp_K) * 1.8) - 459.67
    return round(fahrenheit, 2)


def convertKelvinToCelsius(temp_K):
    """This function converts Kelvin to Celsius."""
    celsius = float(temp_K) - 273.15
    return round(celsius, 2)

