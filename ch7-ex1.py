# Name: Inky Ganbold
# Date: 6/10/2025
# CIS41A
# Chapter 7 Exercise 1
# Team: Python Enjoyers
# This program reads an error log file, counts non-empty lines,
# detects lines with the word "error" (case-sensitive), and writes a report.

def analyze_error_log():
    """
    Main function to analyze error log file and generate report
    """
    # Prompt user for filename
    filename = input("Enter the name of the error log file: ")
    
    try:
        # Read the file and analyze content
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        # Count non-empty lines
        non_empty_lines = []
        for line in lines:
            if line.strip():  # Remove whitespace and check if line is not empty
                non_empty_lines.append(line)
        
        non_empty_count = len(non_empty_lines)
        
        # Search for error lines (case-sensitive)
        error_lines = []
        for line in non_empty_lines:
            if "error" in line or "Error" in line or "ERROR" in line:
                error_lines.append(line.strip())
        
        error_count = len(error_lines)
        
        # Print results to console
        print(f"Total non-empty lines: {non_empty_count}")
        print(f"Number of error lines: {error_count}")
        
        if error_lines:
            for i, error_line in enumerate(error_lines, 1):
                print(f"error line {i}: {error_line}")
        
        # Write report to reportError.txt
        with open('reportError.txt', 'w') as report_file:
            report_file.write(f"Error Log Analysis Report\n")
            report_file.write(f"========================\n\n")
            report_file.write(f"Total non-empty lines: {non_empty_count}\n")
            report_file.write(f"Number of error lines: {error_count}\n\n")
            
            if error_lines:
                report_file.write("Error lines found:\n")
                report_file.write("-" * 20 + "\n")
                for i, error_line in enumerate(error_lines, 1):
                    report_file.write(f"error line {i}: {error_line}\n")
        
        print(f"\nReport saved to reportError.txt")
        
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        print("Please make sure the file exists in the current directory.")
    except IOError:
        print(f"Error: Could not read the file '{filename}'.")
        print("Please check file permissions.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    analyze_error_log()

'''
Sample output:

Enter the name of the error log file: ErrorLog.txt
Total non-empty lines: 108
Number of error lines: 5
error line 1: 2023-10-15 14:23:45 [ERROR] Database connection failed
error line 2: 2023-10-15 15:12:33 [Error] Invalid user credentials
error line 3: 2023-10-15 16:45:22 [error] File not found: config.xml
error line 4: 2023-10-15 17:30:15 [ERROR] Memory allocation failed
error line 5: 2023-10-15 18:15:08 [Error] Network timeout occurred

Report saved to reportError.txt
''' 