# Ejercicio 1

SCP Sudoku

- Variables: Numeros de casillas
- Dominios: {1,2,3,4,5,6,7,8,9}
- Restricciones: casillas en una misma region, en una misma fila o columna deben ser distintos entre si

# Ejercicio 2

El algoritmo recibe un csp y genera una cola con todos los arcos en el csp, luego itera por toda la cola retirando el primero (pop) y probando si es consistente; si no lo es,
lo descarta, lo marca como eliminado y agrega a todos sus vecinos a la cola, si lo es, entonces simplemente lo saca de la cola, esto lo repite hasta que la cola este vacia, 
por lo que al final queda en el csp los nodos consistentes marcados

# Ejercicio 3


