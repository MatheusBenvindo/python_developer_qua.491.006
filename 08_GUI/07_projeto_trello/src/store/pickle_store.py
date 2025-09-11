# store/pickle_store.py

import pickle
from models.board import Board
from models.board_list import BoardList
from models.item import Item
from models.user import User
from store.data_store import DataStore
import os


class PickleStore(DataStore):
    def __init__(self, file_path="data.pkl"):
        self.file_path = file_path
        self._load_data()

    def _load_data(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "rb") as f:
                data = pickle.load(f)
                self.boards = {int(k): v for k, v in data.get("boards", {}).items()}
                self.users = data.get("users", {})
                self.board_lists = {
                    int(k): v for k, v in data.get("board_lists", {}).items()
                }
                self.items = {int(k): v for k, v in data.get("items", {}).items()}
        else:
            self.boards = {}
            self.users = {}
            self.board_lists = {}
            self.items = {}

    def _save_data(self):
        data = {
            "boards": self.boards,
            "users": self.users,
            "board_lists": self.board_lists,
            "items": self.items,
        }
        with open(self.file_path, "wb") as f:
            pickle.dump(data, f)

    def add_board(self, board: Board):
        self.boards[board.board_id] = board.to_dict()
        self._save_data()

    def get_board(self, id: int):
        # Note: This store now returns dicts, the UI layer is responsible for creating controls
        return self.boards.get(id)

    def get_boards(self):
        return list(self.boards.values())

    def update_board(self, board: Board, update: dict):
        if board.board_id in self.boards:
            self.boards[board.board_id].update(update)
            self._save_data()

    def remove_board(self, board: Board):
        if board.board_id in self.boards:
            del self.boards[board.board_id]
            if board.board_id in self.board_lists:
                del self.board_lists[board.board_id]
            # Also remove associated items
            # This logic might need to be more robust depending on your needs
            self._save_data()

    def add_list(self, board_id: int, list_obj: BoardList):
        lists = self.board_lists.setdefault(board_id, [])
        lists.append(list_obj.to_dict())
        self._save_data()

    def get_lists_by_board(self, board_id: int):
        return self.board_lists.get(board_id, [])

    def get_lists(self):
        return [l for lists in self.board_lists.values() for l in lists]

    def remove_list(self, board_id: int, list_id: int):
        if board_id in self.board_lists:
            self.board_lists[board_id] = [
                l for l in self.board_lists[board_id] if l["board_list_id"] != list_id
            ]
            if list_id in self.items:
                del self.items[list_id]
            self._save_data()

    def add_user(self, user: User):
        self.users[user.name] = user  # Assuming User is not a Flet control
        self._save_data()

    def get_users(self):
        return list(self.users.values())

    def get_user(self, id: str):
        return self.users.get(id)

    def remove_user(self, id: str):
        if id in self.users:
            self.users.pop(id)
            self._save_data()

    def add_item(self, board_list_id: int, item: Item):
        items = self.items.setdefault(board_list_id, [])
        items.append(item.to_dict())
        self._save_data()

    def get_items(self, board_list_id: int):
        return self.items.get(board_list_id, [])

    def get_items_by_board(self, board_id: int):
        lists = self.get_lists_by_board(board_id)
        return [item for l in lists for item in self.get_items(l["board_list_id"])]

    def get_item(self, id: int):
        for items in self.items.values():
            for item_data in items:
                if item_data["item_id"] == id:
                    return item_data
        return None

    def remove_item(self, board_list_id: int, item_id: int):
        if board_list_id in self.items:
            self.items[board_list_id] = [
                i for i in self.items[board_list_id] if i["item_id"] != item_id
            ]
            self._save_data()

    def update_list(self, list_obj, update: dict):
        board_id = list_obj.board.board_id
        if board_id in self.board_lists:
            for l in self.board_lists[board_id]:
                if l["board_list_id"] == list_obj.board_list_id:
                    l.update(update)
                    self._save_data()
                    break

    def update_item(self, item, update: dict):
        list_id = item.list.board_list_id
        if list_id in self.items:
            for i in self.items[list_id]:
                if i["item_id"] == item.item_id:
                    i.update(update)
                    self._save_data()
                    break
