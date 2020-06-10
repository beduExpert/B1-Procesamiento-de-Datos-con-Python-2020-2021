<div style="text-align: right"><strong>Curso Data Analysis - Módulo 3</br>PREWORK de Fundamentos de Python</strong></div>

<div style="text-align: center; color:#FF0000"><strong>PREWORK</br>SESIÓN 1</strong></div>

### Introducción

¡Bienvenido al módulo de Procesamiento de Datos con Python! En esta primera sesión aprenderemos a usar algunas herramientas sumamente importantes que estaremos utilizando a través de todo el módulo. Empezaremos platicando rápidamente sobre el Procesamiento de Datos y por qué es tan importante. Después, aprenderemos acerca de Jupyter Notebooks y por qué son útiles para los científicos de datos. Además, aprenderemos algunas cosas básicas del lenguaje de programación Python.

#### Objetivos

1. Identificar la razón por la cual el Procesamiento de Datos es tan importante para la Ciencia de Datos.
2. Utilizar Jupyter Notebooks, el IDE por excelencia de los científicos de datos.
3. Identificar y utilizar los principios básicos de Python.

#### TODO

- Instrucciones para clonar el repo
- Cambiar todo a Google Colab

### ¿Por qué es importante el Procesamiento de Datos?

Todo proyecto de Ciencia de Datos tiene una serie de pasos necesarios para ser realizado con éxito. Normalmente todo empieza con la identificación de un problema en el mundo real. Después de encontrar un problema que creemos que requiere una solución, el paso siguiente es entender el problema. Para entender el problema, necesitamos datos. Puede que ya exista una base de datos disponible que haya sido construida para recopilar instancias del proceso que estamos estudiando. Puede que esa base de datos aún no exista y primero necesitemos pensar sobre cómo recopilar esos datos. De cualquier manera, normalmente el proceso de recopilación y adquisición de los datos es un proceso algo confuso. La realidad no es ordenada, y nuestros datos van a ser un reflejo de esa realidad. Es muy probable que a la hora de obtener nuestra base de datos, nos demos cuenta de que está llena de errores: datos vacíos, formatos inadecuados, columnas innecesarias, tipos de datos incorrectos, la lista sigue y sigue y sigue.

Si intentamos hacer análisis estadístico o visualizaciones de datos con una base de datos desordenada, nos toparemos con muchos problemas. Nuestros análisis serán imprecisos y lo más probable es que terminemos con conclusiones incorrectas. Aquí es donde entra el Procesamiento de Datos. El Procesamiento de Datos reúne toda una serie de herramientas que sirven para explorar, limpiar, transformar, ordenar y estructurar los datos de manera que puedan ser útiles para su posterior análisis y visualización. En este módulo aprendemos cómo realizar estos procesos esenciales y nos prepararemos para poder realizar procesos aún más complejos en módulos posteriores.

### Clonar nuestro repositorio

Para poder realizar los ejercicios diseñados para este módulo es necesario que clones el repositorio del módulo a tu computadora. Probablemente ya hiciste esto en los módulos anteriores, pero en caso de que no lo hayas hecho, he aquí un

### Introducción a Python

En este prework vamos a hablar rápidamente acerca de algunos de los conocimientos fundamentales que necesitamos para programar en Python. Durante la clase presencial se realizarán numerosos ejercicios prácticos que te ayudarán a dominar estos temas. Por lo pronto, recomiendo ampliamente que vayas reescribiendo todo el código que veas aquí en tu propio JN. **NUNCA** hagas copy-paste. La única forma de aprender de verdad es escribir línea por línea, letra por letra, con tus propias manos.

#### Variables en Python

Los lenguajes de programación suelen incluir las famosas **variables**. Podemos pensar en las variables como "contenedores" de información a largo plazo. Son lugares en tu código donde puedes guardar cosas que quieres volver a utilizar después. Para poder crear una variable lo primero que tienes que hacer es elegir un nombre para la variable:

<div style="padding: 10px; margin: 20px"><img src='./Imgs/notebook_10.png'></div>

Después usas un `operador de asignación` que es un signo de "igual":

<div style="padding: 10px; margin: 20px"><img src='./Imgs/notebook_11.png'></div>

Y acto seguido, escribes el valor que quieres "asignar" a tu variable:

<div style="padding: 10px; margin: 20px"><img src='./Imgs/notebook_12.png'></div>

Entonces, el `operador de asignación` lo que hace es indicarle a Python que "el valor que está a la derecha del operador va a ser asignado a la variable que está a la izquierda del operador".

Si corro mi celda, la variable ha sido asignada, y ahora ese número `10`está "guardado" en mi variable `variable_1`. ¿Cómo accedo a ella? Basta con escribir el nombre de la variable y JN me muestra el valor como un `output` de mi celda:

<div style="padding: 10px; margin: 20px"><img src='./Imgs/notebook_13.png'></div>

Puedo asignar cuantas variables quiera y Python va a "recordarlas" (cuando uso palabras entre comillas es porque el término que estoy usando no es técnicamente correcto, pero es una analogía útil para entender lo que está pasando) por mí:

<div style="padding: 10px; margin: 20px"><img src='./Imgs/notebook_14.png'></div>

Hemos estado asignando varios números a estas nuevas variables, ¿ahora qué? ¿Qué podemos hacer con esos números? Dado que son números, ¡resulta que podemos realizar operaciones matemáticas con ellos!

#### Operadores matemáticos

Los operadores matemáticos en Python son exactamente los mismos que hemos aprendido en la escuela: `+`, `-`, `*`, `/`. Podemos usarlos para realizar operaciones matemáticas con nuestras variables (ya que nuestras variables tienen **números** asignados):

<div style="padding: 10px; margin: 20px"><img src='./Imgs/notebook_15.png'></div>

JN sólo me muestra el output de la última línea de código que hay en mi celda, así que si quiero ver el resultado de varias operaciones en la misma celda, tengo que usar un "comando" llamado `print`. `print` imprime lo que sea que reciba, para que podamos verlo con nuestros propios ojos:

<div style="padding: 10px; margin: 20px"><img src='./Imgs/notebook_16.png'></div>

Para usar el comando `print` escribimos la palabra "print", después abrimos paréntesis `()` y escribimos dentro del paréntesis lo que queremos imprimir. Estos "comandos" en Python se llaman `funciones` y es así como les llamaremos a partir de ahora. Veremos más a detalle lo que son las funciones en una sesión posterior.

#### Tipos de datos

En Python y en cualquier otro lenguaje de programación podemos representar diferentes tipos de datos. Hasta ahora hemos trabajado solamente con números. Pero de hecho Python no les llama "números". Python tiene dos tipos de datos para representar distintos tipos de números:

- `int` para números enteros
- `float` para números decimales

Podemos usar la función `type` para "preguntarle" a Python qué tipo de dato tenemos en nuestras variables:

<div style="padding: 10px; margin: 20px"><img src='./Imgs/notebook_17.png'></div>

Si quisiéramos ver los dos tipos en la misma celda, simplemente tenemos que llamar las funciones `type` con los nombres de nuestras variables y después pasarle el resultado a nuestra función `print`:

<div style="padding: 10px; margin: 20px"><img src='./Imgs/notebook_18.png'></div>

Otro tipo de datos muy importante es el que se llama `string`. Un `string` es una secuencia de carácteres, que podemos usar para representar texto:

<div style="padding: 10px; margin: 20px"><img src='./Imgs/notebook_19.png'></div>

Para escribir texto en Python, tenemos que delimitar una secuencia de carácteres con el signo de comillas (`"`). Podemos imprimir `strings` para ir anotando los resultados de nuestro código:

<div style="padding: 10px; margin: 20px"><img src='./Imgs/notebook_20.png'></div>

También podemos imprimir variables dentro de `strings` usando lo que se llama `interpolación de strings`. Eso funciona de la siguiente manera: Empezamos una `string` con la letra `f` antes de las comillas, luego abrimos las comillas, después escribimos texto y cuando queremos interpolar una variable, usamos llaves (`{}`) y escribimos el nombre de la variable dentro de las llaves; finalmente cerramos las comillas:

<div style="padding: 10px; margin: 20px"><img src='./Imgs/notebook_21.png'></div>

¡Facilísimo!

Hay un último tipo de dato que vamos a aprender, porque está muy relacionado con los temas que vienen más adelante. Este tipo de dato es lo que llamamos `booleano`. Un dato `booleando` sólo puede tener dos valores: `True` o `False` (verdadero o falso):

<div style="padding: 10px; margin: 20px"><img src='./Imgs/notebook_22.png'></div>

¿Te parece extraño que esto exista? Quedará mucho más claro por qué necesitamos `booleanos` en esta siguiente sección...

#### Comparaciones

Si escribiéramos un programa que sólo pudiera hacer una sola cosa, siempre, independientemente del `input` (los datos de entrada) que tuviera, ése programa no sería muy útil. Para automatizar procesos también tenemos que automatizar la toma de decisiones, y para esto necesitamos la capacidad de hacer comparaciones entre datos. Como cuando nosotros comparamos un helado de chocolate y un helado de frambuesa y elegimos el de chocolate porque resulta que:

1. Es más barato
2. Es más delicioso
3. Somos alérgicos a la frambuesa

Estamos comparando los helados para poder tomar una decisión de qué comprar.

Los `operadores de comparación` de Python nos permiten hacer exactamente esto. Por el momento no vamos a comparar helados, sino nuestros ya conocidos `ints` y `floats`:

<div style="padding: 10px; margin: 20px"><img src='./Imgs/notebook_23.png'></div>

Basta con escribir la condición `var_1 < var_2` para que Python compare los valores contenidos en cada variable y te diga si efectivamente la `var_1` es más pequeña que la `var_2`. Este signo `<` se llama `menor que`. Python tiene varios operadores de comparación que podemos ver en la siguiente imagen:

<div style="width: 250px; padding: 10px; margin: 20px"><img src='./Imgs/notebook_24.png'></div>

Como puedes imaginar, en este caso todos los resultados son `True` porque las comparaciones resulta que son ciertas. Pero si intercambiamos los números podemos hacer que todas sean `False`:

<div style="width: 250px; padding: 10px; margin: 20px"><img src='./Imgs/notebook_25.png'></div>

¿Por qué queremos hacer comparaciones? Pues para tomar decisiones. ¿Y cómo tomamos decisiones en código? Utilizando las llamadas estructuras de control de flujo:

#### Estructuras de control de flujo

Las estructuras de control de flujo nos permiten usar comparaciones para tomar decisiones acerca de qué pasos tomar en el futuro. La primera estructura de control es lo que llamamos `if`:

<div style="padding: 10px; margin: 20px"><img src='./Imgs/notebook_26.png'></div>

Le pido a Python que haga la comparación `4 < 7`, y si esta comparación resulta `True` entonces corro el código que tengo debajo. Presta atención al código de la segunda línea. Está indentado, ¿lo ves? Esto es muy importante. Para Python, todo el código que está indentado pertenece al bloque de la `sentencia if` y se correra si la comparación resulta ser `True`.

Veamos qué pasa si la condición no se cumple:

<div style="padding: 10px; margin: 20px"><img src='./Imgs/notebook_27.png'></div>

No se corre el bloque de la `sentencia if` porque la comparación es `False`. Pero si yo imprimo algo fuera de la `sentencia if`, eso se imprimirá de todas maneras, porque no pertenece al bloque y por lo tanto no depende de la comparación:

<div style="padding: 10px; margin: 20px"><img src='./Imgs/notebook_28.png'></div>

Podemos también agregar una condición `default` para decirle a Python: Si la comparación no se cumple, entonces corre este otro código. Esto lo hacemos usando el operador `else`:

<div style="padding: 10px; margin: 20px"><img src='./Imgs/notebook_29.png'></div>

También podemos encadenar varias comparaciones, para cuando queramos tener múltiples condiciones que resulten en diferentes acciones. Esto se hace usando el operador `elif`:

<div style="padding: 10px; margin: 20px"><img src='./Imgs/notebook_30.png'></div>

Veamos qué pasa si cambiamos los valores de las variables:

<div style="padding: 10px; margin: 20px"><img src='./Imgs/notebook_31.png'></div>

Y a ver este otro:

<div style="padding: 10px; margin: 20px"><img src='./Imgs/notebook_32.png'></div>

Efectivamente, si `var_1`no es menor ni mayor a `var_2`, ¡lo único que queda es que sean iguales!

Con eso damos por concluido nuestro Prework de esta sesión. ¡En el Work practicaremos mucho todo lo aprendido para afianzar todo este conocimiento!
