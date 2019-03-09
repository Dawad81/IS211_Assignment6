#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module refactor's our code in conversion.py."""



class ConversionNotPossible(Exception): pass


def convert(fromUnit=str, toUnit=str, value=int):
    num = value
    temp_conversions_dict = {
        'fahrenheit': {'celsius': (float(num) - 32) * 5 / 9,
                       'kelvin': (float(num) + 459.67) * 5 / 9},
        'celsius': {'fahrenheit': (float(num) * (1.8)) + 32,
                    'kelvin': float(num) + 273.15},
        'kelvin': {'fahrenheit': (float(num) * 1.8) - 459.67,
                   'celsius': float(num) - 273.15}
        }

    distance_conversion_dict = {
        'miles': {'yards': float(num) * 1760,
                  'meters': float(num) * 1609.34},
        'yards': {'meters': float(num) * 0.9144,
                  'miles': float(num) * 0.00056818},
        'meters': {'yards': float(num) * 1.09361,
                   'miles': float(num) * 0.000621371}
        }
    
    fromUnit = fromUnit.lower()
    toUnit = toUnit.lower()
    if fromUnit == toUnit:
        answere = num
        return float(answere)
    else:
        try:
            if fromUnit and toUnit in temp_conversions_dict:
                answere = temp_conversions_dict[fromUnit][toUnit]
                return round(answere, 2)
            elif fromUnit and toUnit in distance_conversion_dict:
                answere = distance_conversion_dict[fromUnit][toUnit]
                return round(answere, 2)
        except:
            raise ConversionNotPossible



#def testConvert(self):
#    """convertFahrenheitToCelsius should give known result with known input"""
#    for value in self.KnownTempsCFK:
#        answer = conversions_refactored.convert(degree[1])
#        self.assertEqual(degree[0], answer)

if __name__ == "__main__":
    print convert('kelvin', 'kelvin', 0)
    print convert('miles', 'miles', 23)
    print convert('celsius', 'kelvin', 500)
    print convert('miles', 'meters', 1)
    print convert('yards', 'kelvin', 34)
