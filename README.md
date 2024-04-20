## Como ejecutar las pruebas del algoritmo greedy del TP1

Las pruebas se pueden repetir utilizando el código de nuestro repositorio:

<https://github.com/MatiVazquezMorales/TDA-tp1/tree/main>

En la rama **main** hay 3 archivos:

·         **tp1.py:** al ejecutar este script, se procesan los archivos de batallas guardados en la carpeta “generated” (si fueron sets de datos generados usando el archivo generator.py) o en la carpeta “tests\\data” (los archivos de prueba de la cátedra) si se cambia el valor de la variable DATASET_PATH para que apunte a esa carpeta.

·         **tp1_tests.py:** al ejecutar este script, se corren los tests unitarios con los archivos de batallas de la cátedra. Todos los tests pasan con nuestro algoritmo, tal como se espera.

·         **generator.py:** al ejecutar este script, se generan casos de prueba aleatorios de batallas con distintos tamaños de datos (los tamaños a generar están indicados en la variable “amounts”). Todos los archivos creados se guardan en la carpeta “generated”. Para procesar estos archivos generados hay que ejecutar tp1.py

Al ejecutar tp1.py, además de guardar las batallas ordenadas en sus respectivos archivos nuevos (por ejemplo: “100.txt” ---> “100_solved.txt”), se imprime por consola la suma ponderada calculada para cada caso ejecutado, y al final se imprime un “csv” con tuplas **(batallas_tamaño, tiempo_en_segundos)** donde se observa la complejidad medida del algoritmo.