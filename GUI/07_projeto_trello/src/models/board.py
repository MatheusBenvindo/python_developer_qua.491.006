import itertools
import flet as ft
from .board_list import BoardList
from store.data_store import DataStore

class Board(ft.Container):
    id_counter = itertools.count()

    def __init__(self, app, store: DataStore, name: str, page: ft.Page):
        self.page = page
        self.board_id = next(Board.id_counter)
        self.store = store
        self.app = app
        self.name = name

        self.add_list_button = ft.FloatingActionButton(
            icon=ft.Icons.ADD,
            text="Adicionar lista",
            height=30,
            bgcolor="#00A859",
            on_click=self.create_list
        )

        self.board_lists = ft.Row(
            controls=[self.add_list_button],
            vertical_alignment=ft.CrossAxisAlignment.START,
            scroll=ft.ScrollMode.AUTO,
            expand=True,
            width=(self.app.page.width - 310),
            height=(self.app.page.height - 95),
        )

        for l in self.store.get_lists_by_board(self.board_id):
            self.add_list(l)

        super().__init__(
            content=self.board_lists,
            data=self,
            margin=ft.margin.all(0),
            padding=ft.padding.only(top=10, right=0),
            height=self.app.page.height,
        )

    def resize(self, nav_rail_extended, width, height):
        self.board_lists.width = (width - 310) if nav_rail_extended else (width - 50)
        self.height = height
        self.update()

    def create_list(self, e):
        if self.page.client_storage.get("role") == "guest":
            self.page.snack_bar = ft.SnackBar(ft.Text("Visitantes não podem criar listas"))
            self.page.snack_bar.open = True
            return

        def close_dlg(e):
            if dialog_text.value.strip():
                new_list = BoardList(self, self.store, dialog_text.value, self.page)
                self.add_list(new_list)
                self.page.snack_bar = ft.SnackBar(ft.Text("📂 Lista criada"))
                self.page.snack_bar.open = True
            self.page.close(dialog)

        dialog_text = ft.TextField(label="Nome da nova lista", on_submit=close_dlg)
        create_button = ft.ElevatedButton(text="Criar", bgcolor="#00A859", on_click=close_dlg)

        dialog = ft.AlertDialog(
            title=ft.Text("Nova Lista"),
            content=ft.Column([dialog_text, create_button]),
            on_dismiss=lambda e: None
        )
        self.page.open(dialog)
        dialog_text.focus()

    def remove_list(self, list: BoardList, e):
        self.board_lists.controls.remove(list)
        self.store.remove_list(self.board_id, list.board_list_id)
        self.page.update()

    def add_list(self, list):
        self.board_lists.controls.insert(-1, list)
        self.store.add_list(self.board_id, list)
        self.page.update()
