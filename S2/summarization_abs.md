##Summarization Abstractive

En primer lugar me parece destacable el concepto de resumen _abstracto_ por sobre el de resumen _extractivo_, donde el último corresponde a resumir copiando partes del texto, en cuanto el primero corresponde a generar nuevas frases utilizando conceptos no necesariamente utilizados en el texto. Desde un principio parece ser más desafiante que el extractivo, ya que para resumir abstractamente se necesita un conocimiento más acabado del contexto y significado de las palabras, mientras que extractivamente bastaría (sin desmerecer la labor, solo como primera impresión) con seleccionar las frases clave.

Más adelante se mencionan los esfuerzos por evitar repeticiones en los resumenes usando modelos de atención intra-temporales. Me parece interesante el hecho de que se intente reducir la repetición de palabras pero creo que sería interesante mostrar más sobre los efectos que tiene dicha decisión en el modelo final. Elucuburando, se me ocurre que quizás se incluyen conceptos menos relevantes solo por el hecho de forzar la no repetición, lo que en si no tiene por qué ser negativo, sin embargo, creo que un comentario habría sido un buen elemento de aclaración.

En la misma linea, en los esfuerzos de evitar repetición me parece valioso el comentario que se realiza sobre ambas funciones de atención, _intra-decoder_ e _intra-temporal_, donde se señala que su definición es aplicable a diversos tipos de redes recurrentes, ya que sus cálculos computan nuevos vectores y no implican cambios en la función subyacente particular de por ejemplo la LSTM implementada.

La última estrategia para evitar repeticiones, que surge tras analizar los datasets de resumenes, me parece una idea un poco específica y quizás mala ya que viene del hecho de que como no ocurre cierta estructura en el dataset, entonces su resultado tampoco debería tenerla, lo que me parece va un poco en la línea de añadir secuencias `if` para cada particularidad y no dejar que el modelo se robustezca por su estructura.

Me parece sumamente interesante como la mezcla de los modelos consigue una mejor _readability_. En la parte en la que se define el modelo creo que es interesante el hecho de que se agregue otro parámetro **_gamma_** que sopese ambas funciones, la del primer modelo y la del segundo. No se habla en profundidad de la importancia de ese parámetro pero pareciera ser que su valor influiría en la _readability_ si se le da más importancia al modelo ML y por el otro lado si se le da más importancia al RL, los resultados serían más cercanos al _ground truth_. Me parece que falta explorar un poco los resultados en cuanto a ese hiperparámetro o mencionar como se optimizó la elección del mismo, porque a mi juicio es muy relevante.

Los resultados son bastante buenos, quizás me gustaría tener una comparación de los resultados de Mechanical Turk entre la puntuación obtenida por cada uno de los 3 modelos y la puntuación obtenida por el _ground truth_. Sin embargo, parecen ser puntajes bastante altos.

Raimundo Herrera Sufán