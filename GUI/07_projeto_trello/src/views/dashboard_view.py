import flet as ft

def dashboard_view(page):
    user = page.client_storage.get("user")

    return ft.Column(
        controls=[
            ft.Text(f"Bem-vindo, {user}!", size=24, color="white"),
            ft.Text("Este é seu painel estilo Sicoob", color="white"),
            ft.ElevatedButton("Sair", on_click=lambda e: logout(page), style=ft.ButtonStyle(bgcolor={"": "#004B23"}))
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

def logout(page):
    page.client_storage.clear()
    page.go("/")
