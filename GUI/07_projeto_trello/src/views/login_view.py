import flet as ft
from models.user import User
from utils.user_db import validate_user

def login_view(page, on_success):
    def try_login(e):
        if validate_user(username.value, password.value):
            page.client_storage.set("user", username.value)
            page.client_storage.set("role", role.value)
            page.snack_bar = ft.SnackBar(ft.Text("✅ Login realizado"))
            page.snack_bar.open = True
            on_success(username.value, role.value)
        else:
            page.dialog = ft.AlertDialog(title=ft.Text("Credenciais inválidas"))
            page.dialog.open = True
            page.update()

    username = ft.TextField(label="Usuário", width=300)
    password = ft.TextField(label="Senha", password=True, can_reveal_password=True, width=300)
    role = ft.Dropdown(label="Tipo de usuário", options=[
        ft.dropdown.Option("admin"),
        ft.dropdown.Option("member"),
        ft.dropdown.Option("guest")
    ], value="member")
    login_btn = ft.ElevatedButton("Entrar", on_click=try_login, style=ft.ButtonStyle(bgcolor={"": "#00A859"}))

    return ft.Column(
        controls=[
            ft.Text("Login Sicoob", size=30, color="white"),
            username,
            password,
            role,
            login_btn
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )
