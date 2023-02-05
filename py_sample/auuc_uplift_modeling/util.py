import random
from typing import Tuple
from operator import itemgetter

import numpy as np
import pandas as pd


class DataGenerator:
    def generate(self, n_data: int, seed: int=1) -> Tuple[list, list, list]:
        conversions = []
        treatments = []
        features = []

        random_instance = random.Random(seed)

        n_features = 8
        base_weights = [0.02, 0.03, 0.05, -0.04, .0, .0, .0, .0]
        lift_weights = [.0, .0, .0, 0.05, -0.05, .0, .0, .0]

        for i in range(n_data):
            feature = [random_instance.random() for _ in range(n_features)]
            treatment = random_instance.choice((True, False))
            conversion_rate = sum(map(lambda x: x[0]*x[1], zip(feature, base_weights)))

            if treatment:
                conversion_rate += sum(map(lambda x: x[0]*x[1], zip(feature, lift_weights)))
            
            conversion = conversion_rate > random_instance.random()

            conversions.append(conversion)
            treatments.append(treatment)
            features.append(feature)
        
        return conversions, treatments, features


def create_score_tables(conversions: list, treatments: list, scores: np.ndarray) -> pd.DataFrame:
    results = list(zip(conversions, treatments, scores))
    results.sort(key=itemgetter(2), reverse=True)

    n = 10
    df = pd.DataFrame(columns=["cvr_treatment", "cvr_control"])
    for i in range(n):
        start = int(i * len(results)/n)
        end = int((i+1) * len(results)/n) - 1
        quantile_results = results[start: end]

        n_treatment = list(map(lambda result: result[1], quantile_results)).count(True)
        n_control = len(quantile_results) - n_treatment

        cv_treatment = list(
            map(
                lambda result: result[0],
                filter(
                    lambda result: result[1],
                    quantile_results
                )
            )
        ).count(True)
        cv_control = list(
            map(
                lambda result: result[0],
                filter(
                    lambda result: not result[1],
                    quantile_results
                )
            )
        ).count(True)

        cvr_treatment = cv_treatment / n_treatment
        cvr_control = cv_control / n_control

        label = f"{i*10}%~{(i+1)*10}%"
        df.loc[label] = [cvr_treatment, cvr_control]

    return df
