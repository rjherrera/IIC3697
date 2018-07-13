## VQA 2

En primer lugar me parece muy interesante como parte el paper, que es abordando los distintos sesgos que vienen con el lenguaje y con la forma de confeccionar las preguntas.

En particular que se aborde un _bias_ que no es tan intuitivo, el de las preguntas que son adecuadas para cada imagen. Esto es, preguntar si existe un objeto en la imagen, solo en las imagenes que tienen el objeto. Parece evidente, pero no es tan claro que se evite esto, habría que preguntar por cosas muy aleatorias/arbitrarias en todas las imagenes.

La intuición señalada en el paper es que otorgar la misma pregunta a imagenes distintas, repercute en que si la respuesta es distinta, **hay** que observar la imagen para poder diferenciar. Además como see menciona después en el paper, hubo preocupación no solo de que hubieran respuestas distintas a la misma pregunta sobre distintas imágenes, sino que también las imágenes fueran similares semánticamente, de modo que la granularidad de la distinción y la necesidad de _entender_ la imagen fuera alta.

Me parece interesante la idea de probar los sistemas ya entrenados con este nuevo _dataset_ balanceado y no entrenar uno nuevo antes, porque muestra realmente los sesgos que existían. Es una buena forma de validar trabajo anterior.

Es interesante también que los mismos modelos al entrenarlos y testearlos con este _dataset_ balanceado tienen rendimientos similares a los resultados de los entrenados y testeados con el desbalanceado (comparando BB con UU en la notación del paper). Esto muestra como dicen que los modelos son _data-starved_ lo que sugiere que a mejor dataset mejor resultado, lo que a mi parecer habla bien del modelo pues empeora pero no significativamente al mejorar la variedad del _dataset_, pero no habla tan bien de lo capaz de generalizar del modelo, ya que generaliza solo cuando su _dataset_ es lo suficientemente generalizado.

Finalmente la parte de los contraejemplos la encuentro sumamente atractiva para dos cosas:

1. Robustecer los modelos porque la noción de imagenes que son similares a la que se está evaluando pero donde la respuesta es distinta, da luces de lo necesario que es _meterse_ en la imagen y entender realmente lo que pasa, no _achuntarle_.
2. Darle explicabilidad al modelo, de cierto modo lo que se menciona en el paper y que se ha hablado en clases y en IA sobre exigir que los modelos de ML no sean cajas negras, se aborda un poco con esta estrategia ya que se muestra como está _razonando_ el modelo, a partir de las cosas que está descartando.

Raimundo Herrera Sufán


