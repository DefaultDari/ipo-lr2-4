import math;
x = int(input("Введите значение x: "));
y = int(input("Введите значение y: "));
u = (((8 + abs(x-y)**2 + 1 )**(1/3)) / (x**2 + y**2 + 2)) - math.e**abs(x-y);
print("Результат: ", u);
