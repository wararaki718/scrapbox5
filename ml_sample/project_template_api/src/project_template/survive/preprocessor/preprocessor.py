from .components import AgesCategorizer
from project_template.schema.data import PreprocessedData
from project_template.schema.request import Passenger


class PassengerPreprocessor:
    def __init__(self) -> None:
        self._ages_categorizer = AgesCategorizer()

    def transform(self, passenger: Passenger) -> PreprocessedData:
        return PreprocessedData(
            Pclass = [[passenger.Pclass]],
            Age = [[passenger.Age]],
            Embarked = [[passenger.Embarked]],
            Ages = [[self._ages_categorizer.transform(passenger.Age)]]
        )
