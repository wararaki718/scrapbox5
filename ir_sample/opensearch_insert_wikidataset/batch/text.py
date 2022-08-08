class TextParser:
    def parse(self, text: str) -> str:
        return text \
                .replace("_START_ARTICLE_", " ") \
                .replace("_START_SECTION_", " ") \
                .replace("_START_PARAGRAPH_", " ") \
                .replace("_NEWLINE_", "\n")
