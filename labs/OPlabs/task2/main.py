from itertools_lib import fibonacci_generator, consume_with_timeout
import time

def run_demo():
    print("Starting demonstration...")

    fib_gen = fibonacci_generator()
    
    for val in consume_with_timeout(fib_gen, 3):
        print(f"Value: {val}")
        time.sleep(0.1) 

    print("Timeout reached.")

if __name__ == "__main__":
    run_demo()