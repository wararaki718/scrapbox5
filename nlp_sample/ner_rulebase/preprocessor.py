from typing import List

from analyzer import TextAnalyzer
from schema import NamedEntity, AnnotatedEntity, AnnotatedNamedEntity


class NERPreprocessor:
    def __init__(self) -> None:
        self._analyzer = TextAnalyzer()
    
    def transform(self, entities: List[NamedEntity]) -> List[AnnotatedNamedEntity]:
        results = []
        for entity in entities:
            annotated_entites = [
                AnnotatedEntity(
                    name=e.name,
                    span=e.span,
                    type=e.type,
                    is_correct=(e.type == "法人名")
                )
                for e in entity.entities
            ]
            annotated_named_entity = AnnotatedNamedEntity(
                curid=entity.curid,
                tokens=self._analyzer.analyze(entity.text),
                entities=annotated_entites
            )
            results.append(annotated_named_entity)
        return results
