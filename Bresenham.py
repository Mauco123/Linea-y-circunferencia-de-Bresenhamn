#Hay que importar la libreria para graficar en python
import matplotlib.pyplot as plt

#Esta funcion se va a encontrar de graficar los puntos
def graficar(titulo, puntos):
    #Con esto se extrae todas las coordenada 'x' y las coordenadas 'y'
    #y las guarda en listas separadas
    x = [p[0] for p in puntos]
    y = [p[1] for p in puntos]

    plt.plot(x, y, 'bs')  # 'bs' dibuja los cuadros azules
    plt.grid(True)  # Activa la cuadricula que aparece en el fondo
    plt.title(titulo) #Muestra el titulo en la pantalla
    plt.axis('equal')  # Hace que la pantalla tenga la escala correcta
    plt.show() #Renderizar la imagen donde se mostrara la grafica


#Funcion  para graficar las lineas

def bresenham_linea(x1, y1, x2, y2):
    print(f"\n--- LÍNEA ({x1},{y1}) a ({x2},{y2}) ---")
    #Distancias absolutas sin signo entre los puntos iniciales y finales
    dx, dy = abs(x2 - x1), abs(y2 - y1)
    #Determinan la dirección de dibujo, con esto se hacen las reglas
    #1 si avanza hacia la derecha y arriba
    #-1 si retocede
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    #steep revisa si la línea crece más en Y que en X en un ángulo mayor a 45°
    #si si es mayor se intercambia dx y dy temporalmente para que el algoritmo
    #siempre avance sobre el eje dominante
    steep = dy > dx
    if steep:
        dx, dy = dy, dx
    #parametro de decision inicial P0 = 2△y - △x)
    pk = 2 * dy - dx
    #aqui se toma el valor del punto de inicio
    x, y = x1, y1
    #aqui se guardan los pixeles
    puntos = [(x, y)]
    #Este ciclo se repite dependeiendo de los pixes dominantes que haya en el eje dominante (dx)
    for _ in range(dx):
        #guardar el pk antes de modificarlo
        curr_pk = pk
        #si el pl < 0 la inea ideal esta cerca, por lo que no se avanza en
        #el eje secundario
        if pk < 0:
            pk += 2 * dy #actualizar el pk

            if steep:
                y += sy
            else:
                x += sx
        else:
            pk += 2 * (dy - dx)
            x += sx
            y += sy
        print(f"Pk: {curr_pk:>4}  ->  (x, y): ({x}, {y})")
        puntos.append((x, y))
    graficar(f"Línea ({x1},{y1}) a ({x2},{y2})", puntos)

def bresenham_circulo(r):
    print(f"\n--- CÍRCULO r={r} ---")
    x, y, pk = 0, r, 1 - r
    puntos = []
    k = 0
    while x < y:
        curr_pk = pk
        x += 1
        if pk < 0:
            pk += (2 * x) + 1
        else:
            y -= 1
            pk += (2 * x) + 1 - (2 * y)
        print(f"k: {k:>2} | Pk: {curr_pk:>4} | ({x}, {y}) | 2xk: {2 * x:>2} | 2yk: {2 * y:>2}")
        # Agregar los 8 puntos simétricos o en "espejo"
        simetricos = [(x, y), (-x, y), (x, -y), (-x, -y), (y, x), (-y, x), (y, -x), (-y, -x)]
        puntos.extend(simetricos)
        k += 1
    graficar(f"Círculo r={r}", puntos)



#Ejemplo de ejecucion

#bresenham_linea(10, 12, 35, 26)  # Ejercicio 1
# bresenham_linea(17, 21, 35, 42)  # Ejercicio 2
# bresenham_linea(2, 5, 7, 18)     # Ejercicio 3
# bresenham_linea(20, 10, 32, 18)  # Ejercicio 4
bresenham_circulo(20)  # Ejercicio Círculo
