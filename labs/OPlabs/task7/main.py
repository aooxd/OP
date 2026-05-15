from itertools_lib.reactive import EventEmitter

def run_demo():
    emitter = EventEmitter()

    def chat_bot_listener(message):
        print(f"[ChatBot]: Отримано нове повідомлення — '{message}'")

    def logger_listener(message):
        print(f"[Logger]: Запис у системний журнал: {message}")

    print("--- 1. Тест: Декілька слухачів на одну подію ---")
    unsub_chat = emitter.subscribe("message", chat_bot_listener)
    emitter.subscribe("message", logger_listener)

    emitter.emit("message", "hello!")

    print("\n--- 2. Тест: Відписка (Unsubscribe) ---")
    unsub_chat()
    
    print("Після того, як ChatBot відписався:")
    emitter.emit("message", "Тестове повідомлення 2")

    print("\n--- 3. Тест: Робота з іншими подіями ---")
    emitter.subscribe("alert", lambda data: print(f"!!! УВАГА: {data} !!!"))
    emitter.emit("alert", "Система перегріта")

if __name__ == "__main__":
    run_demo()