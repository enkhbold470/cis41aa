# Name: Inky Ganbold
# Date: 6/11/2025
# CIS41A
# Chapter 9 Assignment - Bug Class
# Team: Python Enjoyers
# This program implements a Bug class that models a bug moving along a horizontal line.
# The bug can move left or right and can turn to change direction.

class Bug:
    def __init__(self, p):
        self._p = p
        self._d = 1
    
    def turn(self):
        self._d = -self._d
    
    def move(self):
        self._p += self._d
    
    def getPosition(self):
        return self._p

def main():
    print("Bug Movement Simulation")
    print("=" * 30)
    
    b = Bug(10)
    print(f"Initial position: {b.getPosition()} (Expected: 10)")
    
    b.move()
    print(f"After first move: {b.getPosition()} (Expected: 11)")
    
    b.turn()
    print("Bug turned around (now facing left)")
    
    b.move()
    print(f"After second move: {b.getPosition()} (Expected: 10)")
    
    b.move()
    print(f"After third move: {b.getPosition()} (Expected: 9)")
    
    b.turn()
    print("Bug turned around (now facing right)")
    
    b.move()
    print(f"After fourth move: {b.getPosition()} (Expected: 10)")
    
    b.move()
    print(f"After fifth move: {b.getPosition()} (Expected: 11)")
    
    print("\n" + "=" * 30)
    print("Testing with another bug...")
    
    b2 = Bug(5)
    print(f"Bug2 initial position: {b2.getPosition()} (Expected: 5)")
    
    b2.move()
    b2.move()
    print(f"Bug2 after moving right twice: {b2.getPosition()} (Expected: 7)")
    
    b2.turn()
    b2.move()
    b2.move()
    b2.move()
    print(f"Bug2 after turning and moving left 3 times: {b2.getPosition()} (Expected: 4)")

if __name__ == "__main__":
    main()

'''
Sample Output:

Bug Movement Simulation
==============================
Initial position: 10 (Expected: 10)
After first move: 11 (Expected: 11)
Bug turned around (now facing left)
After second move: 10 (Expected: 10)
After third move: 9 (Expected: 9)
Bug turned around (now facing right)
After fourth move: 10 (Expected: 10)
After fifth move: 11 (Expected: 11)

==============================
Testing with another bug...
Bug2 initial position: 5 (Expected: 5)
Bug2 after moving right twice: 7 (Expected: 7)
Bug2 after turning and moving left 3 times: 4 (Expected: 4)
''' 