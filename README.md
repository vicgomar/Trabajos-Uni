# Project Euler - Problema 19: Contar domingos

## Descripción

Este proyecto resuelve el problema 19 de Project Euler, que consiste en calcular cuántas veces el primer día de un mes cayó en domingo durante el siglo XX.

El periodo que se analiza comienza el 1 de enero de 1901 y termina el 31 de diciembre de 2000.

## Objetivo

Determinar la cantidad de domingos que coincidieron con el primer día de cada mes durante los años 1901 a 2000.

## Lenguaje utilizado

- Python 3

## Funcionamiento del programa

El programa utiliza:

- Una función para identificar si un año es bisiesto.
- Una lista que almacena los días de cada mes.
- Ciclos `for` para recorrer los años y los meses.
- Condiciones `if` para identificar los domingos.
- El operador módulo `%` para calcular el día de la semana.

Se toma como referencia que el 1 de enero de 1900 fue lunes.

## Ejecución

Para ejecutar el programa, abre una terminal en la carpeta del proyecto y escribe:

```bash
python main.py
```

## Resultado

La respuesta obtenida es:

**171 domingos.**

## Autor
Victor Manuel Gomez Marquez
Proyecto realizado como ejercicio de programación en Python.
