import pandera as pa
from pandera.typing import Series


class Users(pa.DataFrameModel):
    name: Series[str]
    age: Series[int]
