##VQA 1

Me parece un muy buen paper porque da luces sobre los desafíos de VQA y cuales son las formas en las que:

1. Recolectaron imágenes.
2. Hacer el desafío interesante para gente que quiere hacer sistemas de reconocimiento no triviales.
3. Diferenciar entre los distintos usos de VQA. 

Una de las partes más interesantes a mi juicio es la parte en que se distingue entre lo que son preguntas que requieren _common-sense_ y lo que son preguntas de baja complejidad. Mi primera impresión fue que se sería muy arbitrario para esa distinción, pero en el fondo la distinción es fundamental. 

Las imagenes tienen características intrínsecas en ellas que son "fácilmente" detectables con un sistema de bajo nivel, como son el color predominante, o la cantidad de objetos de un tipo. De todas formas me parecieron actividades no triviales pero para los autores, pareciera ser que las asumen como actividades de alguna u otra manera, resueltas.

Por otro lado las imagenes tienen características que requieren tanto a la imagen como a el sentido común, lo que a mi parecer hace esa distinción crucial. La pregunta que sale destacada da luces del tema, _"What is the mustache made of?"_ parece ser trivial si solo se toma en cuenta la pregunta, todos los bigotes son de pelo, pero la pregunta asociada a la imagen va más allá y tiene que ver con el contexto de esa imagen y las cosas que tiene puestas en la parte superior de su boca. Creo que desafiar a un sistema de aprendizaje de máquina a detectar dichas sutilezas es apuntar muy alto y me parece que es en la dirección correcta.

Ya habíamos discutido parcialmente esto en clases pero también encuentro interesante que se tome en consideración que ni los humanos están de acuerdo en ciertos aspectos respecto a las preguntas, por lo que para generar los _datasets_ hay que tomar en cuenta ese detalle, y en VQA se hace. En general críticas a sistemas de aprendizaje de máquinas es que hacen tareas simples, pero creo que en este paper se nota el esfuerzo por hacer tareas en las que a los humanos tampoco les va 100% bien, y se preocuparon de introducir las mismas estrategia que hacen a los humanos fallar al confeccionar las alternativas de las preguntas por ejemplo.

Es interesante el esfuerzo de diferenciar cuando se tienen las preguntas solas, las preguntas y los _tags_ de las imagenes, y cuando se tiene la imagen. Creo que si bien es evidente que los resultados serán mejores cuando se tiene la imagen, porque los _tags_ son más bien genéricos, es importante notar que esto elimina un sesgo importante a la hora de clasificar, ya que las ideas preconcebidas se van a la hora de ver la imagen. Esto a mi parecer da luces de que hay ciertas tareas para las que ciertos dominios, como los _tags_, pueden implicar grandes sesgos en los resultados, y que para cada tarea es importante saber que ciertos _inputs_ son más adecuados que otros.

Raimundo Herrera Sufán