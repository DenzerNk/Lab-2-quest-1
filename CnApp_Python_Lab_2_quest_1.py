from mod1 import amoeba

def expression(alpha):
    z = ((2) ** 0.5 / 2) * ((alpha / 2) - (alpha / 2)**3/6) - alpha / 2
    return z

alpha = float(input("Введіть значення α (в радіанах): "))
print("Значення виразу z = ", expression(alpha))

n = int(input("Введіть кількість годин n: "))
print("Кількість амеб через", n, "годин = ", amoeba(n))
