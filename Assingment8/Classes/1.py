class RomanConverter:
    def __init__(self):
        self.int_to_roman_map = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        self.roman_to_int_map = {r: i for i, r in self.int_to_roman_map}

    def int_to_roman(self, num):
        result = ""
        for value, symbol in self.int_to_roman_map:
            while num >= value:
                result += symbol
                num -= value
        return result

    def roman_to_int(self, s):
        i = 0
        total = 0
        while i < len(s):
            if i + 1 < len(s) and s[i:i+2] in self.roman_to_int_map:
                total += self.roman_to_int_map[s[i:i+2]]
                i += 2
            else:
                total += self.roman_to_int_map[s[i]]
                i += 1
        return total
