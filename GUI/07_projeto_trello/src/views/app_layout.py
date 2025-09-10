import flet as ft
from views.sidebar import Sidebar
from views.dashboard_view import dashboard_view
from views.stats_view import stats_view

class AppLayout(ft.Row):
    def __init__(self, page: ft.Page, store, **kwargs):
        self.page = page
        self.store = store

        self.sidebar = Sidebar(self, self.store)
        self.sidebar.page = self.page
        self.sidebar.sync_board_destinations()

        self.active_view = ft.Container()

        super().__init__(
            controls=[self.sidebar, self.active_view],
            expand=True,
            **kwargs
        )

    def initialize(self):
        self.page.views.clear()
        self.page.views.append(ft.View("/", [self], bgcolor="#007A33"))
        self.set_all_boards_view()
        self.page.update()

    def set_all_boards_view(self):
        self.active_view.content = ft.Text("📁 Todos os boards", size=20, color="white")
        self.page.update()

    def set_board_view(self, board_id):
        board = self.store.get_board(board_id)
        self.active_view.content = board
        self.page.update()

    def set_members_view(self):
        self.active_view.content = ft.Text("👥 Membros", size=20, color="white")
        self.page.update()

    def set_dashboard_view(self):
        self.active_view.content = dashboard_view(self.page)
        self.page.update()

    def set_stats_view(self):
        self.active_view.content = stats_view(self.store)
        self.page.update()

    def hydrate_all_boards_view(self):
        self.sidebar.sync_board_destinations()
        self.set_all_boards_view()
