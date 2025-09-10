# models/board.py

import itertools
import flet as ft
from models.board_list import BoardList
from store.data_store import DataStore


class Board(ft.Container):
    id_counter = itertools.count()

    def __init__(self, app, store: DataStore, name: str, page: ft.Page, board_id=None):
        super().__init__()
        self.page = page
        self.board_id = board_id if board_id is not None else next(Board.id_counter)
        self.store = store
        self.app = app
        self.name = name

        self.add_list_button = ft.FloatingActionButton(
            icon=ft.Icons.ADD,
            text="Adicionar lista",
            height=30,
            bgcolor="#7DB61C",
            on_click=self.create_list,
        )

        self.board_lists = ft.Row(
            controls=[self.add_list_button],
            vertical_alignment=ft.CrossAxisAlignment.START,
            scroll=ft.ScrollMode.AUTO,
            expand=True,
            # Initial width, will be resized
            width=(self.app.page.width - 310 if self.app and self.app.page else 800),
            height=(self.app.page.height - 95 if self.app and self.app.page else 600),
        )

        super().__init__(
            content=self.board_lists,
            data=self,
            margin=ft.margin.all(0),
            padding=ft.padding.only(top=10, right=0),
            height=(self.app.page.height if self.app and self.app.page else 600),
        )

    def to_dict(self):
        return {
            "board_id": self.board_id,
            "name": self.name,
        }

    @classmethod
    def from_dict(cls, data):
        # This is primarily for type consistency, not used to create UI
        board = cls.__new__(cls)
        board.board_id = data["board_id"]
        board.name = data["name"]
        return board

    def create_list(self, e):
        dialog_text = ft.TextField(label="Nome da nova lista", autofocus=True)
        dialog = ft.AlertDialog(
            title=ft.Text("Nova Lista"),
            content=dialog_text,
            on_dismiss=lambda e: print("LOG: Diálogo dispensado."),
        )

        def close_dlg(e):
            if dialog_text.value.strip():
                new_list = BoardList(self, self.store, dialog_text.value, self.page)
                self.add_list(new_list)  # Default save=True is correct here
                self.page.snack_bar = ft.SnackBar(
                    ft.Text("📂 Lista criada", color="white"), bgcolor="#003641"
                )
                self.page.snack_bar.open = True
            self.page.overlay.remove(dialog)
            self.page.update()

        def cancel_dlg(e):
            self.page.overlay.remove(dialog)
            self.page.update()

        create_button = ft.ElevatedButton(
            text="Criar", bgcolor="#7DB61C", on_click=close_dlg, color="white"
        )
        cancel_button = ft.TextButton(
            "Cancelar", on_click=cancel_dlg, style=ft.ButtonStyle(color="#00AE9D")
        )
        dialog.actions = [cancel_button, create_button]
        self.page.overlay.append(dialog)
        dialog.open = True
        self.page.update()

    def remove_list(self, list_to_remove: BoardList, e):
        self.board_lists.controls.remove(list_to_remove)
        self.store.remove_list(self.board_id, list_to_remove.board_list_id)
        self.page.update()

    def add_list(self, list_to_add: BoardList, save=True):  # CORRIGIDO
        self.board_lists.controls.insert(-1, list_to_add)
        if save:
            self.store.add_list(self.board_id, list_to_add)
        self.page.update()
