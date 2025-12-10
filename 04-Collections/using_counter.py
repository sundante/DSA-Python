from collections import Counter

def demonstrate_counter_basics():
    print("\n--- Counter Basics ---")
    # Initialize from a list
    colors = ['red', 'blue', 'red', 'green', 'blue', 'blue']
    c = Counter(colors)
    print(f"Count of colors: {c}")
    
    # Initialize from a string
    s = "mississippi"
    c_str = Counter(s)
    print(f"Count of characters in '{s}': {c_str}")

    # Accessing counts
    print(f"Count of 'blue': {c['blue']}")
    print(f"Count of 'yellow' (missing): {c['yellow']}") # Returns 0, doesn't raise KeyError

def demonstrate_methods():
    print("\n--- Counter Methods ---")
    c = Counter(a=4, b=2, c=0, d=-2)
    print(f"Counter: {c}")

    # elements() - returns an iterator over elements repeating each as many times as its count
    elements = list(c.elements())
    print(f"Elements (expanded): {elements}") # Note: ignores counts <= 0

    # most_common()
    s = "abracadabra"
    c_common = Counter(s)
    print(f"Counter('{s}'): {c_common}")
    print(f"Most common 3: {c_common.most_common(3)}")
    
    # subtract()
    c1 = Counter(a=4, b=2)
    c2 = Counter(a=1, b=2)
    c1.subtract(c2)
    print(f"After subtract (a=4, b=2) - (a=1, b=2): {c1}")

    # update()
    c1.update(c2) # Adds counts
    print(f"After update (adding back): {c1}")

def demonstrate_arithmetic():
    print("\n--- Counter Arithmetic ---")
    c1 = Counter(a=3, b=1)
    c2 = Counter(a=1, b=2)
    print(f"c1: {c1}, c2: {c2}")

    # Addition
    print(f"Addition (c1 + c2): {c1 + c2}")

    # Subtraction
    print(f"Subtraction (c1 - c2): {c1 - c2}") # Keeps only positive counts

    # Intersection (min)
    print(f"Intersection (c1 & c2): {c1 & c2}")

    # Union (max)
    print(f"Union (c1 | c2): {c1 | c2}")
    
    # Unary operations
    c3 = Counter(a=2, b=-4)
    print(f"c3: {c3}")
    print(f"+c3 (remove non-positive): {+c3}")
    print(f"-c3 (negate and remove non-positive): {-c3}")

if __name__ == "__main__":
    demonstrate_counter_basics()
    demonstrate_methods()
    demonstrate_arithmetic()
