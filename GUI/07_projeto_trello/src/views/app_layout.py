# views/app_layout.py

import flet as ft
from models.board import Board
from models.board_list import BoardList
from models.item import Item
from views.sidebar import Sidebar
from views.dashboard_view import dashboard_view
from views.stats_view import stats_view


# CLASSE DE DIÁLOGO SIMPLIFICADA
class CreateBoardDialog(ft.AlertDialog):
    def __init__(self, app_layout):
        super().__init__()
        self.app_layout = app_layout
        self.modal = True
        self.title = ft.Text("Novo Board")
        self.dialog_text = ft.TextField(label="Nome do novo board", width=300)
        self.create_button = ft.ElevatedButton(
            "Criar", on_click=self._on_create_click, bgcolor="#7DB61C", color="white"
        )
        self.cancel_button = ft.TextButton("Cancelar", on_click=self._on_cancel_click)

        self.content = self.dialog_text
        self.actions = [self.cancel_button, self.create_button]

    def _on_cancel_click(self, e):
        self.open = False
        self.app_layout.page.update()

    def _on_create_click(self, e):
        board_name = self.dialog_text.value.strip()
        page = self.app_layout.page
        if not board_name:
            page.snack_bar = ft.SnackBar(
                ft.Text("❗ Informe o nome do board", color="white"), bgcolor="#003641"
            )
            page.snack_bar.open = True
            page.update()
            return

        store = self.app_layout.store
        # Create a full Board object for the UI
        new_board = Board(app=self.app_layout, store=store, name=board_name, page=page)
        store.add_board(new_board)
        self.app_layout.sidebar.sync_board_destinations()

        page.snack_bar = ft.SnackBar(
            ft.Text(f"🎉 Board '{board_name}' criado!", color="white"),
            bgcolor="#003641",
        )
        page.snack_bar.open = True

        self.open = False
        page.update()


class AppLayout(ft.Row):
    def __init__(self, store, page: ft.Page, **kwargs):
        super().__init__(**kwargs)
        self.store = store
        self.page = page
        self.boards = {}  # To hold the UI Board objects

        self.sidebar = Sidebar(self, self.store)
        self.active_view = ft.Container(expand=True, padding=20)
        self.controls = [self.sidebar, self.active_view]
        self.expand = True

        self.sidebar.page = self.page
        self.hydrate_data()  # Load data and create UI
        self.sidebar.sync_board_destinations()
        self.set_all_boards_view()

    def open_create_board_dialog(self, e):
        dialog = CreateBoardDialog(self)
        self.page.overlay.append(dialog)
        dialog.open = True
        self.page.update()

    def set_all_boards_view(self):
        create_button = ft.ElevatedButton(
            "Criar Novo Board",
            icon=ft.Icons.ADD,
            on_click=self.open_create_board_dialog,
            style=ft.ButtonStyle(bgcolor={"": "#003641"}, color={"": "black"}),
        )

        self.active_view.content = ft.Column(
            [
                ft.Row(
                    [
                        ft.Text(
                            "📁 Todos os Boards",
                            size=20,
                            weight=ft.FontWeight.BOLD,
                            color="white",
                        ),
                        create_button,
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.Text(
                    "Selecione um board na barra lateral ou crie um novo para começar.",
                    color="white",
                ),
            ]
        )
        self.page.update()  # Ensure view updates

    def hydrate_data(self):
        # Create UI objects from stored data
        for board_data in self.store.get_boards():
            board = Board(
                app=self,
                store=self.store,
                page=self.page,
                name=board_data["name"],
                board_id=board_data["board_id"],
            )
            self.boards[board.board_id] = board

            for list_data in self.store.get_lists_by_board(board.board_id):
                list_obj = BoardList(
                    board=board,
                    store=self.store,
                    page=self.page,
                    name=list_data["name"],
                    board_list_id=list_data["board_list_id"],
                )
                board.add_list(list_obj, save=False)  # Add to UI without re-saving

                for item_data in self.store.get_items(list_obj.board_list_id):
                    item_obj = Item(
                        list_obj=list_obj,
                        store=self.store,
                        page=self.page,
                        item_text=item_data["item_text"],
                        item_id=item_data["item_id"],
                        comments=item_data["comments"],
                    )
                    list_obj.add_item(
                        item_obj, save=False
                    )  # Add to UI without re-saving

    def set_board_view(self, board_id):
        board = self.boards.get(board_id)
        if board:
            self.active_view.content = board
        self.page.update()

    def set_dashboard_view(self):
        self.active_view.content = dashboard_view(self.page)
        self.page.update()

    def set_stats_view(self):
        self.active_view.content = stats_view(self.store)
        self.page.update()
