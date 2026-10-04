"""
RECORD CHECK  -  my version
===========================

Name  : Sianah Sunassy
Lane  :   IT      
Date  : 03/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
label = input("Enter a hostname")
first = float(input("Enter your number: "))
second = float(input("Enter your number: "))
difference = second - first
percentage = (first / second) * 100
print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)
print(first)
print(second)
print(f"{first:>+10.2f}")
print(f"{second:>+10.2f}")
print(f"{difference:>+10.2f}")
print(f"{percentage:>+10.2f}")

# =================================================================== OUTPUT
# 3. Print the report.
#
#    Threshold : print the three values you were given, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : difference always shows its sign, plus one line of your own
#
#    Useful:   f"{value:>10.2f}"    right-aligned, 2 decimal places
#              f"{value:>+10.2f}"   the same, but always shows the sign


# : your report lines go here

print("=" * 34)


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and write the error in your journal
#    [ ] Check every variable name says what it holds
#    [ ] Show it to the person next to you
