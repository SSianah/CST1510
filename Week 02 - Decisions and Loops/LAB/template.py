"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :   IT      
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
label = input("Enter a hostname")
first = float(input("Enter your number: "))
second= float(input("Enter your number: "))
difference =  second - first
percentage = (first / second) * 100
if percentage >= 100:
    status = "OVER LIMIT"
elif percentage >= 90:
    status= "WARNING"
else:
    status= "OK"
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
print(status)
print("=" * 34)







# ================================================================== PROCESS
# 2. Work out the difference and the percentage.       [Typical and above]

difference = 0.0   # replace with your calculation
percent = 0.0       # replace with your calculation
# 3. Decide a status and store it in a variable called status.
#
#    Threshold : if / else        -> "OVER LIMIT" or "OK"
#    Typical   : if / elif / else -> "OVER LIMIT" (100% or more),
#                                     "WARNING" (90% or more), otherwise "OK"

status = ""   # replace with your if / else (or if / elif / else)


# =================================================================== OUTPUT
# 4. Print the report.
#
#    Threshold : the three values you were given, plus status, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : wrap sections 1-4 in a loop so you can check as many records
#                as you like in one run - type "quit" as the label to stop.
#                Keep count of how many came back OVER LIMIT and print that
#                once, after the loop ends.

print()


# your report lines go here




# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every variable name says what it holds
