# Алгоритм вычисления значения функции F(n),
# где n – натуральное число,
# задан следующими соотношениями:
# F(1) = 1
# F(2) = 3
# F(n) = F(n–1) * n + F(n–2) * (n – 1) , при n >2
# Чему равно значение функции F(5)?

def F(n):
    if n == 1:
        return 1
    if n == 2:
        return 3
    if n > 2:
       return F(n-1) * n + F(n-2) * (n - 1)

print(F(5))