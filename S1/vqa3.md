## VQA Derek

A diferencia de los dos anteriores papers, este se enfoca mucho más en el modelo utilizado y la forma en que llevaron a cabo las redes, los entrenamientos, etc. y mucho menos en la confección del _dataset_ de imagenes y respuestas.

En la misma linea de la explicabilidad de los modelos, llama la atención como este trabajo hace esfuerzos por unir fragmentos de distintos trabajos. Por un lado se esfuerza en lograr el objetivo del VQA que es poder responder correctamente a las preguntas dadas a parrtir de reconocer visualmente las imágenes. Por otro lado, se preocupa de reconocer cual es la parte de la imagen que explica la respuesta. De este modo se ve que pudieron hacer reconocimiento de _zonas relevantes_ de las imagenes y ver como estas inciden en el resultado, pareciera ser un _approach_ distinto al de los dos papers y que obtiene resultados bastante buenos.

Además, me parece muy interesante lo realizado al comparar los rendimientos en la tarea, según qué se utiliza. Similar al primer paper pero ahondando más en distintas categorías. Se explora primero solo con palabras, luego con palabras y la imagen, luego con palabras y regiones importantes promedio, y finalmente con palabras y regiones con pesos según relevancia. Es notable como, al seleccionar las regiones según su algoritmo, el rendmiento es el mejor de las 4 opciones.

A mi parecer lo logrado por el paper puede parecer contraintuitivo en ciertos niveles. Por un lado se habla mucho de que _hay_ que dejar que los modelos aprendan por si solos y que las represeentaciones intermedias las va aprendiendo el modelo según el _scope_ del problema, dejando de lado de cierto modo el llamado **conocimiento experto**. Pero por el otro lado se ve que cuando se van guiando el aprendizaje para VQA los resultados mejoran, para mi, esto es conocimiento experto y da luces de que no hay respuestas absolutas en este campo.

Como se observa en el paper, el _weighing_ de regiones da mejores resultados que solo darle la imagen y palabras al modelo, y esto aparte de aportar en la explicabilidad del modelo, muestra a mi parecer que hay mucho donde avanzar, donde la línea entre que decirle y que no al modelo para guiarlo puede ser muy delgada e interesante de explorar.

Raimundo Herrera Sufán
