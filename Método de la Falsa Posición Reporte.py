#Inciso a) usando el Método de Falsa Posición

import matplotlib.pyplot as plt #Llibrería matplotlib para poder hacer gráficas
import math #Librería matemática para usar funciones exponenciales

def f(x): #Define la función f(x)
    return x**3 + 4*x**2 - 10 #Ecuación del inciso
a=1 #Límite inferior del intervalo
b=2 #Límite superior del intervalo
error_deseado=0.0001 # Tolerancia aceptada
error=100 #Se inicia con un error grande que sirve para arrancar el ciclo
iteracion=0 #Contador de iteraciones
xr_anterior=0 #Guarda el valor anterior de la aproximación de la raíz
valores_x=[] #Lista donde se guardarán los valores aproximados de la raíz en la grafica
valores_fx=[] #Lista donde se guardarán los valores de la función evaluada en x en la grafica
iteraciones=[] #Lista para guardar el número de iteración
errores=[] #Lista donde se guardará el error de cada iteración
if f(a)*f(b)>=0: #(PASO 1/INICIAL) Verificar si la condición es correcta
    print("El método de falsa posición no se puede aplicar en este intervalo.")
    print("f(a)*f(b) debe ser menor que 0.")
else: #Crea la tabla de resultados
    print(f"{'Iter':<5}{'a':<10}{'b':<10}{'xr':<10}{'f(xr)':<15}{'Er':<10}{'Er%':<10}")
    print("-"*73) #Línea separadora para la tabla
    
    while error>error_deseado: #El ciclo se ejecuta mientras el error sea mayor que el error permitido
        xr=a-(f(a)*(b-a))/(f(b)-f(a)) #(PASO 2) Calcula la aproximación de la raíz
        fxr=f(xr) #(PASO 3) Evalúa la función en xr
        if iteracion==0: #SI la iteración es igual a 0
            er=1 #El error es 1=100% ya que es el error maximo que se tiene al iniciar el ciclo
        else:
            er=abs((xr-xr_anterior)/xr) #Cálculo del ERROR RELATIVO
        erp=er*100 #Cálculo del ERROR PORCENTUAL
        print(f"{iteracion:<5}{a:<10.4f}{b:<10.4f}{xr:<10.4f}{fxr:<15.6f}{er:<10.6f}{erp:<10.6f}") #Datos de la tabla
        valores_x.append(xr) #Guarda el valor de xr para después graficarlo
        valores_fx.append(fxr) #Guarda el valor de f(xr) para la gráfica
        iteraciones.append(iteracion) #Guarda el número de iteración
        errores.append(er) #Guarda el error relativo
        if f(a)*fxr<0: #(CONDICIÓN 1) La raíz está entre a y xr
            b=xr #Entonces el nuevo límite superior es xr
        elif f(a)*fxr>0: #(CONDICIÓN 2) La raíz está entre xr y b
            a=xr #Entonces el nuevo límite inferior es xr
        else:
            break #(CONDICIÓN 3) Si f(xr)=0 se encontró la raíz exacta
        xr_anterior=xr #Guarda el xr actual para la siguiente iteración
        error=er #El error relativo es igual al error actual
        iteracion+=1 #Aumenta el contador de iteraciones

    plt.figure(figsize=(10,6)) #Crea una figura de tamaño 10x6 para la gráfica
    plt.plot(iteraciones, errores, marker='o', linestyle='-', color='red', label='Er=|(x-x_anterior)/x|') #Configuración de la gráfica
    plt.title(r'Inciso a) $f(x)=x^3+4x^2-10$ con Falsa Posición') #Título de la gráfica
    plt.xlabel('Iteración') #Etiqueta eje X
    plt.ylabel('Error relativo') #Etiqueta eje Y
    plt.grid(True) #Activa la cuadrícula
    plt.legend()  #Muestra la leyenda
    plt.show()  #Muestra la gráfica
    print("\nRaíz aproximada:", xr) #Imprime la raíz final