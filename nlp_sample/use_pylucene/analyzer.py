from typing import List

import lucene
from java.io import StringReader
from org.apache.lucene.analysis.ja import JapaneseAnalyzer
from org.apache.lucene.analysis.tokenattributes import CharTermAttribute


class TextAnalyzer:
    def __init__(self):
        lucene.initVM(vmargs=["-Djava.awt.headless=true"])
        self._analyzer = JapaneseAnalyzer()

    def analyze(self, text: str) -> List[str]:
        stream = self._analyzer.tokenStream("", StringReader(text))
        stream.reset()

        tokens = []
        while stream.incrementToken():
            tokens.append(
                stream.getAttribute(CharTermAttribute.class_).toString()
            )
        return tokens
