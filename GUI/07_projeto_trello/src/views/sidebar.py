# views/sidebar.py

import flet as ft
from store.data_store import DataStore


class Sidebar(ft.Container):
    def __init__(self, app_layout, store: DataStore):
        super().__init__()
        self.store = store
        self.app_layout = app_layout

        # ESTILO DO TEXTO PARA OS ITENS DA NAVEGAÇÃO
        label_style = ft.TextStyle(color="white")

        self.top_nav_items = [
            ft.NavigationRailDestination(
                label="Todos os Boards",
                icon=ft.Icons.FOLDER_COPY_OUTLINED,
                selected_icon=ft.Icons.FOLDER_COPY,
            ),
            ft.NavigationRailDestination(
                label="Dashboard",
                icon=ft.Icons.DASHBOARD_OUTLINED,
                selected_icon=ft.Icons.DASHBOARD,
            ),
            ft.NavigationRailDestination(
                label="Estatísticas",
                icon=ft.Icons.INSERT_CHART_OUTLINED,
                selected_icon=ft.Icons.INSERT_CHART,
            ),
        ]

        self.top_nav_rail = ft.NavigationRail(
            selected_index=0,
            label_type=ft.NavigationRailLabelType.ALL,
            on_change=self.top_nav_change,
            destinations=self.top_nav_items,
            bgcolor="#49479D",
            extended=True,
            height=200,
            # ADICIONADO PARA MUDAR A COR DO TEXTO
            selected_label_text_style=label_style,
            unselected_label_text_style=label_style,
        )

        self.bottom_nav_rail = ft.NavigationRail(
            selected_index=None,
            label_type=ft.NavigationRailLabelType.ALL,
            on_change=self.bottom_nav_change,
            extended=True,
            expand=True,
            bgcolor="#49479D",
            destinations=[],
            # ADICIONADO PARA MUDAR A COR DO TEXTO
            selected_label_text_style=label_style,
            unselected_label_text_style=label_style,
        )

        self.content = ft.Column(
            [self.top_nav_rail, self.bottom_nav_rail], spacing=20, expand=True
        )
        self.padding = ft.padding.all(5)
        self.width = 250
        self.bgcolor = "#49479D"

    def sync_board_destinations(self):
        boards = self.store.get_boards()
        self.bottom_nav_rail.destinations = []
        for board_data in boards:
            self.bottom_nav_rail.destinations.append(
                ft.NavigationRailDestination(
                    label=board_data["name"],
                    icon=ft.Icons.CHEVRON_RIGHT_OUTLINED,
                    selected_icon=ft.Icons.CHEVRON_RIGHT,
                    data=board_data["board_id"],
                )
            )
        if self.page:
            self.page.update()

    def top_nav_change(self, e):
        index = e.control.selected_index
        self.bottom_nav_rail.selected_index = None

        if index == 0:
            self.app_layout.set_all_boards_view()
        elif index == 1:
            self.app_layout.set_dashboard_view()
        elif index == 2:
            self.app_layout.set_stats_view()
        self.page.update()

    def bottom_nav_change(self, e):
        self.top_nav_rail.selected_index = None

        if e.control.selected_index is None:
            e.control.selected_index = self.bottom_nav_rail.selected_index
            return

        board_id = e.control.destinations[e.control.selected_index].data
        self.app_layout.set_board_view(board_id)
        self.page.update()
