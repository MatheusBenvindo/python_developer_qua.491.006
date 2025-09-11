# views/stats_view.py

import flet as ft


def stats_view(store):
    total_boards = len(store.get_boards())
    total_lists = len(store.get_lists())
    total_items = sum(
        len(store.get_items(l["board_list_id"])) for l in store.get_lists()
    )  # CORRIGIDO
    total_comments = sum(
        len(i["comments"])  # CORRIGIDO
        for l in store.get_lists()
        for i in store.get_items(l["board_list_id"])  # CORRIGIDO
    )

    return ft.Column(
        [
            ft.Text("📊 Estatísticas", size=30, color="black"),
            ft.Text(f"Total de Boards: {total_boards}", color="black"),
            ft.Text(f"Total de Listas: {total_lists}", color="black"),
            ft.Text(f"Total de Cards: {total_items}", color="black"),
            ft.Text(f"Total de Comentários: {total_comments}", color="black"),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True,
    )
