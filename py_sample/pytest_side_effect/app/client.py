from typing import Dict, Optional, Union


class DummyClient:
    def __init__(self, host: str = "localhost", port: int = 8080) -> None:
        self._host = host
        self._port = port

    def scroll(self, token: Optional[str]=None) -> Dict[str, Optional[Union[str, int]]]:
        if token == "first":
            return {"id": 1, "name": "first_item", "next_token": "second"}
        
        if token == "second":
            return {"id": 2, "name": "second_item", "next_token": None}
        
        return  {"id": 3, "name": "none_item", "next_token": "first"}


class SearchClient:
    def __init__(self) -> None:
        self._client = DummyClient()
    
    def scroll(self, token: str) -> Dict[str, Optional[Union[str, int]]]:
        return self._client.scroll(token)
