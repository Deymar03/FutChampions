import flet as ft


def marcador_app(page: ft.Page):
    page.title = "Marcador FutChamp"
    page.window_width = 500
    page.window_height = 350
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER


    nombre_local = ft.TextField(label="Equipo Local", value="Local")
    nombre_visitante = ft.TextField(label="Equipo Visitante", value="Visitante")

    # Puntajes
    puntaje_local = ft.Ref[ft.Text]()
    puntaje_visitante = ft.Ref[ft.Text]()
    texto_local = ft.Text("0", size=50, ref=puntaje_local)
    texto_visitante = ft.Text("0", size=50, ref=puntaje_visitante)

    # Funciones para puntajes
    def sumar_local(e):
        texto_local.value = str(int(texto_local.value) + 1)
        page.update()

    def restar_local(e):
        texto_local.value = str(max(0, int(texto_local.value) - 1))  # no permite negativos
        page.update()

    def sumar_visitante(e):
        texto_visitante.value = str(int(texto_visitante.value) + 1)
        page.update()

    def restar_visitante(e):
        texto_visitante.value = str(max(0, int(texto_visitante.value) - 1))
        page.update()

    def reiniciar_partido(e):
        texto_local.value = "0"
        texto_visitante.value = "0"
        page.update()

    # Layout del marcador
    page.add(
        ft.Row(
            [
                ft.Column([nombre_local, texto_local, ft.Row([
                    ft.ElevatedButton("+", on_click=sumar_local, width=50),
                    ft.ElevatedButton("-", on_click=restar_local, width=50)
                ], spacing=10)], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                
                ft.Column([nombre_visitante, texto_visitante, ft.Row([
                    ft.ElevatedButton("+", on_click=sumar_visitante, width=50),
                    ft.ElevatedButton("-", on_click=restar_visitante, width=50)
                ], spacing=10)], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=50
        ),
        ft.Divider(height=30),
        ft.Row([ft.ElevatedButton("Reiniciar Partido", on_click=reiniciar_partido)], alignment=ft.MainAxisAlignment.CENTER)
    )

# Ejecutar marcador
# redireciona para ejecutar el marcador 
if __name__ == "__main__":
    ft.app(target=marcador_app)
