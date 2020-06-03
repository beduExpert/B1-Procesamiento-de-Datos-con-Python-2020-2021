 ## Nombre del Postwork: Transformación, filtración y ordenamiento de datos

### OBJETIVO 

- Utilizar transformaciones de datos para limpiar y preparar un dataset para análisis.
- Realizar filtraciones para obtener conjuntos de datos.
- Reordenar datos para ver el conjunto desde diferentes perspectivas.


#### REQUISITOS 

- Tener un dataset sin `NaNs`, bien indexado y con nombres de columnas que sean comprensibles y coherentes.

#### DESARROLLO

Ha llegado el momento de aplicar técnicas comunes de procesamiento de datos a nuestro conjunto de datos. Para este momento ya debes de tener un conjunto de datos que te sea interesante y que haya sido limpiado previamente de `NaNs`. También es importante que ya hayas explorado extensivamente tu dataset para que lo conozcas muy bien. De igual manera, es recomendable que tu dataset esté bien indexado y que tenga nombres coherentes y comprensibles para las columnas.

Para aplicar en tu dataset lo que vimos en esta sesión, realiza las siguientes acciones:

1. Checa que todos tus datos tengan el tipo de dato correcto. Si no es así, usa casting para convertir tus datos al tipo de dato correcto (recuerda que tipos de dato como `datetime64` se guardan como strings cuando están en archivos .csv, así que tendrás que convertirlos al tipo de dato apropiado cada vez que importes tu archivo.)
2. Si tienes columnas de texto, asegúrate de que todas tengan el formato correcto. Si no es así, utiliza las técnicas de manipulación de `strings` para darles el formato que necesitas.
3. Si consideras que alguna de tus columnas sería más clara si los datos tuvieran otro formato o representación usa `map` para transformar los datos de esa columna.
4. Si crees que es posible generar nuevas columnas útiles a partir de las columnas que ya tienes, usa `apply` para generar nuevos datos a partir de los que tienes y añádelos a tu dataset.
5. Con el fin de responder algunas de las preguntas que te planteaste acerca de tu dataset, usa filtros y sorting para crear nuevos subconjuntos y reordenamientos que sean más adecuados para responder tus preguntas. Primero comienza intentando responder las preguntas que te planteaste al principio, pero después puedes solamente explorar para ver si encuentras otras preguntas que no te habías planteado anteriormente.

Comparte tus dudas y hallazgos con tus compañeros y con la experta, de manera que todos puedan nutrirse mutuamente de su trabajo.

¡Bonne chance!
