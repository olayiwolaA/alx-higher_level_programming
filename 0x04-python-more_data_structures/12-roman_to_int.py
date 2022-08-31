#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string and isinstance(roman_string, str):
        rom_num = {'I': 1, 'V': 5, 'X': 10, 'L':
                   50, 'C': 100, 'D': 500, 'M': 1000}
        rom_str = roman_string
        roman_str = 0
        for rom in range(len(rom_str)):
            if rom > 0 and (rom_num[rom_str[rom]] > rom_num[rom_str[rom - 1]]):
                roman_str += rom_num[rom_str[rom]] -
                (2 * rom_num[roman_string[rom - 1]])
            else:
                roman_str += rom_num[rom_str[rom]]
        return roman_str
    return (0)
