'''
# Evaluación I - Métodos Cuantitativos
# Elaborado por: Giancarlos Hernaiz y Sebastián Medina

# Colas con retrabajo

# Enunciado: Modela un sistema de colas que permita retrabajos. Implementa un mecanismo en el que los clientes que no fueron atendidos correctamente puedan regresar al final de la cola. Calcula el impacto en el tiempo promedio en el sistema y la tasa de retrabajos.
'''
import flet as fl

async def main(page: fl.Page) -> None:
  page.title = "Colas con Retrabajos"
  page.vertical_alignment = fl.MainAxisAlignment.CENTER
  page.horizontal_alignment = fl.MainAxisAlignment.CENTER
  page.window_center()
  page.window_resizable = False
   
if __name__ == '__main__':
  fl.app(target=main)