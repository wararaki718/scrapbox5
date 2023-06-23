from typing import List, Union

from schema import AnnotatedNamedEntity, Result


class RuleExtractor:
    def __init__(self) -> None:
        pass

    def extract(self, entites: List[AnnotatedNamedEntity]) -> List[List[Union[Result, None]]]:
        predictions = []
        for entity in entites:
            results = []
            for i, token in enumerate(entity.tokens):
                pos = token.part_of_speech()
                
                if pos[0] == "名詞" and pos[1] == "固有名詞" and pos[2] == "組織":
                    result = Result(index=i, surface=token.surface())
                elif pos[0] == "名詞" or pos[0] == "接頭詞":
                    result = Result(index=i, surface=token.surface())
                else:
                    result = None

                results.append(result)
            predictions.append(results)
                
        return results
