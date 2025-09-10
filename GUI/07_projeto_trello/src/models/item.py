import itertools
import flet as ft
from store.data_store import DataStore

class Item(ft.Container):
    id_counter = itertools.count()

    def __init__(self, list, store: DataStore, item_text: str):
        self.item_id = next(Item.id_counter)
        self.store = store
        self.list = list
        self.item_text = item_text
        self.comments = []

        self.comment_field = ft.TextField(label="Comentar...", width=180, on_submit=self.add_comment)
        self.comment_section = ft.Column([], visible=False)

        self.card_item = ft.Card(
            content=ft.Column([
                ft.Row([
                    ft.Checkbox(label=self.item_text, width=180),
                    ft.IconButton(icon=ft.Icons.COMMENT, tooltip="Mostrar comentários", on_click=self.toggle_comments)
                ]),
                self.comment_field,
                self.comment_section
            ]),
            elevation=1,
            animate_elevation=300,
            on_hover=lambda e: self.card_item.update(elevation=6 if e.data == "true" else 1),
            data=self.list,
        )

        self.view = ft.Draggable(
            group="items",
            content=ft.DragTarget(
                group="items",
                content=self.card_item,
                on_accept=self.drag_accept,
                on_leave=self.drag_leave,
                on_will_accept=self.drag_will_accept,
            ),
            data=self,
        )

        super().__init__(content=self.view)

    def toggle_comments(self, e):
        self.comment_section.visible = not self.comment_section.visible
        self.update()

    def add_comment(self, e):
        if self.comment_field.value.strip():
            self.comments.append(self.comment_field.value)
            self.comment_section.controls.append(ft.Text(f"- {self.comment_field.value}", size=12))
            self.comment_field.value = ""
            self.page.snack_bar = ft.SnackBar(ft.Text("💬 Comentário adicionado"))
            self.page.snack_bar.open = True
            self.page.update()
        self.update()

    def drag_accept(self, e):
        src = self.page.get_control(e.src_id)
        if src.content.content == e.control.content:
            self.card_item.elevation = 1
            self.list.set_indicator_opacity(self, 0.0)
            e.control.update()
            return

        if src.data.list == self.list:
            self.list.add_item(chosen_control=src.data, swap_control=self)
            self.card_item.elevation = 1
            e.control.update()
            return

        self.list.add_item(src.data.item_text, swap_control=self)
        src.data.list.remove_item(src.data)
        self.list.set_indicator_opacity(self, 0.0)
        self.card_item.elevation = 1
        self.page.update()

    def drag_will_accept(self, e):
        if e.data == "true":
            self.list.set_indicator_opacity(self, 1.0)
        self.card_item.elevation = 20 if e.data == "true" else 1
        self.page.update()

    def drag_leave(self, e):
        self.list.set_indicator_opacity(self, 0.0)
        self.card_item.elevation = 1
        self.page.update()
