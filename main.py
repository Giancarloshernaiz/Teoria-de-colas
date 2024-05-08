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
  
  def route_change(e:fl.RouteChangeEvent) -> None:
    
    page.views.clear()
    
    page.views.append(
      fl.View(
        route='/',
        controls=[
          fl.Column([
            fl.Text("Colas con retrabajo", text_align=fl.MainAxisAlignment.CENTER, weight=500, size=70),
            fl.ElevatedButton(text="Iniciar", scale=2, on_click=lambda _:page.go('/Datos')),
            fl.Row([
              fl.Text("Elaborado por: Giancarlos Hernaiz y Sebastian Medina", text_align=fl.MainAxisAlignment.START, weight=300, size=20), 
              fl.Text("Evaluación I - Métodos cuantitativos", text_align=fl.MainAxisAlignment.END, weight=300, size=20), 
            ], alignment=fl.MainAxisAlignment.SPACE_AROUND)
          ], alignment=fl.MainAxisAlignment.CENTER, horizontal_alignment=fl.CrossAxisAlignment.CENTER, spacing=120)      
        ], 
        vertical_alignment = fl.MainAxisAlignment.CENTER,
        horizontal_alignment= fl.CrossAxisAlignment.CENTER,
        spacing=26
      )
    )
          
    page.update()
  
  def view_pop(e:fl.ViewPopEvent) -> None:
    page.views.pop()
    top_view: fl.View = page.views[-1]
    page.go(top_view.route)
    
  page.on_route_change = route_change
  page.on_view_pop = view_pop  
  page.go(page.route)
  
if __name__ == '__main__':
  fl.app(target=main)