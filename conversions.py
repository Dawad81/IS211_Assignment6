#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module does some tempature conversions."""


def convertCelsiusToKelvin(temp_C):
    """This function converts Celsius to Kelvin.

    Args:
        temp_C (int): args a Celsius temperature to be converted to Kelvin.

    Returns:
        float point number representing a Kelvin temperature rounded to the
        nearest 2nd decimal place.

    Examples:
        >>> convertCelsiusToKelvin(300)
        573.15

        >>> convertCelsiusToKelvin(-10)
        263.15
    """
    kelvin = float(temp_C) + 273.15
    return round(kelvin, 2)


def convertCelsiusToFahrenheit(temp_C):
    """This function converts Celsius to Fahrenheit.

    Args:
        temp_C (int): args a Celsius temperature to be converted to Fahrenheit.

    Returns:
        float point number representing a Fahrenheit temperature rounded to the
        nearest 2nd decimal place.

    Examples:

        >>> convertCelsiusToFahrenheit(-273.15)
        -459.67

        >>> convertCelsiusToFahrenheit(140)
        284.0
    """
    fahrenheit = (float(temp_C) * (1.8)) + 32
    return round(fahrenheit, 2)


def convertFahrenheitToCelsius(temp_F):
    """This function converts Fahrenheit to Celsius.

    Args:
        temp_F (int): args a Fahrenheit temperature to be converted to Celsius.

    Returns:
        float point number representing a Celsius temperature rounded to the
        nearest 2nd decimal place.

    Examples:

        >>> convertFahrenheitToCelsius(572)
        300.0

        >>> convertFahrenheitToCelsius(-238)
        -150.0
    """
    celsius = (float(temp_F) - 32) * 5/9
    return round(celsius, 2)


def convertFahrenheitToKelvin(temp_F):
    """This function converts Fahrenheit to Kelvin.

    Args:
        temp_F (int): args a Fahrenheit temperature to be converted to Kelvin.

    Returns:
        float point number representing a Kelvin temperature rounded to the
        nearest 2nd decimal place.

    Examples:

        >>> convertFahrenheitToKelvin(608)
        593.15

        >>> convertFahrenheitToKelvin(-459.67)
        0.0
    """
    kelvin = (float(temp_F) + 459.67) * 5/9
    return round(kelvin, 2)


def convertKelvinToFahrenheit(temp_K):
    """This function converts Kelvin to Fahrenheit.

    Args:
        temp_K (int): args a Kelvin temperature to be converted to Fahrenheit.

    Returns:
        float point number representing a Fahrenheit temperature rounded to the
        nearest 2nd decimal place.

    Examples:

        >>> convertKelvinToFahrenheit(0)
        -459.67

        >>> convertKelvinToFahrenheit(123.15)
        -238.0
    """
    fahrenheit = (float(temp_K) * 1.8) - 459.67
    return round(fahrenheit, 2)


def convertKelvinToCelsius(temp_K):
    """This function converts Kelvin to Celsius.

    Args:
        temp_K (int): args a Kelvin temperature to be converted to Celsius.

    Returns:
        float point number representing a Celsius temperature rounded to the
        nearest 2nd decimal place.

    Examples:

        >>> convertKelvinToCelsius(663.15)
        390.0

        >>> convertKelvinToCelsius(0)
        -273.15
    """
    celsius = float(temp_K) - 273.15
    return round(celsius, 2)
