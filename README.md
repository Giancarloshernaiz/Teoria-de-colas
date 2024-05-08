# Evaluación I - Colas con Retrabajos

## Elaborado por: Giancarlos Hernaiz @Giancarloshernaiz y Sebastian Medina @sebasmedina2003

## Requerimientos

- Python virtual environment (venv)

- Install Flet

## Enunciado

Modela un sistema de colas que permita retrabajos. Implementa un mecanismo en el que los clientes que no fueron atendidos correctamente puedan regresar al final de la cola. Calcula el impacto en el tiempo promedio en el sistema y la tasa de retrabajos.

## Implementación

Simularemos una gasolinera, donde cada carro representa un elemento de la cola, en este modelo existe una sola cola y cada estación va atendiendo a los carros dependiendo de su orden de llegada (FIFO).

Para resolver este problema le dimos a cada carro arbitrariamente un tiempo random de tardanza en la estación de gasolina de 1 a 3 segundos, aparte de un riesgo (también random) de no poder ser atendido y tener que volver a la cola.
