from abc import ABC, abstractmethod
import time

class AuthStrategy(ABC):
    @abstractmethod
    def add_auth(self, headers: dict) -> dict:
        pass

class APIKeyAuth(AuthStrategy):
    def __init__(self, api_key: str):
        self.api_key = api_key

    def add_auth(self, headers: dict) -> dict:
        headers["X-API-KEY"] = self.api_key
        return headers

class JWTAuth(AuthStrategy):
    def __init__(self, token: str):
        self.token = token

    def add_auth(self, headers: dict) -> dict:
        headers["Authorization"] = f"Bearer {self.token}"
        return headers

class APIProxy:
    def __init__(self, strategy: AuthStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: AuthStrategy):
        self.strategy = strategy

    def send_request(self, endpoint: str, payload: dict = None):
        headers = {"Content-Type": "application/json"}
        headers = self.strategy.add_auth(headers)
        
        print(f"[Proxy Log]: Запит до {endpoint}")
        print(f"[Proxy Log]: Заголовки: {headers}")
        print(f"[Proxy Log]: Дані: {payload}")
        return {"status": 200, "message": "Успішно авторизовано!"}