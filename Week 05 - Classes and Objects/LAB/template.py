"""
RECORD CHECK  -  my version
===========================

Name  :  SIANAH SUNASSY
Lane  :  IT      
Date  :  25/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

class Record:
    def __init__(self, label, value, limit):
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        """It must the return the status based on its value and limit"""
        if self.value >= self.limit:
            return "OVER LIMIT"
        elif self.value >= self.limit * 0.9:
            return "WARNING"
        else:
            return "OK"
        
records = [
    Record("R-001", 92, 100),
    Record("R-002", 75, 100),
    Record("R-003", 105, 100)
]

for record in records:
    print()
    print("=" * 34)
    print(f" Record Check - {record.label}")
    print("=" * 34)

    print(f" value: {record.value}")
    print(f" limit: {record.limit}")
    print(f" status: {record.status()}")
    print("=" * 34)



