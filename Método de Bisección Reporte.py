#Inciso a) usando el Método de Bisección

import matplotlib.pyplot as plt #Llibrería matplotlib para poder hacer gráficas
import math #Librería matemática para usar funciones exponenciales

def f(x): #Define la función f(x)
    return x**3 + 4*x**2 - 10 #Ecuación del inciso
a=1 #Límite inferior del intervalo
b=2 #Límite superior del intervalo
error_deseado=0.0001 # Tolerancia aceptada
error=abs(a-b) #Calcula el error absoluto del intervalo |a-b|
iteracion=0 #Contador de iteraciones
valores_x=[] #Lista donde se guardarán los valores aproximados de la raíz en la grafica
valores_fx=[] #Lista donde se guardarán los valores de la función evaluada en x en la grafica
iteraciones=[] #Lista para guardar el número de iteración
errores=[] #Lista donde se guardará el error de cada iteración
x_anterior=0 #Guarda el valor anterior de la aproximación de la raíz
if f(a)*f(b)>=0: #(PASO INICIAL) Verificar si la condición es correcta
    print("El método de bisección no se puede aplicar en este intervalo.")
    print("f(a)*f(b) debe ser menor o igual que 0.")
else: #Crea la tabla de resultados
    print(f"{'Iter':<5}{'a':<10}{'b':<10}{'x':<10}{'f(x)':<15}{'Er':<10}{'Er%':<10}")
    print("-"*70) #Línea separadora para la tabla

    while error>error_deseado: #El ciclo se ejecuta mientras el error sea mayor que el error permitido
        x=(b+a)/2 #(PASO 1) Calcula el punto medio del intervalo
        fx=f(x) #Evalúa la función en el punto medio
        if iteracion==0: #SI la iteración es igual a 0
            er=0 #El error es 0, no hay iteraciones
        else:
            er=abs((x-x_anterior)/x) #Cálculo del ERROR RELATIVO
        erp=er*100 #Cálculo del ERROR PORCENTUAL
        print(f"{iteracion:<5}{a:<10.4f}{b:<10.4f}{x:<10.4f}{fx:<15.6f}{er:<10.6f}{erp:<10.6f}") #Datos de la tabla
        valores_x.append(x) #Guarda el valor de x para después graficarlo
        valores_fx.append(fx) #Guarda el valor de f(x) para la gráfica
        iteraciones.append(iteracion) #Guarda el número de iteración
        errores.append(er) #Guarda el error relativo
        if f(a)*fx<0: #(PASO 2) SI el signo cambia entre f(a) y f(x)
            b=x #(PASO 3) La raíz está entre a y x, entonces el nuevo límite superior es x
        else: #(PASO 2) Si NO hay cambio de signo entre f(a) y f(x)
            a=x #La raíz está entre x y b, entonces el nuevo límite inferior es x
        error=abs(a-b) #(PASO 4) Calcula el nuevo error usando el tamaño del intervalo
        x_anterior=x #El valor de la x anterior, es el nuevo x calculado
        iteracion+=1 #Aumenta el contador de iteraciones

    plt.figure(figsize=(10,6)) #Crea una figura de tamaño 10x6 para la gráfica
    plt.plot(iteraciones, errores, marker='o', linestyle='-', color='red', label='Er=|(x-x_anterior)/x|') #Configuración de la gráfica
    plt.title(r'Inciso a) $f(x)=x^3+4x^2-10$ con Bisección') #Título de la gráfica
    plt.xlabel('Iteración') #Etiqueta eje X
    plt.ylabel('Error relativo') #Etiqueta eje Y
    plt.grid(True) #Activa la cuadrícula
    plt.legend()  #Muestra la leyenda
    plt.show()  #Muestra la gráfica
    print("\nRaíz aproximada:", x) #Imprime la raíz final