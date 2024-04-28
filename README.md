# TP1 de TDA

## Ejecutar el algoritmo para un caso de prueba de "n" batallas

<code>python tp1.py NUMERO_DE_BATALLAS.txt</code>

Ejemplo:

<code>python tp1.py 50000.txt</code>

Al ejecutar el script, además de guardar las batallas ordenadas en un archivo nuevo (por ejemplo: 50000.txt” ---> “50000_solved.txt”), se imprime por consola la suma ponderada calculada para el caso ejecutado, y al final se imprime un “csv” con tuplas **(batallas_tamaño, tiempo_en_segundos)** donde se observa la complejidad medida del algoritmo.

## Ejecutar las pruebas de tiempo del algoritmo

<code>python generator.py</code>

Al ejecutar el script, se generar archivos con batallas aleatorias, y luego se miden los tiempos del algoritmo para esos archivos.

Los resultados se imprimen por consola.

## Ejecutar las pruebas de la cátedra

<code>python tp1_catedra_tests.py</code>