import flet as ft
from store.data_store import DataStore

class Sidebar(ft.Container):
    def __init__(self, app_layout, store: DataStore):
        self.store = store
        self.app_layout = app_layout
        self.nav_rail_visible = True

        self.top_nav_items = [
            ft.NavigationRailDestination(label="Boards", icon=ft.Icons.BOOK_OUTLINED),
            ft.NavigationRailDestination(label="Members", icon=ft.Icons.PERSON),
        ]

        self.top_nav_rail = ft.NavigationRail(
            selected_index=None,
            label_type=ft.NavigationRailLabelType.ALL,
            on_change=self.top_nav_change,
            destinations=self.top_nav_items,
            bgcolor="#004B23",
            extended=True,
            height=110,
        )

        self.bottom_nav_rail = ft.NavigationRail(
            selected_index=None,
            label_type=ft.NavigationRailLabelType.ALL,
            on_change=self.bottom_nav_change,
            extended=True,
            expand=True,
            bgcolor="#004B23",
        )

        super().__init__(
            content=ft.Column([self.top_nav_rail, self.bottom_nav_rail]),
            padding=ft.padding.all(15),
            width=250,
            bgcolor="#004B23",
            visible=self.nav_rail_visible,
        )

    def sync_board_destinations(self):
        boards = self.store.get_boards()
        self.bottom_nav_rail.destinations = []
        for i, b in enumerate(boards):
            self.bottom_nav_rail.destinations.append(
                ft.NavigationRailDestination(label=b.name, icon=ft.Icons.CHEVRON_RIGHT_OUTLINED)
            )

    def top_nav_change(self, e):
        index = e.control.selected_index
        self.bottom_nav_rail.selected_index = None
        self.top_nav_rail.selected_index = index
        self.page.route = "/boards" if index == 0 else "/members"
        self.page.update()

    def bottom_nav_change(self, e):
        index = e.control.selected_index
        self.top_nav_rail.selected_index = None
        self.bottom_nav_rail.selected_index = index
        self.page.route = f"/board/{index}"
        self.page.update()
