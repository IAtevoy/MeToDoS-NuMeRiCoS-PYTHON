#Inciso a) usando el Método de Newton-Raphson

import matplotlib.pyplot as plt #Llibrería matplotlib para poder hacer gráficas
import math #Librería matemática para usar funciones exponenciales

def f(x): #Define la función f(x)
    return x**3 + 4*x**2 - 10 #Ecuación del inciso
def df(x): #Define la derivada de la función
    return 3*x**2 + 8*x #Derivada del inciso
x=1 #Valor inicial x0 donde inicia el método
error_deseado=0.0001 # Tolerancia aceptada
error=100 #Se inicia con un error grande que sirve para arrancar el ciclo
iteracion=0 #Contador de iteraciones
valores_x=[] #Lista donde se guardarán los valores aproximados de la raíz en la grafica
valores_fx=[] #Lista donde se guardarán los valores de la función evaluada en x en la grafica
iteraciones=[] #Lista para guardar el número de iteración
errores=[] #Lista donde se guardará el error de cada iteración
#Crea la tabla de resultados
print(f"{'Iter':<5}{'x_i':<12}{'f(x_i)':<15}{'f\'(x_i)':<15}{'x_i+1':<12}{'Er':<10}{'Er%':<10}")
print("-"*85) #Línea separadora para la tabla

while error>error_deseado: #El ciclo se ejecuta mientras el error sea mayor que el error permitido
    fx=f(x) #(PASO 1) Evalúa la función en el valor actual x_i
    dfx=df(x) #(PASO 1) Evalúa la derivada en el valor actual x_i
    if dfx==0: #Si la derivada es cero
        print("Error: derivada cero.")
        break
    x_nuevo=x-(fx/dfx) #(PASO 2) Calcula el siguiente valor aproximado x_(i+1)
    er=abs((x_nuevo-x)/x_nuevo) #(PASO 3) Cálculo del ERROR RELATIVO
    erp=er*100 #Cálculo del ERROR PORCENTUAL
    print(f"{iteracion:<5}{x:<12.6f}{fx:<15.6f}{dfx:<15.6f}{x_nuevo:<12.6f}{er:<10.6f}{erp:<10.6f}") #Datos de la tabla
    valores_x.append(x) #Guarda el valor de x para después graficarlo
    valores_fx.append(fx) #Guarda el valor de f(x) para la gráfica
    iteraciones.append(iteracion) #Guarda el número de iteración
    errores.append(er) #Guarda el error relativo
    x=x_nuevo #El nuevo valor pasa a ser el actual para la siguiente iteración
    error=er #Aumenta el contador de iteraciones
    iteracion+=1 #Aumenta el contador de iteraciones

plt.figure(figsize=(10,6)) #Crea una figura de tamaño 10x6 para la gráfica
plt.plot(iteraciones, errores, marker='o', linestyle='-', color='red', label='Er=|(x-x_anterior)/x|') #Configuración de la gráfica
plt.title(r'Inciso a) $f(x)=x^3+4x^2-10$ con Newton-Raphson') #Título de la gráfica
plt.xlabel('Iteración') #Etiqueta eje X
plt.ylabel('Error relativo') #Etiqueta eje Y
plt.grid(True) #Activa la cuadrícula
plt.legend()  #Muestra la leyenda
plt.show()  #Muestra la gráfica
print("\nRaíz aproximada:", x) #Imprime la raíz final