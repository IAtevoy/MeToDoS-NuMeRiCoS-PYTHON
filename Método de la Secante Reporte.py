#Inciso a) usando el Método de la Secante

import matplotlib.pyplot as plt #Llibrería matplotlib para poder hacer gráficas
import math #Librería matemática para usar funciones exponenciales

def f(x): #Define la función f(x)
    return x**3 + 4*x**2 - 10 #Ecuación del inciso
x0=1 #Primer valor inicial x_(i-1)
x1=2 #Segundo valor inicial x_i
error_deseado=0.0001 # Tolerancia aceptada
error=100 #Se inicia con un error grande que sirve para arrancar el ciclo
iteracion=0 #Contador de iteraciones
valores_x=[] #Lista donde se guardarán los valores aproximados de la raíz en la grafica
valores_fx=[] #Lista donde se guardarán los valores de la función evaluada en x en la grafica
iteraciones=[] #Lista para guardar el número de iteración
errores=[] #Lista donde se guardará el error de cada iteración
#Crea la tabla de resultados
print(f"{'Iter':<5}{'x_(i-1)':<12}{'x_i':<12}{'f(x_i)':<15}{'x_(i+1)':<12}{'Er':<10}{'Er%':<10}")
print("-"*85) #Línea separadora para la tabla

while error>error_deseado: #El ciclo se ejecuta mientras el error sea mayor que el error permitido
    f0=f(x0) #(PASO 1) Evalúa la función en x_(i-1)
    f1=f(x1) #(PASO 1) Evalúa la función en x_i
    #Verificación (evitar división entre 0)
    if (f0-f1)==0: #SI el denominador es cero
        print("Error: división entre cero. No se puede continuar.")
        break #Detiene el programa
    x2=x1-f1*(x0-x1)/(f0-f1) #(PASO 2) Calcula el siguiente valor x_(i+1)
    er=abs((x2-x1)/x2) #Cálculo del ERROR RELATIVO
    erp=er*100 #(PASO 3) Cálculo del ERROR PORCENTUAL
    print(f"{iteracion:<5}{x0:<12.6f}{x1:<12.6f}{f1:<15.6f}{x2:<12.6f}{er:<10.6f}{erp:<10.6f}") #Datos de la tabla
    valores_x.append(x2) #Guarda el nuevo valor de x2 para después graficarlo
    valores_fx.append(f(x2)) #Guarda el valor de la nueva función para la gráfica
    iteraciones.append(iteracion) #Guarda el número de iteración
    errores.append(er) #Guarda el error relativo
    x0=x1 #El valor actual pasa a ser el anterior
    x1=x2 #El nuevo valor pasa a ser el actual
    error=er #Aumenta el contador de iteraciones
    iteracion+=1 #Aumenta el contador de iteraciones

plt.figure(figsize=(10,6)) #Crea una figura de tamaño 10x6 para la gráfica
plt.plot(iteraciones, errores, marker='o', linestyle='-', color='red', label='Er=|(x-x_anterior)/x|') #Configuración de la gráfica
plt.title(r'Inciso a) $f(x)=x^3+4x^2-10$ con Secante') #Título de la gráfica
plt.xlabel('Iteración') #Etiqueta eje X
plt.ylabel('Error relativo') #Etiqueta eje Y
plt.grid(True) #Activa la cuadrícula
plt.legend()  #Muestra la leyenda
plt.show()  #Muestra la gráfica
print("\nRaíz aproximada:", x1) #Imprime la raíz final