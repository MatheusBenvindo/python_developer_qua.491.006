import flet as ft

#estrutura padrão de um app flet
def main(page: ft.Page):
    counter = ft.Text("0", size=50, data=0)

    page.add(
        ft.SafeArea(

            ft.Container(ft.Text("Hello, Flet!", size=50), alignment=ft.alignment.center),
            expand=True,
        )
    )


ft.app(target=main)
