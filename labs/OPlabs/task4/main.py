from itertools_lib.priority_queue import BiDirectionalPriorityQueue

def run_demo():
    pq = BiDirectionalPriorityQueue()
    
    print("--- Додавання елементів ---")
    pq.enqueue("Завдання А", priority=10) 
    pq.enqueue("Завдання Б", priority=5)  
    pq.enqueue("Завдання В", priority=20) 
    pq.enqueue("Завдання Г", priority=15) 
    
    print(f"Peek Highest: {pq.peek('highest')}") 
    print(f"Peek Lowest: {pq.peek('lowest')}")   
    print(f"Peek Oldest: {pq.peek('oldest')}")   
    print(f"Peek Newest: {pq.peek('newest')}")  
    
    print("\n--- Видалення за пріоритетом ---")
    print(f"Dequeue Highest: {pq.dequeue('highest')}") 
    print(f"Dequeue Lowest: {pq.dequeue('lowest')}")   
    
    print("\n--- Залишки за чергою вставки ---")
    print(f"Dequeue Oldest: {pq.dequeue('oldest')}")   
    print(f"Dequeue Newest: {pq.dequeue('newest')}")   

if __name__ == "__main__":
    run_demo()