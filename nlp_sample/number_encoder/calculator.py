class Calculator:
    def __init__(self):
        self._numbers = {i: int(i) for i in "0123456789"}
        self._numbers.update({key: i for i, key in enumerate("０１２３４５６７８９")})
        self._numbers.update({key: i for i, key in enumerate("〇一二三四五六七八九")})
        self._numbers.update({key: i for i, key in enumerate("壱弐参", start=1)})
        self._digits = {key: 10**i for i, key in enumerate("十百千", start=1)}
        self._digits.update({key: 10**(i*4) for i, key in enumerate("万億兆", start=1)})

    def calculate(self, s: str) -> str:
        s = s.replace(",", "")
        if len(set(s) & (set(self._digits.keys()))) == 0:
            return "".join(map(lambda c: str(self._numbers.get(c, c)), s))
        
        if len(set(s) & set(self._numbers.keys())) == 0:
            return s

        digits = 1
        n = ""
        result = 0
        for i, c in enumerate(reversed(s)):
            if c == ".":
                n = "." + n
                continue

            n = str(self._numbers.get(c, "")) + n
            d = self._digits.get(c, 1)

            if c in self._digits and n != "":
                result += float(n) * digits
                n = ""
            digits *= d
        
        if s[0] in self._digits:
            result += digits
        elif n != "":
            result += float(n) * digits

        return str(int(result))


if __name__ == "__main__":
    calculator = Calculator()
    texts = [
        "二〇〇五",
        "一二三四五六七八九",
        "千",
        "二万七千",
        "1億9千万",
        "四千二百万",
        "10,000万",
        "１億",
        "10,10",
        "10",
        "十",
        "10.6億",
        "0.6",
        "百三億",
        "106百万"
    ]
    for text in texts:
        result = calculator.calculate(text)
        print(f"before: {text}")
        print(f"after : {result}")
        print()