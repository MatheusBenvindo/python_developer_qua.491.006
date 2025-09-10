# views/dashboard_view.py

import flet as ft


def dashboard_view(page):
    user = page.client_storage.get("user")

    def logout(e):
        page.client_storage.clear()
        page.go("/login")

    return ft.Column(
        [
            ft.Text(f"Bem-vindo, {user}!", size=24, color="black"),
            ft.Text("Este é seu painel estilo Sicoob", color="black"),
            ft.ElevatedButton(
                "Sair",
                on_click=logout,
                bgcolor="#7DB61C",
                color="black",  # COR ATUALIZADA
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True,
    )
