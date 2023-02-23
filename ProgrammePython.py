# Ex 8:
# 1)
for i in range(11):
    print("4 x", i, "=", 4*i)
print("-----------")
# 2)
for i in range(3, 9):
    print("4 x", i, "=", 4*i)
print("-----------")
# 3)
def TableMultiplication(n):
    for i in range(11):
        print(n, "x", i, "=", n*i)
# L'intérêt d'écrire une telle fonction est de pouvoir afficher tout les multiples d'un nombre entre 0 et 10
# Ex 9:
# 1)
def f(x):
    return x**2
# 2)
def f(x):
    return x**2
for x in range(-3, 4):
    print("f(", x, ") =", f(x))
print("-----------")
# 3)
def f(x):
    return x**2
for x in range(-2, 4, 2):
    print("f(", x, ") =", f(x))