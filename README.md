# Reto_Python: Búsqueda de Números Primos

## Descripción del Reto

Este reto consiste en desarrollar un programa que identifique y liste todos los números primos en el rango del 1 al 250. El objetivo es practicar conceptos fundamentales de Python como funciones, bucles, condicionales y manejo de archivos.

## Objetivo

Crear un algoritmo eficiente que:
- Identifique correctamente números primos
- Procese el rango completo del 1 al 250
- Guarde los resultados en un archivo
- Sea verificable mediante pruebas automatizadas

## ¿Qué es un Número Primo?

Un número primo es un número natural mayor que 1 que tiene exactamente dos divisores: el 1 y él mismo. Los primeros números primos son: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29...

## Estructura del Proyecto

### Archivos

- **Ejercicio.py**: Contiene la lógica principal del reto
  - Función `es_primo(numero)`: Determina si un número es primo
  - Script principal que itera del 1 al 250 y guarda los primos encontrados

- **Pruebas.py**: Suite de pruebas automatizadas usando pytest
  - Valida números primos conocidos
  - Verifica números no primos
  - Prueba casos borde (números negativos, cero)
  - Verifica números grandes dentro del rango

- **results.txt**: Archivo de salida con los resultados
  - Contiene todos los números primos encontrados (uno por línea)
  - Se genera automáticamente al ejecutar `Ejercicio.py`

## Algoritmo de Detección de Primos

El programa utiliza un algoritmo de prueba por división:

1. **Caso base**: Los números ≤ 1 no son primos
2. **Iteración**: Prueba si el número es divisible por cualquier número desde 2 hasta n-1
3. **Resultado**: Si encontramos un divisor, no es primo; si no, sí lo es


## Ejecución

### Ejecutar el programa principal:
```bash
python Ejercicio.py
```

### Ejecutar las pruebas:
```bash
pytest Pruebas.py
```

## Resultados

El programa encontró un total de **53 números primos** en el rango 1-250:

2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241

## Conceptos Practicados

- ✅ Definición y uso de funciones
- ✅ Estructuras de control (bucles, condicionales)
- ✅ Operaciones matemáticas (módulo)
- ✅ Manejo de archivos (lectura/escritura)
- ✅ Pruebas unitarias con pytest
- ✅ Documentación de código

## Notas

- El algoritmo utilizado es simple pero funcional para el rango especificado
- Para rangos mucho mayores, se podría optimizar usando el Criba de Eratóstenes
- Todas las pruebas pasan correctamente validando la solución
