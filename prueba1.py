import math
2
3# Definir el valor de pi en 6 decimales
4PI = math.pi * 1000000 / 1000000
5
6# Definir los radios
7radios = [3, 8, 10]
8
9# Calcular la circunferencia de cada radio
10circunferencias = [2 * PI * radio for radio in radios]
11
12# Mostrar los resultados en la consola a través de un print en español
13print("Los radios y sus respectivas circunferencias son:")
14for i in range(len(radios)):
15    print(f"Radio {radios[i]}: {circunferencias[i]:.2f} cm")
