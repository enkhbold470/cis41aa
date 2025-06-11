# Inky Ganbold - CIS 41 Midterm
# 6/11/2025
# Chapter 2 Exercise 2
# Team: Python Enjoyers

import math
import tkinter as tk
from tkinter import simpledialog

def main():
    # Initialize window
    r = tk.Tk()
    r.title("CIS40 - Ch2 Ex2")
    
    # Get inputs
    w = simpledialog.askinteger("Input", "Enter width:", initialvalue=400)
    h = simpledialog.askinteger("Input", "Enter height:", initialvalue=300)
    rad = simpledialog.askfloat("Input", "Enter radius:", initialvalue=50)
    oc = simpledialog.askstring("Input", "Enter outline color:", initialvalue="blue")
    fc = simpledialog.askstring("Input", "Enter fill color:", initialvalue="red")
    n = simpledialog.askstring("Input", "Enter name:", initialvalue="Inky")
    
    # Setup canvas
    c = tk.Canvas(r, width=w, height=h, bg='#FFFFE0')
    c.pack()
    
    # Calculate positions
    cx = w / 2
    cy = h / 2
    
    # Draw circle
    c.create_oval(cx - rad, cy - rad, cx + rad, cy + rad,
                 outline=oc, fill=fc, width=5)
    
    # Calculate metrics
    circ = 2 * math.pi * rad
    a = math.pi * rad * rad
    
    # Display info
    tx = 0.01 * w
    ty = 0.01 * h
    msg = f"{n}\nCircumference: {circ:.2f}\nArea: {a:.2f}"
    c.create_text(tx, ty, anchor="nw", text=msg)
    
    # Print results
    print(f"Circumference: {circ:.2f}")
    print(f"Area: {a:.2f}")
    
    r.mainloop()

if __name__ == "__main__":
    main()

'''
Test Run 1:
Enter width: 400
Enter height: 300
Enter radius: 50
Enter outline color: blue
Enter fill color: red
Enter name: Inky
Circumference: 314.16
Area: 7853.98

Test Run 2:
Enter width: 600
Enter height: 400
Enter radius: 75
Enter outline color: green
Enter fill color: yellow
Enter name: Inky
Circumference: 471.24
Area: 17671.46
'''
