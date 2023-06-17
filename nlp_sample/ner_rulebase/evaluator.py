from collections import defaultdict
from typing import Dict, List, Tuple, Union

from schema import AnnotatedNamedEntity, Result

class NEREvaluator:
    def __init__(self) -> None:
        pass

    def evaluate(self, sentences: List[AnnotatedNamedEntity], predictions: List[List[Union[Result, None]]]) -> Tuple[Dict[str, int], float, float, float]:
        metrics = defaultdict(int)

        for sentence, results in zip(sentences, predictions):
            if results is None:
                continue
            for entity, result in zip(sentence.entities, results):
                metrics["TP"] += int(entity.is_correct and result is not None)
                metrics["TN"] += int(not entity.is_correct and result is None)
                metrics["FN"] += int(entity.is_correct and result is None)
                metrics["FP"] += int(not entity.is_correct and result is not None)
        
        accuracy = (metrics["TP"] + metrics["TN"]) / (metrics["TP"] + metrics["TN"] + metrics["FN"] + metrics["FP"])
        precision =  metrics["TP"] / (metrics["TP"] + metrics["FP"])
        recall = metrics["TP"] / (metrics["TP"] + metrics["FN"])

        return metrics, accuracy, precision, recall
