#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module refactor's our code in conversion.py."""


class ConversionNotPossible(Exception):
    """ConversionNotPossible fromUnit and toUnit cannot be converted
    incompatible units."""
    pass


def convert(fromUnit=str, toUnit=str, value=int):
    """This function converts a value from one unit of measurement to
    another.

    Args:
        fromUnit (str): args the unit of measurement for the input in the value
        param.
        toUnit (str): args the type of unit the param value will be converted
        to.
        value (int): args the int value of fromUnit to be converted into toUnits.

    Returns:
        float point number converted and rounded to the nearest 2nd decimal
        place. If units are incompatible it will raise the ConversionNotPossible
        exception error.

    Example:

        >>> convert('miles', 'miles', 23)
        23.0

        >>> convert('celsius', 'kelvin', 500)
        773.15

        >>> convert('miles', 'meters', 1)
        1609.34

        >>> convert('yards', 'kelvin', 34)
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
          File "conversions_refactored.py", line 59, in convert
            raise ConversionNotPossible(error)
        __main__.ConversionNotPossible: 'yards'
    """
    num = value
    temp_conversions_dict = {'fahrenheit': {'celsius': (float(num)
                                                        - 32) * 5 / 9,
                                            'kelvin': (float(num)
                                                       + 459.67) * 5 / 9},
                             'celsius': {'fahrenheit': (float(num)
                                                        * (1.8)) + 32,
                                         'kelvin': float(num) + 273.15},
                             'kelvin': {'fahrenheit': (float(num)
                                                       * 1.8) - 459.67,
                                        'celsius': float(num) - 273.15}}

    distance_conversion_dict = {'miles': {'yards': float(num) * 1760,
                                          'meters': float(num) * 1609.34},
                                'yards': {'meters': float(num) * 0.9144,
                                          'miles': float(num) * 0.00056818},
                                'meters': {'yards': float(num) * 1.09361,
                                           'miles': float(num) * 0.000621371}}
    fromUnit = fromUnit.lower()
    toUnit = toUnit.lower()
    if fromUnit == toUnit:
        answer = float(num)
        return round(answer, 2)
    else:
        try:
            if fromUnit and toUnit in temp_conversions_dict:
                answer = temp_conversions_dict[fromUnit][toUnit]
                return round(answer, 2)
            elif fromUnit and toUnit in distance_conversion_dict:
                answer = distance_conversion_dict[fromUnit][toUnit]
                return round(answer, 2)
        except KeyError as error:
            raise ConversionNotPossible(error)


if __name__ == "__main__":
    print convert('miles', 'miles', 23)
    print convert('celsius', 'kelvin', 500)
    print convert('miles', 'meters', 1)
    print convert('yards', 'kelvin', 34)
