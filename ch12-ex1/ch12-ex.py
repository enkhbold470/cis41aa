# Inky Ganbold - CIS 41
# Team: Python Enjoyers
# Chapter 12 - Exercise 1 - Read and write in csv and using "assert"
# it is a program that reads a csv file and writes a new csv file
# the new csv file is a total of the quantities of the burgers

import csv
import os

def read_order(filename):
    order_dict = {}
    total_order_dict = {}
    
    path = os.path.join(os.path.dirname(__file__), filename)
    with open(filename, 'r') as file:
        for line in file:
            data = line.strip().split(',')
            burger_num = data[0]
            quantities = [int(x) for x in data[1:]]
            
            order_dict[burger_num] = quantities
            total_order_dict[burger_num] = sum(quantities)
    
    print("Order Dictionary:", order_dict)
    print("Total Order Dictionary:", total_order_dict)
    
    return total_order_dict

def test_sum():
    expected_result_total_order_dict = {'1': 91, '2': 100, '3': 32, '4': 62, '5': 64}
    
    assert actual_result_total_order_dict['1'] == expected_result_total_order_dict['1'], \
        "The actual result is not the same as expected result for the order number 1!"
    
    assert actual_result_total_order_dict['2'] == expected_result_total_order_dict['2'], \
        "The actual result is not the same as expected result for the order number 2!"
    
    assert actual_result_total_order_dict['3'] == expected_result_total_order_dict['3'], \
        "The actual result is not the same as expected result for the order number 3!"
    
    assert actual_result_total_order_dict['4'] == expected_result_total_order_dict['4'], \
        "The actual result is not the same as expected result for the order number 4!"
    
    assert actual_result_total_order_dict['5'] == expected_result_total_order_dict['5'], \
        "The actual result is not the same as expected result for the order number 5!"

def write_order_csv(total_order_dict, output_file):
    with open(output_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        for key in total_order_dict.keys():
            writer.writerow([key, total_order_dict[key]])
    
    print(f"Output written to {output_file}")

actual_result_total_order_dict = {}

if __name__ == "__main__":
    print("=== Sample Run 1 ===")
    actual_result_total_order_dict = read_order("order.csv")
    test_sum()
    print("Everything passed")
    write_order_csv(actual_result_total_order_dict, "outputfile.csv")
    
    print("\n=== Sample Run 2 ===")
    actual_result_total_order_dict = read_order("order.csv")
    test_sum()
    print("Everything passed")
    write_order_csv(actual_result_total_order_dict, "outputfile.csv")
    
    
"""
here is the sample run 1:

(base) PS C:\Users\inky-ryzen-machine\Desktop\cis41aa\ch12-ex1> python3 .\ch12-ex.py
=== Sample Run 1 ===
Order Dictionary: {'1': [10, 3, 78], '2': [35, 0, 65], '3': [9, 23, 0], '4': [0, 19, 43], '5': [43, 0, 21]}
Total Order Dictionary: {'1': 91, '2': 100, '3': 32, '4': 62, '5': 64}
Everything passed
Output written to outputfile.csv

=== Sample Run 2 ===
Order Dictionary: {'1': [10, 3, 78], '2': [35, 0, 65], '3': [9, 23, 0], '4': [0, 19, 43], '5': [43, 0, 21]}
Total Order Dictionary: {'1': 91, '2': 100, '3': 32, '4': 62, '5': 64}
Everything passed
Output written to outputfile.csv
"""