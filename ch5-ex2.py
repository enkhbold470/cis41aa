# author: Inky Ganbold
# team: Python Enjoyers
# date: may 8
# course: cis41 - python class
# description: this program calculates gross pay with simple input checks and output.

def get_input():
    while True:
        company = input("enter your company name: ").strip()
        if company != "":
            break
        print("company name can't be empty. try again.")

    while True:
        hours_input = input("enter the hours: ").strip()
        try:
            hours = float(hours_input)
            if hours < 0:
                print("hours can't be negative. try again.")
                continue
            break
        except:
            print("invalid input. enter a number for hours.")

    while True:
        rate_input = input("enter the rate: ").strip()
        try:
            rate = float(rate_input)
            if rate < 0:
                print("rate can't be negative. try again.")
                continue
            break
        except:
            print("invalid input. enter a number for rate.")

    return company, hours, rate

def compute_pay(hours, rate):
    if hours > 40:
        overtime = hours - 40
        pay = (40 * rate) + (overtime * rate * 1.5)
    else:
        pay = hours * rate
    return pay

def print_output(company, hours, rate, pay):
    print("**********************************************")
    print("company:", company)
    print("hours:", hours)
    print("rate: $", rate)
    print("your gross pay for", company, "is $", pay)

def main():
    company, hours, rate = get_input()
    pay = compute_pay(hours, rate)
    print_output(company, hours, rate, pay)

main()
