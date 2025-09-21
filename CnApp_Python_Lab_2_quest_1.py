import math

def expression(alpha):
    z = (math.sqrt(2) / 2) * math.sin(alpha / 2)
    return z

def amoeba(n):
    k = n // 3
    return 2 ** k

alpha = float(input("Enter a =: "))
print("Result z = ", expression(alpha))

n = int(input("Enter the number hours n: "))

while n < 0:
    n = int(input("Number hours negative, enter n again: "))

print("Result amoeba", n, "hours =", amoeba(n))