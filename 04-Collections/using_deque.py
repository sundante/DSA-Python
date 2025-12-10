from collections import deque

def demonstrate_deque_basics():
    print("\n--- Deque Basics ---")
    # Initialize a deque
    d = deque(['a', 'b', 'c'])
    print(f"Initialized deque: {d}")

    # Append to right
    d.append('d')
    print(f"After append('d'): {d}")

    # Append to left
    d.appendleft('z')
    print(f"After appendleft('z'): {d}")

    # Pop from right
    item = d.pop()
    print(f"Popped from right: {item}, Deque: {d}")

    # Pop from left
    item = d.popleft()
    print(f"Popped from left: {item}, Deque: {d}")

def demonstrate_maxlen():
    print("\n--- Maxlen (Circular Buffer) ---")
    # Initialize with maxlen
    d = deque(maxlen=3)
    
    for i in range(5):
        d.append(i)
        print(f"Added {i}, Deque: {d}")
    
    print("Note how older elements are discarded when maxlen is reached.")

def demonstrate_rotation():
    print("\n--- Rotation ---")
    d = deque([1, 2, 3, 4, 5])
    print(f"Original: {d}")

    # Rotate right
    d.rotate(1)
    print(f"Rotate right (1): {d}")

    # Rotate left (negative number)
    d.rotate(-2)
    print(f"Rotate left (-2): {d}")

def demonstrate_other_ops():
    print("\n--- Other Operations ---")
    d = deque(['a', 'b', 'c', 'd', 'e'])
    print(f"Original: {d}")
    
    # Extend
    d.extend(['f', 'g'])
    print(f"Extend ['f', 'g']: {d}")
    
    # Extend left
    d.extendleft(['y', 'x']) # Note: adds y then x, so order is x, y...
    print(f"Extendleft ['y', 'x']: {d}")
    
    # Reverse
    d.reverse()
    print(f"Reversed: {d}")

    # Count
    d.append('a')
    count_a = d.count('a')
    print(f"Count of 'a': {count_a}")

if __name__ == "__main__":
    demonstrate_deque_basics()
    demonstrate_maxlen()
    demonstrate_rotation()
    demonstrate_other_ops()
