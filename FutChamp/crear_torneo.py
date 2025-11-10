import flet as ft
from mesclar_equipos import mesclar_equipos

def crear_torneo_app(page: ft.Page):
    page.title = "Crear Torneo"
    page.window_width = 600
    page.window_height = 700
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    tipo_torneo = ft.Ref[ft.Dropdown]()
    num_equipos = ft.Ref[ft.TextField]()
    equipos = []
    campos_equipos = []

    dropdown_tipo = ft.Dropdown(
        label="Tipo de Torneo",
        options=[
            ft.dropdown.Option("Liga"),
            ft.dropdown.Option("Eliminación Directa")
        ],
        ref=tipo_torneo,
        width=300
    )

    campo_num_equipos = ft.TextField(
        label="Número de Equipos (mínimo 2)",
        value="2",
        ref=num_equipos,
        width=300,
        keyboard_type=ft.KeyboardType.NUMBER
    )

    contenedor_equipos = ft.Column(scroll=ft.ScrollMode.AUTO, height=300)

    def actualizar_campos_equipos(e):
        try:
            num = int(campo_num_equipos.value)
            if num < 2:
                num = 2
                campo_num_equipos.value = "2"
            equipos.clear()
            campos_equipos.clear()
            contenedor_equipos.controls.clear()
            for i in range(num):
                campo = ft.TextField(label=f"Nombre Equipo {i+1}", width=300)
                campos_equipos.append(campo)
                contenedor_equipos.controls.append(campo)
            page.update()
        except ValueError:
            pass

    boton_generar = ft.ElevatedButton(
        "Generar Campos de Equipos",
        on_click=actualizar_campos_equipos,
        width=300
    )

    def crear_torneo(e):
        equipos.clear()
        for campo in campos_equipos:
            if campo.value.strip():
                equipos.append(campo.value.strip())
        if len(equipos) < 2:
            page.snack_bar = ft.SnackBar(ft.Text("Debe ingresar al menos 2 equipos"))
            page.snack_bar.open = True
            page.update()
            return
        equipos_mezclados = mesclar_equipos(equipos.copy())
        enfrentamientos = []
        for i in range(0, len(equipos_mezclados), 2):
            if i + 1 < len(equipos_mezclados):
                enfrentamientos.append(f"{equipos_mezclados[i]} contra {equipos_mezclados[i+1]}")
            else:
                enfrentamientos.append(f"{equipos_mezclados[i]} (sin pareja)")
        page.clean()
        page.add(
            ft.Column([
                ft.Text("Enfrentamientos del Torneo", size=30, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                ft.Column([ft.Text(enfrentamiento, size=18) for enfrentamiento in enfrentamientos], spacing=10),
                ft.ElevatedButton("Volver al Menú Principal", on_click=lambda e: volver_menu(e), width=300)
            ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20)
        )
        page.update()

    def volver_menu(e):
        page.clean()
        page.title = "FutChampions"
        page.window_width = 400
        page.window_height = 600

        def abrir_crear_torneo(e):
            page.clean()
            crear_torneo_app(page)

        def abrir_marcador(e):
            page.clean()
            from marcador import marcador_app
            marcador_app(page)

        boton_crear = ft.ElevatedButton("Crear Torneo", width=250, on_click=abrir_crear_torneo)
        boton_seguir = ft.ElevatedButton("Seguir Torneo", width=250)
        boton_marcador = ft.ElevatedButton("Marcador", width=250, on_click=abrir_marcador)
        boton_historial = ft.ElevatedButton("Historial", width=250)

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
        page.update()
        
    boton_crear = ft.ElevatedButton(
        "Crear Torneo",
        on_click=crear_torneo,
        width=300
    )

    page.add(
        ft.Column([
            ft.Text("Crear Torneo", size=30, weight=ft.FontWeight.BOLD),
            dropdown_tipo,
            campo_num_equipos,
            boton_generar,
            ft.Text("Equipos:", size=18),
            contenedor_equipos,
            boton_crear
        ], alignment=ft.MainAxisAlignment.START, horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20)
    )
