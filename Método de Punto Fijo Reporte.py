#Inciso a) usando el Método de Punto Fijo

import matplotlib.pyplot as plt #Llibrería matplotlib para poder hacer gráficas
import math #Librería matemática para usar funciones exponenciales

def g(x): #Define la trabsformada g(x)
    return math.sqrt(10/(x+4)) #Transformada del inciso
x0=1 #Primer valor inicial x_(i-1)
error_deseado=0.0001 # Tolerancia aceptada
error=100 #Se inicia con un error grande que sirve para arrancar el ciclo
iteracion=0 #Contador de iteraciones
valores_x=[] #Lista donde se guardarán los valores aproximados de la raíz en la grafica
valores_fx=[] #Lista donde se guardarán los valores de la función evaluada en x en la grafica
iteraciones=[] #Lista para guardar el número de iteración
errores=[] #Lista donde se guardará el error de cada iteración
#Crea la tabla de resultados
print(f"{'Iter':<5}{'x_i':<12}{'x_(i+1)':<12}{'Er':<10}{'Er%':<10}")
print("-"*67) #Línea separadora para la tabla

while error>error_deseado: #El ciclo se ejecuta mientras el error sea mayor que el error permitido
    x1=g(x0) #(PASO INICIAL) calcular x_(i+1)
    if iteracion==0: #SI la iteración es igual a 0
        er=1 #El error es 1=100% ya que es el error maximo que se tiene al iniciar el ciclo
    else:
        er=abs((x1-x0)/x1) #(PASO 2) Cálculo del ERROR RELATIVO
    erp=er*100 #Cálculo del ERROR PORCENTUAL
    print(f"{iteracion:<5}{x0:<12.6f}{x1:<12.6f}{er:<10.6f}{erp:<10.6f}") #Datos de la tabla
    valores_x.append(x1) #Guarda el nuevo valor de x1 para después graficarlo
    valores_fx.append(x1) #Guarda el valor de la nueva función para la gráfica
    iteraciones.append(iteracion) #Guarda el número de iteración
    errores.append(er) #Guarda el error relativo
    x0=x1 #El valor actual pasa a ser el anterior
    error=er #Aumenta el contador de iteraciones
    iteracion+=1 #Aumenta el contador de iteraciones

plt.figure(figsize=(10,6)) #Crea una figura de tamaño 10x6 para la gráfica
plt.plot(iteraciones, errores, marker='o', linestyle='-', color='red', label='Er=|(x-x_anterior)/x|') #Configuración de la gráfica
plt.title(r'Inciso a) $f(x)=x^3+4x^2-10$ con Punto Fijo') #Título de la gráfica
plt.xlabel('Iteración') #Etiqueta eje X
plt.ylabel('Error relativo') #Etiqueta eje Y
plt.grid(True) #Activa la cuadrícula
plt.legend()  #Muestra la leyenda
plt.show()  #Muestra la gráfica
print("\nRaíz aproximada:", x0) #Imprime la raíz final