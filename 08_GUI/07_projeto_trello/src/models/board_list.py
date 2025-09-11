# models/board_list.py

import itertools
import flet as ft
from models.item import Item
from store.data_store import DataStore


class BoardList(ft.Container):
    id_counter = itertools.count()

    def __init__(
        self, board, store: DataStore, name: str, page: ft.Page, board_list_id=None
    ):
        super().__init__()
        self.page = page
        self.board = board
        self.store = store
        self.name = name
        self.board_list_id = (
            board_list_id if board_list_id is not None else next(BoardList.id_counter)
        )

        self.items = ft.Column([], scroll=ft.ScrollMode.AUTO, expand=True)
        self.title = ft.Text(
            self.name, size=16, weight=ft.FontWeight.BOLD, color="white"
        )
        self.add_item_field = ft.TextField(
            label="Novo card", on_submit=self.add_item_from_field
        )

        title_row = ft.Row(
            controls=[
                self.title,
                ft.Row(
                    [
                        ft.IconButton(
                            icon=ft.Icons.EDIT,
                            tooltip="Renomear lista",
                            on_click=self.edit_list,
                            icon_size=16,
                            height=28,
                        ),
                        ft.IconButton(
                            icon=ft.Icons.DELETE_FOREVER,
                            tooltip="Excluir lista",
                            on_click=self.delete_list,
                            icon_size=16,
                            height=28,
                        ),
                    ]
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )

        self.content = ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [title_row, self.add_item_field, self.items], tight=True, spacing=5
                ),
                padding=10,
            ),
            color="#004A3A",
            width=250,
        )
        self.data = self

    def to_dict(self):
        return {
            "board_list_id": self.board_list_id,
            "name": self.name,
        }

    def add_item_from_field(self, e):
        if self.add_item_field.value.strip():
            item = Item(self, self.store, self.add_item_field.value, self.page)
            self.add_item(item)  # Default save=True is correct here
            self.add_item_field.value = ""
            self.page.snack_bar = ft.SnackBar(
                ft.Text("📝 Card adicionado", color="white"), bgcolor="#003641"
            )
            self.page.snack_bar.open = True
            self.update()

    def add_item(self, item: Item, save=True):  # CORRIGIDO
        item.list = self
        if save:
            self.store.add_item(self.board_list_id, item)
        self.items.controls.append(item)
        self.update()

    # The rest of your methods for BoardList...
    def edit_list(self, e):
        def close_dlg(e):
            new_name = dialog_text.value.strip()
            if new_name:
                self.name = new_name
                self.title.value = new_name
                self.store.update_list(self, {"name": new_name})
                self.page.snack_bar = ft.SnackBar(
                    ft.Text("✅ Lista renomeada", color="white"), bgcolor="#003641"
                )
                self.page.snack_bar.open = True
            self.page.dialog.open = False
            self.page.update()

        dialog_text = ft.TextField(value=self.name, on_submit=close_dlg)
        edit_button = ft.ElevatedButton(
            "Salvar", on_click=close_dlg, bgcolor="#7DB61C", color="white"
        )
        dialog = ft.AlertDialog(
            title=ft.Text("Renomear Lista"),
            content=ft.Column([dialog_text, edit_button]),
            on_dismiss=lambda e: None,
        )
        self.page.dialog = dialog
        self.page.dialog.open = True
        self.page.update()

    def delete_list(self, e):
        def close_dlg(e):
            if e.control.text == "Sim":
                self.board.remove_list(self, e)
                self.page.snack_bar = ft.SnackBar(
                    ft.Text("🗑️ Lista excluída", color="white"), bgcolor="#003641"
                )
                self.page.snack_bar.open = True
            self.page.dialog.open = False
            self.page.update()

        dialog = ft.AlertDialog(
            title=ft.Text("Confirmar Exclusão"),
            content=ft.Text(f"Excluir a lista '{self.name}'?"),
            actions=[
                ft.TextButton(
                    "Não", on_click=close_dlg, style=ft.ButtonStyle(color="#00AE9D")
                ),
                ft.TextButton(
                    "Sim", on_click=close_dlg, style=ft.ButtonStyle(color="#00AE9D")
                ),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        self.page.dialog = dialog
        self.page.dialog.open = True
        self.page.update()

    def remove_item(self, item: Item):
        self.items.controls.remove(item)
        self.store.remove_item(self.board_list_id, item.item_id)
        self.update()
