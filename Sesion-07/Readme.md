
## Sesión 07: Transformación, filtración y ordenamiento de datos

### 1. Objetivos

- Hacer casting de tipos de datos.
- Manipular strings usando el módulo `str`.
- Aplicar funciones custom a un `DataFrame`.
- Aplicar filtros a nuestros datos.
- Ordenar nuestro dataset por columnas.

### 2. Contenido

---

<ins>Introducción</ins>

Hoy aprenderemos algunas técnicas para realizar transformación y reestructuración de datos.

La transformación de datos consiste en convertir un dato en otro dato utilizando algún tipo de proceso transformativo.

La reestructuración de datos tiene que ver con ver tu conjunto de datos desde diferentes perspectivas.

La transformación es muy útil para limpiar nuestro dataset y para dejarlo preparado para futuros análisis estadísticos, mientras que la reestructuración nos ayuda a entender mejor nuestro conjunto de datos y extraer información valiosa que pueda ser luego analizada o visualizada.

---

<ins>Casting</ins>

El primer tipo de transformación que veremos es el `casting`. `Casting` significa convertir un dato de un tipo de dato a otro tipo de dato. O sea, convertir una `string` a un `int`, un `int` a un `float`, un `int` a un `datetime`, etc.

Muchas veces los conjuntos de datos con los que nos topamos no tienen el formato adecuado o están muy sucios. Esto ocasiona que `pandas` no sepa cómo interpretar el tipo de datos con los que se enfrenta.

Veremos algunas técnicas parar hacer `casting` manualmente en los casos en los que `pandas` se equivoque o no sepa cómo proceder.

>

[**`Ejemplo 1`**](Ejemplo-01/casting.ipynb)
[**`Reto 1`**](Reto-01/casting.ipynb)

---

<ins>Manipulación de `strings`</ins>

Manipular `strings` es todo un tema por sí mismo. Aprender a usar las herramientas de manipulación de `strings` es muy importante puesto que nos permite trabajar con datos no estructurados. Los datos no estructurados son básicamente secuencias de caracteres tipo texto.

Dado que en un texto las configuraciones, patrones y significados posibles son casi infinitos, necesitamos técnicas que nos ayuden a lidiar a mucho detalle con estos datos.

Para eso tenemos la propiedad `str` que estudiaremos a continuación.

>

[**`Ejemplo 2`**](Ejemplo-02/manipulacion_de_strings.ipynb)
[**`Reto 2`**](Reto-02/manipulacion_de_strings.ipynb)

---

<ins>`map`</ins>

Otra cosa que podemos hacer es usar un mapeo de un dato a otro. Esto significa que le damos a `pandas` algún objeto que contenga una correspondencia entre un dato y otro para que realice una conversión.

`map` nos permite pasarle tanto un `diccionario` como una `función` para realizar la conversión de un dato a otro.

Veámoslo en acción.

>

[**`Ejemplo 3`**](Ejemplo-03/map.ipynb)
[**`Reto 3`**](Reto-03/map.ipynb)

---

<ins>`apply`</ins>

Otra manera de crear correspondencias es aplicando una función a nuestro `DataFrame` o `Serie` usando `apply`.

Para una `Serie` podemos usar `apply` para aplicar una función "elemento por elemento".

En `DataFrames` podemos usar este mismo método para aplicar funciones por filas o por columnas.

>

[**`Ejemplo 4`**](Ejemplo-04/apply.ipynb)
[**`Reto 4`**](Reto-04/apply.ipynb)

---

<ins>Filtros</ins>

Los filtros nos sirven para obtener subconjuntos de datos que tengan una cierta característica que necesitamos. Podemos "filtrar" solamente los datos que deseamos y dejar fuera datos indeseables.

Crear subconjuntos a partir de nuestro conjunto de datos es muy útil para entender mejor la conformación de nuestro dataset y para realizar análisis de muestras del total de nuestros datos.

¡Ésta es una de las herramientas que vas a estar usando más a menudo!

>

[**`Ejemplo 5`**](Ejemplo-05/filtros.ipynb)
[**`Reto 5`**](Reto-05/filtros.ipynb)

---

<ins>`sort`</ins>

También podemos reordenar nuestros datos usando el método `sort_values`. Reordenamos nuestro conjunto de datos tomando en cuenta el valor que cada fila tenga en una columna dada. Podemos ordenarlos ascendente o descentemente.

Reordenar nuestros datos puede ayudarnos a entender mejor la distribución de nuestros datos, así como preparar nuestro conjunto o subconjuntos para ser visualizados.

>

[**`Ejemplo 6`**](Ejemplo-06/sort.ipynb)
[**`Reto 6`**](Reto-06/sort.ipynb)

---

### 3. Postwork

[**`Postwork Sesión 7`**](Postwork/Readme.md)
