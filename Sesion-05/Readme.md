
## Sesión 05: Funciones vectorizadas y limpieza de datos

### 1. Objetivos

1. Identificar y utilizar las funciones vectorizadas.
2. Identificar agregaciones/reducciones.
3. Leer un CSV.
4. Encontrar y limpiar datos nulos.
5. Reindexar y cambiar el nombre de las columnas.

### 2. Contenido

---

<ins>Introducción</ins>

El día de hoy vamos a aprender a limpiar un poco nuestros datasets. Necesitamos limpiar nuestros datasets para facilitarnos los procesos posteriores de análisis y visualización. Trabajar con un dataset sucio es muy difícil y frustrante.

Vamos a aprender a encontrar valores nulos en nuestro dataset y limpiarlos.

Pero para poder hacer esto, primero vamos a aprender dos herramientas que se llaman `funciones vectorizadas` y `agregaciones` que expandirán tus posibilidades muchísimo.

---

<ins>Aritmética con `Series` y Funciones vectorizadas</ins>

`map` nos permite aplicar una función a una `lista` "elemento por elemento". Hay una manera todavía más fácil de aplicar este tipo de procesos a una `Serie` gracias a la aritmética con `Series` y a las funciones vectorizadas. Aplicar una transformación es tan fácil como esto:

<div style="padding: 10px; margin: 20px"><img src='./Imgs/sesion-5_5.png'></div>

Vamos a ver cómo es que funcionan.

>

[**`Ejemplo 1`**](Ejemplo-01/funciones_vectorizadas.ipynb)
[**`Reto 1`**](Reto-01/funciones_vectorizadas.ipynb)

---

<ins>Agregaciones</ins>

Las `agregaciones` son una variación de las funciones vectorizadas. Lo que hacen es tomar un arreglo (una `Serie`, por ejemplo), aplicar una operación a todos los elementos y regresar un resultado único que es la `agregación` o `reducción`  del arreglo. Una `agregación` se ve así:

<div style="padding: 10px; margin: 20px"><img src='./Imgs/sesion-5_10.png'></div>

Exploremos un poco.

>

[**`Ejemplo 2`**](Ejemplo-02/agregaciones.ipynb)
[**`Reto 2`**](Reto-02/agregaciones.ipynb)

---

<ins>Funciones vectorizadas y agregaciones con `DataFrames`</ins>

También podemos aplicar estas herramientas a `DataFrames` completos. Tanto las operaciones aritméticas, funciones vectorizadas y agregaciones funcionan con ligeras diferencias de procedimiento.

<div style="padding: 10px; margin: 20px"><img src='./Imgs/sesion-5_17.png'></div>

>

[**`Ejemplo 3`**](Ejemplo-03/vectorizacion_con_dataframes.ipynb)
[**`Reto 3`**](Reto-03/vectorizacion_con_dataframes.ipynb)

---

<ins>NaN o Valores Nulos</ins>

Como viste en tu Prework, los valores `NaN` (`Not a Number`) son bastante indeseables porque no podemos utilizarlos para realizar análisis estadístico u operaciones aritméticas. Es por eso que uno de los primeros pasos en la Limpieza de Datos suele ser la eliminación de estos valores.

Los `NaNs` se ven así en un `DataFrame`:

<div style="padding: 10px; margin: 20px"><img src='./Imgs/sesion-5_45.png'></div>

Vamos a ver primero cómo identificarlos.

>

[**`Ejemplo 4`**](Ejemplo-04/nan.ipynb)

---

<ins>Limpiando `NaNs`</ins>

Hay 3 operaciones básicas que podemos realizar para eliminar `NaNs` de nuestros datasets:

1. Eliminar filas con `NaNs`
2. Eliminar columnas con `NaNs`
3. Llenar los `NaNs` con algún valor.

Exploremos las 3 opciones.

>

[**`Ejemplo 5`**](Ejemplo-05/limpiando_nans.ipynb)
[**`Reto 4`**](Reto-04/limpiando_nans.ipynb)

---

<ins>Aplicando nuestros conocimientos a un dataset real</ins>

¡Vamos a ver un pequeño ejemplo donde vamos a aplicar lo que hemos visto el día de hoy a un dataset real!

Este dataset está en formato CSV, que quiere decir que cada columna está separada por una `coma`. Las líneas de nuestro archivo .csv son cada una las filas de nuestro dataset, y los datos en cada fila, separados por comas (`,`), conforman las columnas:

<div style="padding: 10px; margin: 20px"><img src='./Imgs/sesion-5_1.png'></div>

>

[**`Ejemplo 6`**](Ejemplo-06/aplicacion_real.ipynb)

---

<ins>Reindexando y renombrando columnas</ins>

Tenemos ahora un dataset que ha sido limpiado de `NaNs`. Tenemos ahora dos problemas. El primero es que nuestro índice no corresponde al número de filas que tenemos ahora:

<div style="padding: 10px; margin: 20px"><img src='./Imgs/sesion-5_40.png'></div>

El segundo es que los nombres de nuestras columna son muy inconsistentes (e incluso contienen errores ortográficos):

<div style="padding: 10px; margin: 20px"><img src='./Imgs/sesion-5_46.png'></div>

Para terminar esta sesión, vamos a arreglar esos problemas.

>

[**`Ejemplo 7`**](Ejemplo-07/reindexando_y_renombrando.ipynb)
[**`Reto 5`**](Reto-05/limpiando_un_dataset.ipynb)

---

### 3. Postwork

[**`Postwork Sesión 5`**](Postwork/Readme.md)
