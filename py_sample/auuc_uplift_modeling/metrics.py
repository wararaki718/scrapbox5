import numpy as np
import pandas as pd


def get_metrics_table(conversions: list, treatments: list, scores: np.ndarray) -> pd.DataFrame:
    n_treatment = 0
    n_cv_treatment = 0
    cvr_treatment = 0
    n_control = 0
    n_cv_control = 0
    cvr_control = 0
    results = []
    for conversion, treatment, score in zip(conversions, treatments, scores):
        if treatment:
            n_treatment += 1
            if conversion:
                n_cv_treatment += 1
            cvr_treatment = n_cv_treatment / n_treatment
        else:
            n_control += 1
            if conversion:
                n_cv_control += 1
            cvr_control = n_cv_control / n_control

        lift = (cvr_treatment - cvr_control) * n_treatment

        results.append({
            "conversion": conversion,
            "treatment": treatment,
            "score": score,
            "n_treatment": n_treatment,
            "n_control": n_control,
            "cv_treatment": n_cv_treatment,
            "cv_control": n_cv_control,
            "cvr_treatment": cvr_treatment,
            "cvr_control": cvr_control,
            "lift": lift
        })
    
    df = pd.DataFrame(results)
    df["base"] = df.index * df.lift[df.shape[0]-1] / df.shape[0]

    return df


def auuc_score(lift: pd.Series, base: pd.Series) -> float:
    return (lift.values - base.values).sum() / lift.shape[0]
