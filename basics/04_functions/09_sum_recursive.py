# Write a recursive function to calculate the sum of first n natural numbers.

def sum_natural(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n + sum_natural(n - 1)

number = int(input("Enter the Number to check its sum of first 'n' natural numbers : "))
result = sum_natural(number)
print(result)
