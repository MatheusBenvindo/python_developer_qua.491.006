import itertools
import flet as ft
from .item import Item
from store.data_store import DataStore

class BoardList(ft.Container):
    id_counter = itertools.count()

    def __init__(self, board, store: DataStore, name: str, page: ft.Page, color="#00C389"):
        self.page = page
        self.board = board
        self.store = store
        self.name = name
        self.color = color
        self.board_list_id = next(BoardList.id_counter)
        self.items = []

        self.title = ft.Text(self.name, size=16, weight=ft.FontWeight.BOLD, color="white")
        self.add_item_field = ft.TextField(label="Novo card", width=180, on_submit=self.add_item_from_field)

        self.item_column = ft.Column()

        for item in self.store.get_items(self.board_list_id):
            self.add_item(item)

        self.card = ft.Card(
            content=ft.Column([
                self.title,
                self.add_item_field,
                self.item_column
            ]),
            bgcolor=self.color,
            elevation=2,
            width=200,
            height=300,
            data=self
        )

        super().__init__(content=self.card)

    def add_item_from_field(self, e):
        if self.add_item_field.value.strip():
            item = Item(self, self.store, self.add_item_field.value)
            self.add_item(item)
            self.store.add_item(self.board_list_id, item)
            self.add_item_field.value = ""
            self.page.snack_bar = ft.SnackBar(ft.Text("📝 Card adicionado"))
            self.page.snack_bar.open = True
            self.page.update()

    def add_item(self, item, swap_control=None):
        if swap_control:
            index = self.item_column.controls.index(swap_control)
            self.item_column.controls.insert(index, item)
        else:
            self.item_column.controls.append(item)
        self.page.update()

    def remove_item(self, item):
        self.item_column.controls.remove(item)
        self.store.remove_item(self.board_list_id, item.item_id)
        self.page.update()

    def set_indicator_opacity(self, item, opacity: float):
        item.opacity = opacity
        self.page.update()
