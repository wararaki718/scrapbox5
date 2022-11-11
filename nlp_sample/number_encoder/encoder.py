class NumberConverter:
    def __init__(self):
        self._mappings = {key: value for key, value in zip(list("一二三四五六七八九〇壱弐参"),list("1234567890123"))}

    def convert(self, s: str) -> str:
        result = ""
        for c in list(s):
            c = self._mappings.get(c, c)
            result += c
        return result
