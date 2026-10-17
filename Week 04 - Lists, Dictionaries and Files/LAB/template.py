"""
RECORD CHECK  -  my version
===========================

Name  : Sianah Sunassy
Lane  :  IT      
Date  :  14/10/2026

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
    
def check_record(value, limit):
    "Calculate and return the difference and percentage and status"
    difference = value - limit
    percent = (value / limit) * 100
    status = status_of(percent)
    return (difference, percent,status)

difference, percent, status = check_record(value, limit)
status = status_of(percent)

def print_report(label, value, limit, difference, percent, status):
    """Print all the record"""
print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)
print(f"{value:>10.2f}")
print(f"{limit:>10.2f}")
print(f"{difference:>10.2f}")
print(f"{percent:>10.2f}")
print(status)
print("=" * 34)

def load_records(path):
    """Read records from a file and return as dictionaries"""
    records = []
    with open(path, "r") as file:
        for line in file:
            label,value, limit = line.strip().split(",")
            record = {
                "label": label,
                "value": float(value),
                "limit": float(limit)
            }
            records.append(record)
            return records

        records = load_records("records.txt")

    for record in records:
        difference, percent, status = check_record(
            record["value"],
            record["limit"]
        )

        print_report(
            record["label"],
            record["value"],
            record["limit"],
            difference,
            percent,
            status
        )

