#Escribir un programa dentro de exercise_math.py que dado dos números enteros imprima en pantalla el resultado 
#de las siguientes operaciones: la suma, la diferencia, el producto, el promedio, el cociente entero y el resto 
#de la división entera y el valor real de la división. Para entregar correctamente se deberá imprimir dichos 
#resultados en el orden que fueron pedidos en la consigna. Por ejemplo, primero la suma, despues la diferencia,
# y asi sucesivamente.

#Ejemplo: Para a = 57 y b = 7 el output debera ser:

#64
#50
#399
#32.0
#8
#1
#8.142857142857142

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

#print(f"La suma entre {num1} y {num2} es : {num1 + num2}")
#print(f"La diferencia entre {num1} y {num2} es : {num1 - num2}")
#print(f"El producto entre {num1} y {num2} es : {num1 * num2}")
#print(f"El promedio entre {num1} y {num2} es : {(num1 + num2) / 2}")
#print(f"El cociente entero entre {num1} y {num2} es : {round(num1 / num2)}")
#print(f"El resto de la division entera entre {num1} y {num2} es : {num1 % num2}")
#print(f"La division entre {num1} y {num2} es : {num1 / num2}")

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print((num1 + num2) / 2)
print(round(num1 / num2))
print(num1 % num2)
print(num1 / num2)
