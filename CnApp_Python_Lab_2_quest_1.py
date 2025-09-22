import math
from mod import amoeba

def expression(alpha):
    z = (math.sqrt(2) / 2) * math.sin(alpha / 2) - alpha / 2
    return z

alpha = float(input("Введіть значення α (в радіанах): "))
print("Значення виразу z = ", expression(alpha))

n = int(input("Введіть кількість годин n: "))
print("Кількість амеб через", n, "годин = ", amoeba(n))
