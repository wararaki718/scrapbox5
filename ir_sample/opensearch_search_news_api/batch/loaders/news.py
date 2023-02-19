from pathlib import Path
from typing import List

import pandas as pd

from schemas.news import News


class NewsLoader:
    @classmethod
    def load(cls, news_path: Path) -> List[News]:
        df = pd.read_csv(news_path)
        df.rename(columns={"id": "newsid"}, inplace=True)
        return [News(**news) for news in df.to_dict(orient="records")]
