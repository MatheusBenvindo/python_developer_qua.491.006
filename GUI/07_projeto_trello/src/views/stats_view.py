import flet as ft

def stats_view(store):
    total_boards = len(store.get_boards())
    total_lists = sum(len(store.get_lists_by_board(b.board_id)) for b in store.get_boards())
    total_items = sum(len(store.get_items(l.board_list_id)) for l in store.get_lists())
    total_comments = sum(len(i.comments) for l in store.get_lists() for i in store.get_items(l.board_list_id))

    return ft.Column(
        controls=[
            ft.Text("📊 Estatísticas", size=30, color="white"),
            ft.Text(f"Boards: {total_boards}", color="white"),
            ft.Text(f"Listas: {total_lists}", color="white"),
            ft.Text(f"Cards: {total_items}", color="white"),
            ft.Text(f"Comentários: {total_comments}", color="white"),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
