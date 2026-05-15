from itertools_lib.auth_proxy import APIProxy, APIKeyAuth, JWTAuth

def run_demo():
    print("=== Тестування Authentication Proxy (Task 8) ===")

    print("\n--- випадок 1: API Key ---")
    key_auth = APIKeyAuth(api_key="oxy-secret-key-123")
    proxy = APIProxy(key_auth)
    proxy.send_request("/v1/user/profile", {"id": 1})

    print("\n--- випадок 2: Перемикання на JWT ---")
    jwt_auth = JWTAuth(token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...")
    proxy.set_strategy(jwt_auth)
    proxy.send_request("/v1/admin/dashboard")

if __name__ == "__main__":
    run_demo()