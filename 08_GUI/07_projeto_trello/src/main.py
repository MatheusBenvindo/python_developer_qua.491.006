# main.py

import flet as ft
from views.login_view import login_view
from views.app_layout import AppLayout
from store.pickle_store import PickleStore


def main(page: ft.Page):
    page.title = "Trello Sicoob"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = "#ffffff"  # COR ATUALIZADA
    page.fonts = {"Pacifico": "Pacifico-Regular.ttf"}

    store = PickleStore()

    def route_change(route):
        page.views.clear()

        if page.route == "/":
            if page.client_storage.contains_key("user"):
                app = AppLayout(store, page)
                page.views.append(ft.View("/", [app], bgcolor=page.bgcolor))
            else:
                page.go("/login")

        elif page.route == "/login":

            def on_login_success(user, role):
                page.client_storage.set("user", user)
                page.client_storage.set("role", role)
                page.go("/")

            page.views.append(
                ft.View(
                    "/login", [login_view(page, on_login_success)], bgcolor=page.bgcolor
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    # Define a rota inicial
    if page.client_storage.contains_key("user"):
        page.go("/")
    else:
        page.go("/login")


# Inicia a aplicação
ft.app(target=main, assets_dir="assets")
