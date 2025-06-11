# Author: Inky Ganbold
# CIS41A
# Chapter 6 Exercise 3
# Team: Python Enjoyers
# This program creates a medal table using lists, calculates totals,
# removes countries without gold medals, and compares list vs dictionary storage.

def main():
    tbl = [
        ["Canada", 0, 3, 0],
        ["Italy", 0, 0, 1],
        ["Germany", 0, 0, 1],
        ["Japan", 1, 0, 0],
        ["Russia", 3, 1, 1],
        ["South Korea", 0, 1, 0],
        ["United States", 1, 0, 1]
    ]
    
    print("Figure Skating Medal Counts")
    print("=" * 40)
    print(f"{'Country':<15} {'Gold':<6} {'Silver':<6} {'Bronze':<6}")
    print("-" * 40)
    
    for c in tbl:
        print(f"{c[0]:<15} {c[1]:<6} {c[2]:<6} {c[3]:<6}")
    
    print()
    
    tot = 0
    g = 0
    s = 0
    b = 0
    
    for c in tbl:
        g += c[1]
        s += c[2]
        b += c[3]
        tot += c[1] + c[2] + c[3]
    
    print(f"Total number of medals: {tot}")
    print(f"Total gold medals: {g}")
    print(f"Total silver medals: {s}")
    print(f"Total bronze medals: {b}")
    print()
    
    gold = []
    for c in tbl:
        if c[1] > 0:
            gold.append(c)
    
    print("Countries with Gold Medals:")
    print("=" * 40)
    print(f"{'Country':<15} {'Gold':<6} {'Silver':<6} {'Bronze':<6}")
    print("-" * 40)
    
    for c in gold:
        print(f"{c[0]:<15} {c[1]:<6} {c[2]:<6} {c[3]:<6}")
    
    print()
    
    d1 = {}
    for c in tbl:
        d1[c[0]] = [c[1], c[2], c[3]]
    
    print("Dictionary with list values (country: [gold, silver, bronze]):")
    print("=" * 65)
    for c, m in d1.items():
        print(f"{c}: {m}")
    
    print()
    
    d2 = {}
    for c in tbl:
        d2[c[0]] = {
            "Gold": c[1],
            "Silver": c[2],
            "Bronze": c[3]
        }
    
    print("Dictionary with nested dictionary values:")
    print("=" * 50)
    for c, m in d2.items():
        print(f"{c}: {m}")

if __name__ == "__main__":
    main()
    
    
# (cis41aa) ➜  cis41aa git:(main) ✗ uv run ch6-ex3.py
# Figure Skating Medal Counts
# ========================================
# Country         Gold   Silver Bronze
# ----------------------------------------
# Canada          0      3      0     
# Italy           0      0      1     
# Germany         0      0      1     
# Japan           1      0      0     
# Russia          3      1      1     
# South Korea     0      1      0     
# United States   1      0      1     

# Total number of medals: 14
# Total gold medals: 5
# Total silver medals: 5
# Total bronze medals: 4

# Countries with Gold Medals:
# ========================================
# Country         Gold   Silver Bronze
# ----------------------------------------
# Japan           1      0      0     
# Russia          3      1      1     
# United States   1      0      1     

# Dictionary with list values (country: [gold, silver, bronze]):
# =================================================================
# Canada: [0, 3, 0]
# Italy: [0, 0, 1]
# Germany: [0, 0, 1]
# Japan: [1, 0, 0]
# Russia: [3, 1, 1]
# South Korea: [0, 1, 0]
# United States: [1, 0, 1]

# Dictionary with nested dictionary values:
# ==================================================
# Canada: {'Gold': 0, 'Silver': 3, 'Bronze': 0}
# Italy: {'Gold': 0, 'Silver': 0, 'Bronze': 1}
# Germany: {'Gold': 0, 'Silver': 0, 'Bronze': 1}
# Japan: {'Gold': 1, 'Silver': 0, 'Bronze': 0}
# Russia: {'Gold': 3, 'Silver': 1, 'Bronze': 1}
# South Korea: {'Gold': 0, 'Silver': 1, 'Bronze': 0}
# United States: {'Gold': 1, 'Silver': 0, 'Bronze': 1}
# (cis41aa) ➜  cis41aa git:(main) ✗ 