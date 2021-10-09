# Ejercicio 1

CSP Sudoku

- Variables: 81 casillas
- Dominios: {1,2,3,4,5,6,7,8,9}
- Restricciones: casillas en una misma region, en una misma fila o columna deben ser distintos entre si

# Ejercicio 2

El algoritmo recibe un csp y genera una cola con todos los arcos en el csp, luego itera por toda la cola retirando el primero (pop) y probando si es consistente; si no lo es,
lo descarta, lo marca como eliminado y agrega a todos sus vecinos a la cola, si lo es, entonces simplemente lo saca de la cola, esto lo repite hasta que la cola este vacia, 
por lo que al final queda en el csp los nodos consistentes marcados

# Ejercicio 3
La complejidad de la comprobación de consistencia de arco puede analizarse como sigue:~~~~
un CSP binario tiene a lo más O(n^2) arcos; cada arco (Xk, Xi) puede insertarse en la agenda sólo d veces, porque Xi tiene a lo más d valores para suprimir; la comprobación de la consistencia de un arco puede hacerse en O(d²) veces; entonces el tiempo total, en el caso peor, es O(n²d³).

# Ejercicio 4
Para evitar llegar a O(n²d³) que es el peor caso podemos conservar las aristas que se sabe que son consistentes y asi evitar encolarlas nuevamente, esto nos dejaria en una solucion O(n²d²), ya que casi evitariamos revisar una pasada de dominio completa

# Ejercicio 5
## Inciso A
Para demostrar que cualquier PSR estructurado por árbol puede resolverse en tiempo lineal en el número de variables, tenemos 3 pasos en la resolución:

* Elija cualquier variable como la raíz del árbol, y ordene las variables desde la raíz a las hojas de tal modo que el padre de cada nodo en el árbol lo precede
en el ordenamiento. Etiquetar las variables X1..., Xn en orden. Ahora, cada variable excepto la raíz tiene exactamente una variable padre

* Para j desde n hasta 2, aplicar la consistencia de arco al arco (Xi, Xj), donde Xi es el padre de Xj, quitando los valores del DOMINIO[Xi] que sea necesario.

* Para j desde 1 a n, asigne cualquier valor para Xj consistente con el valor asignado para Xi, donde Xi es el padre de Xj.

El objetivo del algoritmo es resolver un problema de k-consistencia como uno de arco-consistencia. Para esto, podemos destacar dos puntos claves: 
* En el paso uno y dos convertimos el problema en arco-consistencia, entonces en el paso 3 no se requiere ninguna vuelta atras 
* En el segundo paso, al aplicar la comprobacion de consistencia de arco en orden inverso, el algoritmo asegura que cualquier valor suprimido no puede poner en peligro la consistencia de arcos que ya han sido tratados.

El algoritmo completo se ejecuta en tiempo O(nd²)  

## Inciso B
Gracias al ejercicio anterior, llegamos a la conclusión de que es posible resolver un CSP cuyo grafo de restricciones es un árbol, mediante la arco-consistencia de cada una de sus variables, es decir, el algoritmo citado en el ejercicio anterior resulta correcto para todos los CSP cuyo grafo de restrcciones pueda ser convertido en un árbol, a pesar de que en un principio parezca que tenemos que lidiar con la n-consistencia.

# Ejercicio 6

| Reinas | Algoritmo         | Tiempo                | Estados recorridos | 
| :----: | ----------------- | --------------------- | ------------------ |
| 4      | Forward Checking  | 6.794929504394531e-05 | 8                  | 
| 4      | Backtracking      | 8.106231689453125e-05 | 26                 |
| 8      | Forward Checking  | 0.0025751590728759766 | 113                |
| 8      | Backtracking      | 0.007006406784057617  | 876                | 
| 10     | Forward Checking  | 0.003156900405883789  | 102                | 
| 10     | Backtracking      | 0.009738683700561523  | 975                | 
| 12     | Forward Checking  | 0.012352943420410156  | 261                | 
| 12     | Backtracking      | 0.0370633602142334    | 3066               | 
| 14     | Forward Checking  | 0.08189225196838379   | 1359               | 
| 14     | Backtracking      | 0.2884037494659424    | 20280              | 
