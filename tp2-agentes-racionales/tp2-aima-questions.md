# 2.10 Considere una versión modificada del entorno de la aspiradora del Ejercicio 2.7, en el que se penalice al agente con un punto en cada movimiento.
## a. ¿Puede un agente reactivo simple ser perfectamente racional en este medio? Explíquese

Un agente racional actua obteniendo el mejor resultado esperado, un agente reactivo simple no tiene sensores o conocimiento del entorno, en este caso, el agente reactivo simple actua casi por aleatoriedad, por lo que si descontamos un punto por cada movimiento realizado, es posible que nunca alcance una puntuacion aceptable
## b. ¿Qué sucedería con un agente reactivo con estado?

Al ser un agente reactivo con estado, actuaria solo conociendo los datos de donde esta parado, y por ende, nuevamente no seria prefectamente racional, solo que esta vez tendria un nivel menos de ineficiencia, pudiendo obviar de realizar las acciones "idle" y "limpiar" en el caso de una casilla que este limpia

## c. ¿Cómo se responderían las preguntas a y b si las percepciones proporcionan al agente información sobre el nivel de suciedad/limpieza de todas las cuadrículas del entorno?

Al conocer los estados de todas las cuadriculas del entorno podriamos hacer el agente racional, en el sentido de que evite chocarse las paredes, buscar el camino mas corto hacia la proxima casilla sucia, etc

---
# 2.11 Considere una versión modificada del entorno de la aspiradora del Ejercicio 2.7, en el que la geografía del entorno (su extensión, límites, y obstáculos) sea desconocida, así como, la disposición inicial de la suciedad. (El agente puede ir hacia arriba, abajo, así como, hacia la derecha y a la izquierda.)

## a. ¿Puede un agente reactivo simple ser perfectamente racional en este medio? Explíquese.
No, nuevamente la respuesta se asemeja al caso anterior, en este caso, al no tener penalidad, el agente seria capaz de recorrer todo el entorno y lograr limpiar todas las casillas, pero el problema es que la resolucion no seria eficiente y podria tomar demasiado tiempo, es decir, deberiamos considerar que al no conocer los imites o disposicion de la suciedad, el agente podria dar vueltas sin sentido por mucho tiempo e incluso toparse con casillas sucias y no limpiarlas

## b. ¿Se puede diseñar un entorno en el que el agente con la función aleatoria obtenga una actuación muy pobre?

Si, es posible, si se considera un entorno lo suficientemente grande, es posible que al agente le tome mucho tiempo concluir la tarea de limpiar todo (considerando infinitos movimientos). 

## c. ¿Puede un agente reactivo simple con una función de agente aleatoria superar a un agente reactivo simple?

Dificilmente podria superarlo por amplio margen, el problema esta en la escencia de ambos, que al no considerar el entorno completo, no pueden optimizar la busqueda de casillas sucias, ambos dependen de su aleatoriedad en cuanto a tomar las decisiones. Para concluir, se puede destacar que si es posible que el agente aleatorio pueda superarlo, pero la diferencia seria poca.

## d. ¿Puede un agente reactivo con estado mejorar los resultados de un agente reactivo simple?

Si, puede mejorar los resultados ya que el agente con estados seria capaz de guardar las casillas recorridas y evitar pasar sobre las mismas que ha visitado y generar movimientos extra, como lo haria el agente simple
