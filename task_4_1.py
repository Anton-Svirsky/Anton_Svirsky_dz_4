# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

float_number = float(input("Введите число: "))
n = int(input("Введите точность (количество знаков после запятой): "))
print(round(float_number, n))