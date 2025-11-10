import flet as ft
from marcador import marcador_app  
from marcador import marcador_app
from crear_torneo import crear_torneo_app

def main(page: ft.Page):
    page.title = "FutChampions"
    page.window_width = 400
    page.window_height = 600

    # menú principal
    def abrir_crear_torneo(e):
        page.clean()
        crear_torneo_app(page)

    boton_crear = ft.ElevatedButton("Crear Torneo", width=250, on_click=abrir_crear_torneo)
    boton_seguir = ft.ElevatedButton("Seguir Torneo", width=250)

    #abrir el marcador
    def abrir_marcador(e):
       

        page.clean()
        marcador_app(page)  
        marcador_app(page)

    boton_marcador = ft.ElevatedButton("Marcador", width=250, on_click=abrir_marcador)
    boton_historial = ft.ElevatedButton("Historial", width=250)

# Contenedor
    fondo = ft.Container(
        expand=True,
        bgcolor="green",
        content=ft.Column(
            [
                ft.Text("🔥🐐 FutChampions🐐 🔥", size=30, weight=ft.FontWeight.BOLD, color="white", text_align=ft.TextAlign.CENTER),
                boton_crear,
                boton_seguir,
                boton_marcador,
                boton_historial
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
    )

    page.add(fondo)


ft.app(target=main)
