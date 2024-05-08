'''
# Evaluación I - Métodos Cuantitativos
# Elaborado por: Giancarlos Hernaiz y Sebastián Medina

# Colas con retrabajo

# Enunciado: Modela un sistema de colas que permita retrabajos. Implementa un mecanismo en el que los clientes que no fueron atendidos correctamente puedan regresar al final de la cola. Calcula el impacto en el tiempo promedio en el sistema y la tasa de retrabajos.
'''
import flet as fl
import random

async def main(page: fl.Page) -> None:
  page.title = "Colas con Retrabajos"
  page.vertical_alignment = fl.MainAxisAlignment.CENTER
  page.horizontal_alignment = fl.MainAxisAlignment.CENTER
  page.window_center()
  page.window_resizable = False
  
  def route_change(e:fl.RouteChangeEvent) -> None:
    
    def show_values(e:fl.KeyboardType) -> None:
      global tiempo, carros
      try:
        carros = nro_carros.value.split(",")
        cola.value = carros
        tiempo = int(tiempo_simulacion.value)
        cola.update()
      except:
        pass
    
    def result(carros, tiempo) -> str:
      tiempo_carro = []
      for i in range(len(carros)):
        tiempo_carro.append(random.randint(1,3))
      retrabajos = random.randint(0, len(carros))
      tiempo_final = sum(tiempo_carro) + retrabajos
      
      tiempo_correjido = 0
      i = 0
      if tiempo_final > tiempo:
        while tiempo_correjido < tiempo:
          tiempo_correjido += tiempo_carro[i]
          i += 1
        return(f"No todos los carros de la cola pudieron ser atendidos en el tiempo dado. \n El tiempo total es: {tiempo_correjido}s.\n La tasa de retrabajos de {retrabajos}.")
      else:
        return(f"El tiempo total de los carros atendidos es de: {tiempo_final}\n La tasa de retrabajos es de {retrabajos}.") 
        
    nro_carros = fl.TextField(label="Ingrese el número de carros", on_submit=show_values)
    tiempo_simulacion = fl.TextField(label="Ingrese el tiempo de simulación", on_change=show_values)
    cola = fl.TextField(label='Cola',disabled=True, value=' ')
    
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
    
    if page.route == '/Datos':
      
      page.views.append(
        fl.View(
          route='/Datos',
          controls=[
            fl.AppBar(title=fl.Text("Datos"), bgcolor=fl.colors.GREY_900),
            
            fl.Column([
                
                fl.Text("Ingrese los datos", text_align=fl.MainAxisAlignment.CENTER, weight=500, size=70),
                
                fl.Text(f"Simularemos una gasolinera, donde cada carro representa un elemento de la cola, en este modelo existe una sola cola y cada estación va atendiendo a los carros dependiendo de su orden de llegada (FIFO). Cada carro tiene un tamaño random del tanque, por lo que su tiempo en la estación también es random. Siempre existe el riesgo de que al llegar a la estación el tipo no tenga vuelto 😠. En ese caso le toca volver a hacer la cola.", text_align=fl.TextAlign.CENTER, weight=500, size=20),
                
                fl.Column([
                  
                  fl.Row([
                    nro_carros, 
                    tiempo_simulacion
                  ], alignment=fl.MainAxisAlignment.SPACE_BETWEEN),
                                   
                  cola
                  
                ], alignment=fl.MainAxisAlignment.CENTER, horizontal_alignment=fl.CrossAxisAlignment.CENTER, spacing=20)
                
                ,fl.ElevatedButton(text="Calcular", scale=2, on_click = lambda _: page.go('/Tiempos'))
              ], alignment=fl.MainAxisAlignment.CENTER, horizontal_alignment=fl.CrossAxisAlignment.CENTER, spacing=60, width=1000)        

          ], 
          vertical_alignment = fl.MainAxisAlignment.CENTER,
          horizontal_alignment= fl.CrossAxisAlignment.CENTER,
          spacing=26
        )
      )
    
    if page.route == '/Tiempos':
      
      res = fl.TextField(value=result(carros, tiempo), multiline=True, read_only=True, height=740)
      
      page.views.append(
        fl.View(
          route='/Tiempos',
          controls=[
            fl.AppBar(title=fl.Text("Resultado"), bgcolor=fl.colors.GREY_900),
            fl.Column([
                fl.Text("Tiempo de la cola", text_align=fl.MainAxisAlignment.CENTER, weight=500, size=60),
                res,
                fl.ElevatedButton(text="Salir", scale=2, on_click= lambda _: page.go('/Datos'))
              ], alignment=fl.MainAxisAlignment.CENTER, horizontal_alignment=fl.CrossAxisAlignment.CENTER, spacing=40, width=800)            

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