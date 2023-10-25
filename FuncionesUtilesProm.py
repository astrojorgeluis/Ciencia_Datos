# Bienvenidx al archivo de funciones definitivo de Jorge Luis

def promedio(datos):
    """
    Calcula el promedio de una lista de datos.

    Parámetros
    ----------
    datos : list
        Lista de números.

    Retorna
    ----------
    float
        El promedio de los datos.
    """
    promedio = sum(datos) / len(datos)
    return promedio

def mediana(datos):
    """
    Calcula la mediana de una lista de datos.

    Parámetros
    ----------
    datos : list
        Lista de números.

    Retorna
    ----------
    float
        La mediana de los datos.
    """
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
    """
    Calcula la moda de una lista de datos.

    Parámetros
    ----------
    datos : list
        Lista de números.

    Retorna
    ----------
    int or float
        La moda de los datos.
    """
    moda = None
    max_contador = 0

    for elemento in datos:
        contador = datos.count(elemento)
        if contador > max_contador:
            moda = elemento
            max_contador = contador

    return moda

def rango(datos):
   """
   Calcula el rango de una lista de datos.

   Parámetros
   ----------
   datos : list
       Lista de números.

   Retorna
   ----------
   int or float or None
       El rango de los datos. Si la lista está vacía, retorna None.
   """
   if len(datos) == 0:
       return None  # Si la lista está vacía, no hay rango.

   min_valor = min(datos)  # Encuentra el valor mínimo en la lista.
   max_valor = max(datos)  # Encuentra el valor máximo en la lista.

   rango = max_valor - min_valor  # Calcula la diferencia entre el máximo y el mínimo.

   return rango

def frec_absoluta(datos):
   """
   Calcula la frecuencia absoluta de una lista de datos.

   Parámetros
   ----------
   datos : list
       Lista de números.

   Retorna
   ----------
   dict
       Un diccionario con los elementos como claves y su frecuencia como valores.
   """
   frecuencia_absoluta = {}

   for elemento in datos:
       if elemento in frecuencia_absoluta:
           frecuencia_absoluta[elemento] += 1
       else:
           frecuencia_absoluta[elemento] = 1

   return frecuencia_absoluta

def varianza(datos):
    """
    Calcula la varianza muestral de una lista de datos.

    Parámetros
    ----------
    datos : list
        Lista de números.

    Retorna
    ----------
    float or None
        La varianza muestral de los datos. Si hay menos de dos elementos, retorna None.
    """
    n = len(datos)
    if n < 2:
        return None  # No se puede calcular la varianza con menos de 2 datos.

    media = sum(datos) / n
    suma_de_cuadrados = sum((x - media) ** 2 for x in datos)
    varianza = suma_de_cuadrados / (n - 1)  # Usamos n - 1 para calcular la varianza muestral.

    return varianza

def desv_estandar(datos):
    """
    Calcula la desviación estándar de una lista de datos.

    Parámetros
    ----------
    datos : list
        Lista de números.

    Retorna
    ----------
    float or None
        La desviación estándar de los datos. Si hay menos de dos elementos, retorna None.
    """
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
   """
   Calcula los cuartiles de una lista de datos.

   Parámetros
   ----------
   datos : list
       Lista de números.

   Retorna
   ----------
   tuple
       Un tuple con los tres cuartiles (Q1, Q2, Q3).
   """
   datos.sort()
   n = len(datos)
   q1 = datos[n // 4]
   q2 = datos[n // 2]
   q3 = datos[(3 * n) // 4]

   return q1, q2, q3

def mediana_absoluta(datos):
   """
   Calcula la mediana absoluta de una lista de datos.

   Parámetros
   ----------
   datos : list
       Lista de números.

   Retorna
   ----------
   float or int
       La mediana absoluta de los datos.
   """
   datos_absolutos = [abs(x) for x in datos]
   datos_absolutos.sort()
   n = len(datos_absolutos)
   mediana_absoluta = datos_absolutos[n // 2]

   return mediana_absoluta

