import flet as ft
from views.login_view import login_view
from views.app_layout import AppLayout
from store.memory_store import InMemoryStore

def main(page: ft.Page):
    page.title = "Trello Sicoob"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = "#007A33"
    page.fonts = {"Pacifico": "Pacifico-Regular.ttf"}

    store = InMemoryStore()

    def on_login_success(user, role):
        page.client_storage.set("user", user)
        page.client_storage.set("role", role)
        page.clean()
        app = AppLayout(page, store)
        page.add(app)
        app.initialize()

    if page.client_storage.contains_key("user"):
        app = AppLayout(page, store)
        page.add(app)
        app.initialize()
    else:
        page.add(login_view(page, on_login_success))

ft.app(target=main)
