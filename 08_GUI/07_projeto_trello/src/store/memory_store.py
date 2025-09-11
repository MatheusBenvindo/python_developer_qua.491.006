from models.board import Board
from models.board_list import BoardList
from models.item import Item
from models.user import User
from store.data_store import DataStore


class InMemoryStore(DataStore):
    def __init__(self):
        self.boards = {}
        self.users = {}
        self.board_lists = {}
        self.items = {}

    def add_board(self, board: Board):
        self.boards[board.board_id] = board

    def get_board(self, id: int):
        return self.boards[id]

    def get_boards(self):
        return list(self.boards.values())

    def update_board(self, board: Board, update: dict):
        for k in update:
            setattr(board, k, update[k])

    def remove_board(self, board: Board):
        del self.boards[board.board_id]
        self.board_lists[board.board_id] = []

    def add_list(self, board: int, list: BoardList):
        self.board_lists.setdefault(board, []).append(list)

    def get_lists_by_board(self, board: int):
        return self.board_lists.get(board, [])

    def get_lists(self):
        return [l for lists in self.board_lists.values() for l in lists]

    def remove_list(self, board: int, id: int):
        self.board_lists[board] = [
            l for l in self.board_lists[board] if l.board_list_id != id
        ]

    def add_user(self, user: User):
        self.users[user.name] = user

    def get_users(self):
        return list(self.users.values())

    def get_user(self, id: str):
        return self.users.get(id)

    def remove_user(self, id: str):
        self.users.pop(id, None)

    def add_item(self, board_list: int, item: Item):
        self.items.setdefault(board_list, []).append(item)

    def get_items(self, board_list: int):
        return self.items.get(board_list, [])

    def get_items_by_board(self, board: int):
        lists = self.get_lists_by_board(board)
        return [item for l in lists for item in self.get_items(l.board_list_id)]

    def get_item(self, id: int):
        for items in self.items.values():
            for item in items:
                if item.item_id == id:
                    return item

    def remove_item(self, board_list: int, id: int):
        self.items[board_list] = [i for i in self.items[board_list] if i.item_id != id]

    # ✅ adicionados
    def update_list(self, list_obj, update: dict):
        for k, v in update.items():
            setattr(list_obj, k, v)

    def update_item(self, item, update: dict):
        for k, v in update.items():
            setattr(item, k, v)
