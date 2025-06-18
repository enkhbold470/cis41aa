"""
# Author: Inky Ganbold
# CIS41A
# Chapter 12 Exercise 2
# Team: Python Enjoyers
# This program creates a Fibonacci sequence using Iterator and Generator.

"""


# ITERATOR APPROACH - Using a simple class with __iter__ and __next__

class FibIterator:
    """Simple Fibonacci iterator"""
    
    def __init__(self, max_count=10):
        self.max_count = max_count
        self.count = 0
        self.current = 1
        self.next_val = 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count >= self.max_count:
            raise StopIteration
        
        result = self.current
        self.current, self.next_val = self.next_val, self.current + self.next_val
        self.count += 1
        return result


# GENERATOR APPROACH - Using yield (Functional Programming)

def fib_generator(max_count=10):
    """Simple Fibonacci generator function"""
    count = 0
    current = 1
    next_val = 1
    
    while count < max_count:
        yield current
        current, next_val = next_val, current + next_val
        count += 1


# ALTERNATIVE GENERATOR - Infinite Fibonacci generator

def fib_infinite():
    """Infinite Fibonacci generator"""
    current = 1
    next_val = 1
    
    while True:
        yield current
        current, next_val = next_val, current + next_val


# FUNCTIONAL APPROACH - Using generator with take function

def take(n, iterable):
    """Take first n items from iterable"""
    count = 0
    for item in iterable:
        if count >= n:
            break
        yield item
        count += 1


# MAIN PROGRAM

if __name__ == "__main__":
    print("Fibonacci Numbers using Iterator and Generator")
    print("=" * 50)
    
    # Test both approaches
    print("First 10 Fibonacci numbers:")
    print(f"Iterator:  {list(FibIterator(10))}")
    print(f"Generator: {list(fib_generator(10))}")
    
    print("\nFirst 6 numbers step by step:")
    for i, num in enumerate(fib_generator(6), 1):
        print(f"  Step {i}: {num}")
        
        
"""
➜  cis41aa git:(main) python3 ch12-ex2.py
Fibonacci Numbers using Iterator and Generator
==================================================
First 10 Fibonacci numbers:
Iterator:  [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
Generator: [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

First 6 numbers step by step:
  Step 1: 1
  Step 2: 1
  Step 3: 2
  Step 4: 3
  Step 5: 5
  Step 6: 8
"""