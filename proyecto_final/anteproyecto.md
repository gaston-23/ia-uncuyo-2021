# Entrenamiento de Agente jugador de Snake con Reinforcement Learning

## Código del proyecto: STSP (Self Taught Snake Player)

## Integrantes: Gastón Cavallo y Juan Manuel Fernandez

### Introducción:

  La idea detrás de este trabajo es la de explorar el mundo del aprendizaje reforzado aplicado al campo de los videojuegos. La realidad es que la forma de aprender a jugar
  videojuegos (o cualquier juego de la vida real) es mediante la experimentación del mismo, es decir, jugar repetidamente hasta conocer con claridad las reglas y, por que no,
  hacerse mejor en el juego en cuestión.
  
  Es justo por lo anteriormente mencionado, que el aprendizaje reforzado, o reinforcement learning en inglés, nos pareció la mejor aproximación al problema de aprender, conocer
  y mejorar en un entorno cuyas reglas y condiciones resultan en principio desconocidas para el agente. Si se exploran otras alternativas, como lo es el aprendizaje supervisado,
  automáticamente nos encontramos con dos limitaciones claras: Generar un dataset para juego como Poker o Snake con suficientes ejemplos resulta tedioso o casi imposible, y por
  otro lado, si obtuviesemos los datos necesarios de un jugador de los mismos, el agente jamás lograría ser mejor que el jugador que generó los datos, ya que el agente es una fiel copia
  de los movimientos realizados por el jugador con anterioridad.
  
  Sin embargo, el aprendizaje reforzado tiene sus limitaciones, debemos dar instrucciones precisas al agente de "como aprender", con cuestiones como lo son la función de costo,
  o la manera en la que perciben el entorno, ya que en caso de que alguna de estas (entre otras variables) no resulte la mas óptima, el agente puede nunca llegar a aprender las reglas
  y mucho menos mejorar con el tiempo. Es a partir de estas variables que pretendemos medir el desempeño del agente, es decir, hacer ligeras modificaciones en la función de costo,
  como en la representación de los estados para observar la variación de la performance del agente en el juego, en este caso, puntuación máxima de manzanas que el agente es capaz 
  de recolectar. El trabajo estará inspirado y basado en el siguiente [artículo](https://towardsdatascience.com/snake-played-by-a-deep-reinforcement-learning-agent-53f2c4331d36),
  en el cual se muestra una implementación del videojuego con un agente basado en Deep Reinforcement Learning.
  
  Gracias al artículo citado, tenemos una visión de como se podría plantear el entorno para que el agente sea capaz de aprender, modelando estado del mapa mediante posiciones, 
  teniendo el agente que decidir entre 4 acciones: Arriba, Izquierda, Derecha y abajo, dichas decisiones las tomará en base a la posición de su cuerpo y si tiene paredes en la proximidad.
  
  La pregunta que puede surgir es: ¿ Por que no tratar este problema con un simple programa que juegue desde un principio ? La realidad es que resulta viable programar un "bot"
  capaz de jugar snake, pero como todo programa cuyo funcionamiento algorítmico fue diseñado por alguien, jamás será mejor que su creador, como ya se mencionó con anterioridad.
  Mediante la implementación de aprendizaje reforzado se pueden lograr cosas impresionantes, como es el caso de la supercomputadora de IBM entrenada para jugar ajedrez, siendo
  capaz incluso de ganar a cualquiera de los mejores jugadores del mundo, un resultado literalmente imposible, si ésta, no es programada por el mismisimo mejor jugador del mundo, y 
  aún así, el agente estaría limitado a ser igual de bueno que el mejor del mundo y nunca mejor...
  La magia detrás del reinforcement learning se encuentra en que, el agente, jugará de manera completamente distinta a su creador y, en ocasiones, incluso mejor.
  

  ## Bibliografia
  Se consultó el libro AIMA 3rd Edition y AIMA 2da Edition (en español)

  [Snake Played by a Deep Reinforcement Learning Agent](https://towardsdatascience.com/snake-played-by-a-deep-reinforcement-learning-agent-53f2c4331d36)

  ## Justificacion
  El objetivo de este trabajo es la investigacion y comparacion de los algoritmos de reinforcement learning asi como tambien su aplicacion el un ejemplo tangible como es la puesta en ejecucion del clasico juego "Snake", se comparara el algoritmo Q-Learning en metricas como tiempo de respuesta para alcanzar una misma puntuacion (eficiencia), puntuacion maxima alcanzada y performance ante distintos escenarios
  Y como posible objetivo extra sera aplicar algun algoritmo de Deep RL y comparar en las mismas metricas.
  ## Tiempo total estimado: *26 dias*

  ## Actividades a llevar a cabo
  
  1. Lectura de articulos *[2 días]*
  
  2. Investigar algoritmos de Reinforcement Learning *[2 días]*
  
  3. Leer bibliografía para profundizar en los algoritmos *[4 días]*
  
  4. Elección del algoritmo a implementar *[1 día]*
  
  5. Búsqueda de librerías o implementación propia del algoritmo *[3 días]*
  
  6. Adaptación del entorno de Snake para funcionar con nuestro algoritmo *[3 días]*
  
  7. Plantear el modelo de entrenamiento para el algoritmo *[4 días]*
  
  8. Ajustar variables para un mejor aprendizaje del agente *[2 días]*
  
  9. Revisar los resultados obtenidos y redactar el informe final *[5 días]*

  ## Cronograma
  
  | Actividad | Dia 1 | Dia 2 | Dia 3 | Dia 4 | Dia 5 | Dia 6 | Dia  7| Dia 8 | Dia 9 | Dia 10 | Dia 11 | Dia 12 | Dia 13 | Dia 14 | Dia 15 | Dia 16 | Dia 17 | Dia 18 | Dia 19 | Dia 20 | Dia 21 | Dia 22 | Dia 23 | Dia 24 | Dia 25 | Dia 26 |
  | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
  | Lectura de articulos                                                  | X | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
  | Investigar algoritmos de Reinforcement Learning                       |   |   | X | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
  | Leer bibliografía para profundizar en los algoritmos                  |   |   |   |   | X | X | X | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
  | Elección del algoritmo a implementar                                  |   |   |   |   |   |   |   |   | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
  | Búsqueda de librerías o implementación propia del algoritmo           |   |   |   |   |   |   |   |   |   | X | X | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
  | Adaptación del entorno de Snake para funcionar con nuestro algoritmo  |   |   |   |   |   |   |   |   |   |   |   |   | X | X | X |   |   |   |   |   |   |   |   |   |   |   |
  | Búsqueda de librerías o implementación propia del algoritmo           |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X | X | X | X |   |   |   |   |   |   |   |
  | Ajustar variables para un mejor aprendizaje del agente                |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X | X |   |   |   |   |   |
  | Revisar los resultados obtenidos y redactar el informe final          | X | X | X | X | X | X | X | X | X | X | X | X | X | X | X | X | X | X | X | X | X | X | X | X | X | X |
