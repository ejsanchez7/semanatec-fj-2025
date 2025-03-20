def promedio(numeros):
    suma = 0
    for num in numeros:
	suma += num
    return suma / len(numeros)

print(promedio([1, 2, 3]))
