
## Sesión 02: Estructuras de datos y funciones

### 1. Objetivos

1. Comprender la utilidad de las estructuras de datos para organizar información dentro de nuestros programas.
2. Utilizar listas y diccionarios y entender las principales diferencias entre ellos.
3. Declarar funciones y utilizarlas exitosamente.

### 2. Contenido

---

<ins>Listas</ins>

Como vimos en el Prework, las listas son uno de los tipos de estructuras de datos que podemos utilizar en Python. Una estructura de datos nos sirve para organizar datos y para optimizar el acceso, procesamiento y uso de éstos.

Las listas son secuencias ordenadas de datos y se ven así:

`lista_de_numeros = [1, 4, 7, 5, 3, 4, 6]`

Vayamos a un primer ejemplo para entender su funcionamiento.

> Lo más importante de esta sección es que los alumnos entiendan bien el `operador de indexación`, ya que es muy similar al que se usa en `numpy` y en `pandas`.

[**`Ejemplo 1`**](Ejemplo-01/listas.ipynb)
[**`Reto 1`**](Reto-01/listas.ipynb)

---

<ins>Modificando Listas</ins>

Tenemos 2 métodos básicos para modificar listas:

1. `append`: Agrega un elemento al final de la lista
2. `pop`: Elimina el último elemento de la lista o el elemento guardado en el índice que le pasemos

Veámoslos en acción.

> Aunque los métodos `append` y `pop` pocas veces son usados profesionalmente, es importante que los alumnos entiendan la noción de modificación de estructuras de datos, cómo se pueden agregar y eliminar elementos y los demás elementos se mantienen, aunque con diferente índice.

[**`Ejemplo 2`**](Ejemplo-02/modificando_listas.ipynb)
[**`Reto 2`**](Reto-02/modificando_listas.ipynb)

---

<ins>Creando y accesando diccionarios</ins>

Los diccionarios son nuestra segunda estructura de datos básica en Python. A diferencia de las listas, los diccionarios no tienen un orden definido. Esto no importa demasiado porque los diccionarios contienen pares llave-valor en vez de elementos (como en las listas). Para acceder a los valores basta con pasarle al diccionario la llave que estamos buscando. Piénsalo como pasarle un `url` a tu navegador para obtener una página web. En algún lado hay una estructura similar a un diccionario que relaciona cada `url` con la ip en donde está almacenada la página a la queremos acceder.

Veamos cómo crear y acceder diccionarios.

> Los diccionarios sobre todo me parecen valiosos por su similitud al formato JSON y porque son ideales para representar filas (muestras) en una tabla (el nombre de columna como llave y el valor de la celda como el valor de la llave). También es buena idea hablar sobre la idea del mappeo, cómo es que podemos crear pares de información que representan "lo mismo" pero visto desde diferentes perspectivas o a diferentes niveles de profundidad.

[**`Ejemplo 3`**](Ejemplo-03/diccionarios.ipynb)
[**`Reto 3`**](Reto-03/diccionarios.ipynb)

---

<ins>Modificando diccionarios</ins>

Tenemos 3 maneras básicas de modificar diccionarios:

1. Agregar datos: Esto se hace "llamando" la llave nueva que queremos agregar y asignándole un valor.
2. Modificar datos: Para modificar un dato en un diccionario, basta con reasignar un nuevo valor a una llave ya existente.
3. Borrar datos: Para borrar una llave en un diccionario, podemos usar el método `pop`.

Vayamos a un ejemplo para ver cómo es que funcionan.

>

[**`Ejemplo 4`**](Ejemplo-04/modificando_diccionarios.ipynb)
[**`Reto 4`**](Reto-04/modificando_diccionarios.ipynb)

---

<ins>Funciones</ins>

Repetir código es una de las peores prácticas que podemos tener como programadores y analistas: vuelve nuestro código confuso y difícil de modificar. Para eso existen las funciones, que nos permiten "encapsular" procesos para que puedan ser repetidos a través de todo nuestro programa.

Las funciones nos pueden ayudar a quitarle complejidad a nuestro programa y hacerlo más fácil de entender.

Así se ve una función:

```
def soy_una_funcion(soy_un_parametro):
    nueva_variable = soy_un_proceso
    
    return nueva_variable
```

Vamos a analizarlas paso a paso.

> Desde el principio dejamos en claro que las funciones tienen parámetros y returns. A veces suelen enseñarse funciones sin parámetros y returns pero a mí me parece una mala idea porque es enseñar malas prácticas desde el inicio. Una función sin parámetros a) siempre hace lo mismo, o b) utiliza variables que no le son pasadas como parámetros. Una función sin return a) no genera nada que pueda ser utilizado en otras partes del programa, o b) está modificando variables fuera de la función (está teniendo efectos secundarios). Ambos comportamientos son peligrosos. Este módulo fue diseñado para incitar a los alumnos a programar funcionalmente. Por lo tanto, preferimos siempre funciones puras y enseñamos los principios generales adecuados para intentar evitar los efectos secundarios (sigue habiendo mutabilidad, pero eso es un problema un poco más complejo que decidí no tocar por ahora).

[**`Ejemplo 5`**](Ejemplo-05/funciones.ipynb)
[**`Reto 5`**](Reto-05/funciones.ipynb)

---

### 3. Postwork

[**`Postwork Sesión 2`**](Postwork/Readme.md)
