"""
RECORD CHECK  -  my version
===========================

Name  :   Sianah Sunassy
Lane  :   IT      
Date  :   10/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

label = input("Enter a hostname: ")
value = float(input("Enter your value: "))
limit= float(input("Enter your limit: "))

def status_of(percent):
    """return the result based on the percentage"""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >=90:
        return "WARNING"
    else:
        return "OK"
    
def check(value, limit):
    "Calculate and return the difference and percentage"
    difference = value - limit
    percent = (value / limit) * 100
    return (difference, percent)

difference, percent = check(value, limit)
status = status_of(percent)


def print_report(label, value, limit, difference, percent, status):
    """Print all the record"""
print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)
print(value)
print(limit)
print(f"{value:>10.2f}")
print(f"{limit:>10.2f}")
print(f"{difference:>10.2f}")
print(f"{percent:>10.2f}")
print(status)
print("=" * 34)







# =================================================================== OUTPUT
# 4. Print the report.
#
#    Threshold : the three values you were given, plus status, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : call print_report() instead of printing directly here, and
#                wrap sections 2-4 in a loop so you can check as many records
#                as you like in one run - type "quit" as the label to stop.
#                Keep count of how many came back OVER LIMIT and print that
#                once, after the loop ends.



# your report lines go here



# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every function does one job - if a function both calculates
#        and prints, split it
