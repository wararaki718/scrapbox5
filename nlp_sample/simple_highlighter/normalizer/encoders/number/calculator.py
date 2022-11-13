class Calculator:
    def __init__(self):
        self._numbers = {i: int(i) for i in "0123456789"}
        self._numbers.update({key: i for i, key in enumerate("０１２３４５６７８９")})
        self._numbers.update({key: i for i, key in enumerate("〇一二三四五六七八九")})
        self._numbers.update({key: i for i, key in enumerate("壱弐参", start=1)})
        self._digits = {key: 10**i for i, key in enumerate("十百千", start=1)}
        self._large_digits = {key: 10**(i*4) for i, key in enumerate("万億兆", start=1)}

    def calculate(self, s: str) -> str:
        # ip
        if s.count(".") > 1:
            return "".join(map(lambda c: str(self._numbers.get(c, c)), s))

        s = s.replace(",", "")
        queue = ""
        tmp = 0.0
        result = 0.0
        for c in s:
            if c in self._digits:
                if len(queue) == 0:
                    queue = "1"
                tmp += float(queue) * self._digits.get(c)
                queue = ""
                continue

            if c in self._large_digits:
                if len(queue) > 0:
                    tmp += float(queue)
                result += (tmp * self._large_digits.get(c))
                queue = ""
                tmp = 0.0
                continue
            
            queue += str(self._numbers.get(c, c))
        
        if len(queue) > 0:
            tmp += float(queue)
        
        if tmp > 0:
            result += tmp
        
        if result.is_integer():
            result = int(result)
        
        return str(result)
