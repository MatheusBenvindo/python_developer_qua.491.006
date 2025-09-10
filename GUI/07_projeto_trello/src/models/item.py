# models/item.py

import itertools
import flet as ft
from store.data_store import DataStore


class Item(ft.Container):
    id_counter = itertools.count()

    def __init__(
        self,
        list_obj,
        store: DataStore,
        item_text: str,
        page: ft.Page,
        item_id=None,
        comments=None,
    ):
        super().__init__()
        self.item_id = item_id if item_id is not None else next(Item.id_counter)
        self.store = store
        self.list = list_obj
        self.item_text = item_text
        self.comments = comments if comments is not None else []
        self.page = page
        self.checkbox = ft.Checkbox(label=self.item_text, value=False)
        self.comment_field = ft.TextField(
            label="Comentar...", on_submit=self.add_comment, text_size=12
        )
        self.comment_section = ft.Column(
            [ft.Text(f"- {c}", size=12) for c in self.comments], visible=False
        )

        action_buttons = ft.Row(
            controls=[
                ft.IconButton(
                    icon=ft.Icons.EDIT,
                    tooltip="Editar item",
                    on_click=self.edit_item,
                    icon_size=16,
                    height=28,
                ),
                ft.IconButton(
                    icon=ft.Icons.DELETE_FOREVER,
                    tooltip="Excluir item",
                    on_click=self.delete_item,
                    icon_size=16,
                    height=28,
                ),
                ft.IconButton(
                    icon=ft.Icons.COMMENT,
                    tooltip="Comentários",
                    on_click=self.toggle_comments,
                    icon_size=16,
                    height=28,
                ),
            ],
            spacing=0,
        )

        self.card_item = ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.Row(
                            [self.checkbox, action_buttons],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        ),
                        self.comment_field,
                        self.comment_section,
                    ]
                ),
                padding=ft.padding.only(left=10, right=5, top=5, bottom=5),
            ),
            elevation=1,
            data=self.list,
        )

        self.content = ft.Draggable(
            group="items",
            content=ft.DragTarget(
                group="items",
                content=self.card_item,
                on_accept=self.drag_accept,
            ),
            data=self,
        )

    def to_dict(self):
        return {
            "item_id": self.item_id,
            "item_text": self.item_text,
            "comments": self.comments,
        }

    def edit_item(self, e):
        def close_dlg(e):
            new_text = dialog_text.value.strip()
            if new_text:
                self.item_text = new_text
                self.checkbox.label = new_text
                self.store.update_item(self, {"item_text": new_text})  # UPDATED
                self.page.snack_bar = ft.SnackBar(
                    ft.Text("✅ Item atualizado", color="white"), bgcolor="#003641"
                )
                self.page.snack_bar.open = True
            self.page.dialog.open = False
            self.page.update()

        dialog_text = ft.TextField(value=self.item_text, on_submit=close_dlg)
        edit_button = ft.ElevatedButton(
            "Salvar", on_click=close_dlg, bgcolor="#7DB61C", color="white"
        )
        dialog = ft.AlertDialog(
            title=ft.Text("Editar Item"),
            content=ft.Column([dialog_text, edit_button]),
            on_dismiss=lambda e: None,
        )
        self.page.dialog = dialog
        self.page.dialog.open = True
        self.page.update()

    def delete_item(self, e):
        def close_dlg(e):
            if e.control.text == "Sim":
                self.list.remove_item(self)
                self.page.snack_bar = ft.SnackBar(
                    ft.Text("🗑️ Item excluído", color="white"), bgcolor="#003641"
                )
                self.page.snack_bar.open = True
            self.page.dialog.open = False
            self.page.update()

        dialog = ft.AlertDialog(
            title=ft.Text("Confirmar Exclusão"),
            content=ft.Text(f"Deseja excluir '{self.item_text}'?"),
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

    def toggle_comments(self, e):
        self.comment_section.visible = not self.comment_section.visible
        self.update()

    def add_comment(self, e):
        if self.comment_field.value.strip():
            comment_text = self.comment_field.value.strip()
            self.comments.append(comment_text)
            self.comment_section.controls.append(ft.Text(f"- {comment_text}", size=12))
            self.comment_field.value = ""
            self.store.update_item(self, {"comments": self.comments})  # UPDATED
            self.page.snack_bar = ft.SnackBar(
                ft.Text("💬 Comentário adicionado", color="white"), bgcolor="#003641"
            )
            self.page.snack_bar.open = True
            self.update()

    def drag_accept(self, e):
        src = self.page.get_control(e.src_id)
        if src.data.list == self.list:
            return

        # Remove from old list's data
        src.data.list.store.remove_item(src.data.list.board_list_id, src.data.item_id)
        # Add to new list's data
        self.list.store.add_item(self.list.board_list_id, src.data)

        # Update UI
        src.data.list.items.controls.remove(src.data)
        self.list.items.controls.append(src.data)
        src.data.list = self.list
        self.page.update()
