from model_selection import treatment_control_split
from util import DataGenerator, create_score_tables

from sklearn.linear_model import LogisticRegression


def main():
    generator = DataGenerator()

    n_train = 10000
    y_train, t_train, X_train = generator.generate(n_train)
    y_treatment, y_control, X_treatment, X_control = treatment_control_split(
        y_train,
        X_train,
        t_train
    )
    print(f"cvr(treatment): {y_treatment.count(True)/len(y_treatment)}")
    print(f"cvr(control)  : {y_control.count(True)/len(y_control)}")
    print()

    print("model training...")
    model_treatment = LogisticRegression(C=0.01)
    model_treatment.fit(X_treatment, y_treatment)

    model_control = LogisticRegression(C=0.01)
    model_control.fit(X_control, y_control)

    n_test = 10000
    y_test, t_test, X_test = generator.generate(n_test, seed=42)
    score_treatment = model_treatment.predict_proba(X_test)
    score_control = model_control.predict_proba(X_test)

    print("uplift scores:")
    scores = score_treatment[:, 1] / score_control[:, 1]
    df = create_score_tables(y_test, t_test, scores)
    print(df)

    print("DONE")


if __name__ == "__main__":
    main()
