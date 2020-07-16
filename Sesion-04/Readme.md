
## Sesión 04: Pandas y Análisis Exploratorio de Datos

### 1. Objetivos

1. Identificar las características básicas de las Series y DataFrames de Pandas.
2. Leer JSONs usando Pandas.
3. Utilizar herramientas básicas de exploración de datos.

### 2. Contenido

---

<ins>Series de Pandas</ins>

Las `Series` son una de las dos estructuras de datos que ofrece `pandas` que nos hacen la vida mucho más fácil como científicos de datos.

Las `Series` son una especie de híbrido entre `listas` y `diccionarios`.

<div style="padding: 10px; margin: 20px"><img src='./Imgs/sesion-4_7.png'></div>

Vamos a ver cómo funcionan.

> He elegido enseñar el operador `loc` desde el principio. Usar el `operador de indexación` sin `loc` o `iloc`, aunque pareciera mejor por su similitud a las `listas` se presta a muchas confusiones y puede acarrear muchos errores. Creo que es mejor acostumbrarse a ser específicos al respecto de si estamos pidiendo los índices por su nombre o por su posición.

[**`Ejemplo 2`**](Ejemplo-02/series.ipynb)
[**`Reto 1`**](Reto-01/series.ipynb)

---

<ins>Métodos avanzados de indexación</ins>

Podemos usar otros métodos de indexación en las `Series` que resultan súmamente útiles a la hora de explorar y procesar datos.

Podemos elegir, por ejemplo, rangos de datos usando una sintaxis como la siguiente:

`serie.loc[4:23]`

>

[**`Ejemplo 3`**](Ejemplo-03/indexacion_de_series.ipynb)
[**`Reto 2`**](Reto-02/indexacion_de_series.ipynb)

---

<ins>Dataframes</ins>

Los `DataFrames` son la segunda estructura de datos de `pandas` que vamos estar usando constantemente. Un `DataFrame` está hecho de dos o más `Series` acomodadas de manera que obtenemos una estructura tabular.

Los `DataFrames` son bidimensionales, tienen filas y columnas. Cada columna es una `Serie` que tiene un nombre. Los `DataFrames` nos ayudan a manejar datos en estructura tabular de manera muy eficiente.

<div style="padding: 10px; margin: 20px"><img src='./Imgs/sesion-4_23.png'></div>

Veamos cómo funcionan.

> 

[**`Ejemplo 4`**](Ejemplo-04/dataframes.ipynb)
[**`Reto 3`**](Reto-03/dataframes.ipynb)

---

<ins>Manipulación de columnas en un `DataFrame`</ins>

Podemos agregar, reasignar y eliminar columnas de nuestros `DataFrames`. La sintaxis es muy parecida a la que se usa con los `diccionarios`.

> 

[**`Ejemplo 5`**](Ejemplo-05/manipulacion_de_columnas.ipynb)
[**`Reto 4`**](Reto-04/manipulacion_de_columnas.ipynb)

---

<ins>Lectura de archivos JSON</ins>

Uno de los formatos más comunes en los que vamos a encontrar conjuntos de datos es el formato JSON. Como probablemente ya sabrás, el formato JSON se parece bastante al formato que tienen los `diccionarios` de Python:

```python
{
    "llave_1": "valor_1",
    "llave_2": "valor_2",
    "llave_3": "valor_3",
    "llave_4": "valor_4"
}
```

Vamos a aprender a leer archivos JSON y a convertirlos en `DataFrames`.

> Lectura de CSVs y adquisición de datos por medio de APIs y Bases de Datos se estudian más adelante en el módulo.

[**`Ejemplo 6`**](Ejemplo-06/lectura_de_json.ipynb)

---

<ins>Análisis Exploratorio de Datos</ins>

El Ánalisis Exploratorio de Datos es el proceso a través del cual exploramos un nuevo conjunto de datos para conocer su contenido a profundidad. Este paso es extremadamente importante, puesto que nos ayuda a saber cómo limpiar y reestructurar nuestro conjunto de datos de manera que podamos realizar un mejor análisis y visualización de los datos.

Vamos a ver algunas herramientas básicas que tienen los `DataFrames` para explorar un conjunto de datos.

> Por ahora estamos haciendo una exploración muy básica. Lo que importa es que el alumno entienda los principios básicos de cómo crear `DataFrames` a partir de conjuntos de datos existentes. En la sesión que sigue se verá Análisis Exploratorio a más profundidad.

[**`Ejemplo 7`**](Ejemplo-07/aed.ipynb)
[**`Reto 5`**](Reto-05/aed.ipynb)

---

### 3. Postwork

[**`Postwork Sesión 4`**](Postwork/Readme.md)
