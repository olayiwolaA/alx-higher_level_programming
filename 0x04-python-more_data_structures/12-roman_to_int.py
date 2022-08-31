#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string and isinstance(roman_string, str):
        rom_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        rom_str = roman_string
        roman = 0
        for l in range(len(rom_str)):
            if l > 0 and (rom_num[rom_str[l]] > rom_num[rom_str[l - 1]]):
                roman += rom_num[rom_str[l]] - (2 * rom_num[roman_string[l - 1]])
            else:
                roman += rom_num[rom_str[l]]
        return roman
    return (0)
