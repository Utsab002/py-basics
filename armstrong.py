n = int(input("Enter a number: "))
s = str(n)
power = len(s)
total = sum(int(d) ** power for d in s)
if total == n:
    print("The number is an Armstrong number")
else:
    print("The number is not an Armstrong number")