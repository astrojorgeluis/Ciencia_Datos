# Bienvenidx al archivo de funciones definitivo de Jorge Luis

def promedio(datos):
    promedio = sum(datos) / len(datos)
    return promedio

def mediana(datos):
    datos.sort()
    n = len(datos)
    if n % 2 != 0:
        mediana = datos[n // 2]
    else:
        izquierdo = datos[n // 2 - 1]
        derecho = datos[n // 2]
        mediana = (izquierdo + derecho) / 2
    return mediana

def moda(datos):
    moda = None
    max_contador = 0

    for elemento in datos:
        contador = datos.count(elemento)
        if contador > max_contador:
            moda = elemento
            max_contador = contador

    return moda

def rango(datos):
    if len(datos) == 0:
        return None  # Si la lista está vacía, no hay rango.

    min_valor = min(datos)  # Encuentra el valor mínimo en la lista.
    max_valor = max(datos)  # Encuentra el valor máximo en la lista.

    rango = max_valor - min_valor  # Calcula la diferencia entre el máximo y el mínimo.

    return rango
    
def frec_absoluta(datos):
    frecuencia_absoluta = {}
    
    for elemento in datos:
        if elemento in frecuencia_absoluta:
            frecuencia_absoluta[elemento] += 1
        else:
            frecuencia_absoluta[elemento] = 1

    return frecuencia_absoluta

def varianza(datos):
    n = len(datos)
    if n < 2:
        return None  # No se puede calcular la varianza con menos de 2 datos.

    media = sum(datos) / n
    suma_de_cuadrados = sum((x - media) ** 2 for x in datos)
    varianza = suma_de_cuadrados / (n - 1)  # Usamos n - 1 para calcular la varianza muestral.

    return varianza

def desv_estandar(datos):
    n = len(datos)
    if n < 2:
        return None  # No se puede calcular la desviación estándar con menos de 2 datos.

    # 1. Calcular la media.
    media = sum(datos) / n

    # 2. Restar la media y elevar al cuadrado.
    sumatorio_cuadrados = sum((x - media) ** 2 for x in datos)

    # 3. Calcular la media de los valores al cuadrado.
    varianza = sumatorio_cuadrados / (n - 1)  # Usamos n - 1 para calcular la varianza muestral.

    # 4. Tomar la raíz cuadrada de la varianza para obtener la desviación estándar.
    desviacion_estandar = varianza ** 0.5

    return desviacion_estandar

def cuartiles(datos):
    datos.sort()
    n = len(datos)
    q1 = datos[n // 4]
    q2 = datos[n // 2]
    q3 = datos[(3 * n) // 4]
    
    return q1, q2, q3

def mediana_absoluta(datos):
    datos_absolutos = [abs(x) for x in datos]
    datos_absolutos.sort()
    n = len(datos_absolutos)
    mediana_absoluta = datos_absolutos[n // 2]
    
    return mediana_absoluta
