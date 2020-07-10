
## Sesión 01: Fundamentos de Python

### 1. Objetivos

1. Asignar variables, operadores matemáticos y tipos de datos.
2. Realizar interpolación de Strings.
3. Realizar comparaciones y estructuras de control de flujo.

### 2. Contenido

<ins>Revisión de Software</ins>

Asegurarse de que todos los alumnos hayan realizado con éxito la conexión entre Google Drive, Github y Google Colab. 

Es necesario saber leer archivos .ipynb en Colab desde el repositorio del módulo.

También es necesario haber creado el Acceso Directo a los Datasets desde el Drive del alumno para poder acceder a los conjuntos de datos desde Colab.

> Todas las instrucciones están paso por paso en el Prework.

---

<ins>Jupyter Notebooks</ins>

Ya hablamos sobre Jupyter Notebooks en el Prework. Vamos a hacer un pequeño repaso para que quede claro cómo aprovechar al máximo este REPL.

[**`Ejemplo 1`**](Ejemplo-01/notebook_de_practica.ipynb)

---

<ins>Variables en Python</ins>

En Python usamos `variables` para asignarles contenido que queremos utilizar después.

- La sintaxis es:

`nombre_de_variable = valor`

`valor` puede ser muchas cosas, que ya iremos aprendiendo poco a poco.

> Me parece muy importante hablar sobre la convención de nombramiento en Python: todas las variables y nombres de funciones se escriben en camel_case, sin excepciones. No es necesario mencionar la convención para clases en este momento, ya que ese tema no se tocará en este módulo.

[**`Ejemplo 2`**](Ejemplo-02/variables.ipynb)
[**`Reto 1`**](Reto-01/variables.ipynb)

---

<ins>Operaciones numéricas</ins>

Hemos estado asignando números a variables. En Python podemos realizar operaciones matemáticas de una forma muy sencilla. Simplemente tenemos que usar los `operadores aritméticos` que ya conocemos para hacer operaciones entre las variables que hayamos definido previamente. Los operadores aritméticos en Python son los siguientes:

- Suma: `+`
- Resta: `-`
- Multiplicación: `*`
- División: `/`
- Exponente: `**`

¡Practiquemos con ellos!

> Deje fuera división entera y módulo para no confundir a los alumnos. En el Ejemplo se va a usar la función `print`. No es necesario ahondar mucho en el tema, pero sí hay que mencionar la sintaxis básica de cómo llamar estas funciones. Se pueden usar los comandos de la terminal como referencia para que los alumnos tengan una analogía.

[**`Ejemplo 3`**](Ejemplo-03/operaciones_numericas.ipynb)
[**`Reto 2`**](Reto-02/operaciones_numericas.ipynb)

---

<ins>Tipos de datos en Python</ins>

Python tiene diferentes tipos de datos para representar diferentes cosas. Por el momento vamos a aprender los 4 más básicos y esenciales:

- `int` => números enteros
- `float` => números decimales
- `string` => secuencias de caracteres (texto)
- `boolean` => booleanos (True o False)

Por el momento no importa si no entiendes para qué sirven las strings y los booleanos. Eso lo veremos más adelante.

> Explicar por qué necesitamos diferentes tipos de datos, por qué a Python no le da igual leer un "1" que un 1. En el Ejemplo se va a usar la función `type` Hay que explicar cómo funciona llamar una función y pasarle el resultado a otra función.

[**`Ejemplo 4`**](Ejemplo-04/tipos_de_datos.ipynb)

---

<ins>Interpolación de Strings</ins>

Más adelante veremos que las Strings pueden contener información muy relevante dentro de nuestros conjuntos de datos (como nombres de personas, descripciones de procesos, categorías, etc). Por lo pronto, vamos a utilizar nuestras Strings para imprimir anotaciones en nuestros `outputs`. Queremos obtener resultados que se vean más o menos así:

`Suma de variable_1 y variable_2: 10`

Vamos a ver cómo hacer eso.

> Elegí f-strings por sobre las otras formas de interpolar strings porque son las más modernas y su sintaxis se parece mucho a la sintaxis de interpolación de otros lenguajes de programación (como JS y Swift).

[**`Ejemplo 5`**](Ejemplo-05/interpolacion_de_strings.ipynb)
[**`Reto 3`**](Reto-03/interpolacion_de_strings.ipynb)

---

<ins>Booleanos y operadores de comparación</ins>

Ya practicamos con `ints`, `floats` y `strings`. Sólo nos falta entender para qué usar los `booleanos`. Nuestros programas necesitan una manera de "tomar decisiones". Nosotros en la vida real solemos tomar decisiones haciendo comparaciones entre las opciones y tomando la decisión que más nos convenga tomando en cuenta el contexto. El primer paso para lograr esto son los `operadores de comparación`. Sirven para comparar valores. Regresan un booleano `True` cuando la comparación es cierta y un booleano `False` cuando la comparación es falsa.

Python tiene los siguientes `operadores de comparación`:

```
Mayor que: >
Mayor o igual que: >=
Menor que: <
Menor o igual que: <=
Igual que: ==
No igual (distinto) que: !=
```

Veamos cómo funcionan.

> Creo que es muy útil hacer esta referencia de las decisiones que tomamos en la vida real. ¿Cómo es que funciona la inteligencia humana? Y ¿cómo es que los programas emulan esta inteligencia para variar su output dependiendo del input que reciban?

[**`Ejemplo 6`**](Ejemplo-06/operadores_de_comparacion.ipynb)
[**`Reto 4`**](Reto-04/operadores_de_comparacion.ipynb)

---

<ins>Estructuras de control de flujo</ins>

Para finalizar, vamos a juntar todo lo que hemos aprendido el día de hoy y vamos a darle a nuestro programa la capacidad de tomar decisiones. Los programas tienen datos de entrada (inputs) y datos de salida (outputs). Varían sus outputs dependiendo del input que reciban. Para poder tomar decisiones, utilizan las llamadas `estructuras de control de flujo`. Que se ven así:

```
if var_1 > var_2:
    print("OK")
else:
    print("ERROR")
```

Vamos a ver cómo funcionan.

> Lo más importante de aclarar me parece que es la indentación de los bloques de las sentencias if. Se habló sobre ello en el Prework, pero es algo que puede ser confuso. Hay que mencionarlo repetidas veces para que los alumnos entiendan que lo que está indentado pertenece al bloque del if, y lo que no está indentando ya no pertenece.

[**`Ejemplo 7`**](Ejemplo-07/estructuras_de_control_de_flujo.ipynb)
[**`Reto 5`**](Reto-05/estructuras_de_control_de_flujo.ipynb)

---

### 3. Postwork

[**`Postwork Sesión 1`**](Postwork/Readme.md)
