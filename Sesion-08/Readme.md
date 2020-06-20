
## Sesión 08: Bases de datos, merge y agrupaciones

### 1. Objetivos

- Conectarse a una base de datos MySQL usando Python.
- Obtener datos de un SGBD y convertir esos datos a `DataFrames`.
- Unir `DataFrames` usando el método `merge`.
- Segmentar nuestros `DataFrames` usando `groupby`.
- Aplicar agregaciones y funciones a nuestros grupos.

### 2. Contenido

---

<ins>Introducción</ins>

Bienvenido a la última sesión de este módulo. El día de hoy cerraremos con 3 temas que son esenciales para redondear tu educación como procesador de datos:

1. Bases de datos, cómo conectarnos a ellas y cómo obtener información de ellas
2. `merge` y cómo unir `DataFrames` al estilo de un `join` de SQL
3. `groupby` y cómo segmentar tus `DataFrames` por grupo para aplicar funciones agregadoras a cada grupo

¡A por ella!

---

<ins>Bases de Datos</ins>

Como vimos en el Prework, los sistemas de gestión de bases de datos (como MySQL, PostgreSQL, MariaDB, MongoDB, etc) son una gran manera de almacenar grandes (o pequeñas) cantidades de datos y compartirlas con muchas personas.

Normalmente, estas bases de datos van a estar almacenadas en algún servidor al que todos los integrantes de tu equipo van a tener acceso. Vamos a conectarnos a una base de datos remota usando la librería `mysql-connector`.

Antes que nada, si no lo has hecho ya, instala la librería desde Google Colab:

`!pip install mysql-connector-python`

>

[**`Ejemplo 1`**](Ejemplo-01/conectandose.ipynb)
[**`Reto 1`**](Reto-01/conectandose.ipynb)

---

<ins>Tablas a `DataFrames`</ins>

Ya que hemos realizado nuestra conexión, vamos a hacer unas consultas a nuestra base de datos para construir algunos `DataFrames` a partir de las tablas que existen en la base `movielens`.

Podríamos hacer consultas filtradas a la base de datos cada vez que necesitáramos un subconjunto específico, pero resulta mucho más fácil (sobre todo en este caso en el que nuestro conjunto de datos es pequeño), pedir todos los datos y luego filtrarlos usando `pandas`.

Aunque ésta no es una solución apta para **todos** los casos (en el mundo de la ingeniería de software y la ciencia de datos en realidad rara vez sucede eso), es la que usaremos en esta sesión.

>

[**`Ejemplo 2`**](Ejemplo-02/tablas_a_dataframes.ipynb)
[**`Reto 2`**](Reto-02/tablas_a_dataframes.ipynb)

---

<ins>`merge`</ins>

Ok, ahora tenemos una base de datos que consiste de 5 tablas distintas. Dentro de cada una de esas tablas, tenemos información relevante que se relaciona con otras tablas a través de lo que llamamos 'llaves foráneas' ('foreign keys'). Esto quiere decir que si en una tabla tenemos una columna `user_id` y en otra tabla también tenemos la columna `user_id`, podemos usar ambas columnas para relacionar ambas tablas y construir una nueva tabla que contenga la información de las dos tablas originales.

Usando este proceso, podemos unir `DataFrames` y completar información relevante que le falte a una de las tablas pero que podamos encontrar en otra tabla.

>

[**`Ejemplo 3`**](Ejemplo-03/merge.ipynb)
[**`Reto 3`**](Reto-03/merge.ipynb)

---

<ins>`groupby`</ins>

Ya sabemos unir `DataFrames` usando `concat` y `merge`, pero ¿qué pasa cuando lo que queremos es segmentar nuestro `DataFrame`? A veces en vez de unir todos los datos en la misma estructura lo que queremos es dividirlos para facilitar su comprensión, análisis y visualización.

Para esto podemos utilizar el método `groupby`, que nos permite agrupar nuestros datos por categorías y luego aplicar funciones agregadoras a cada grupo.

>

[**`Ejemplo 4`**](Ejemplo-04/groupby.ipynb)

---

Ahora sí viene lo bueno. Los siguientes 3 Retos serán exploraciones mucho más profundas de todo lo que hemos visto el día de hoy y en sesiones anteriores. Si los encuentras muy difíciles, recuerda que siempre puedes compartir tus dudas con tus compañeros y con la experta. ¡Mucha suerte!

[**`Reto 4`**](Reto-04/las_mejores_50.ipynb)
[**`Reto 5`**](Reto-05/ratings_de_mas_valoradas.ipynb)
[**`Reto 6`**](Reto-06/lo_que_los_cientificos_aman.ipynb)

---

### 3. Postwork

[**`Postwork Sesión 8`**](Postwork/Readme.md)
