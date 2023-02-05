from typing import Tuple


def treatment_control_split(y: list, X: list, treatments: list) -> Tuple[list, list, list, list]:
    y_control = []
    X_control = []
    y_treatment = []
    X_treatment = []
    for i, treatment in enumerate(treatments):
        if treatment:
            y_treatment.append(y[i])
            X_treatment.append(X[i])
        else:
            y_control.append(y[i])
            X_control.append(X[i])
    
    return y_treatment, y_control, X_treatment, X_control
