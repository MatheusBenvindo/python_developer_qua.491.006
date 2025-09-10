class DataStore:
    def add_board(self, model): raise NotImplementedError
    def get_board(self, id): raise NotImplementedError
    def get_boards(self): raise NotImplementedError
    def update_board(self, model, update): raise NotImplementedError
    def remove_board(self, board): raise NotImplementedError

    def add_user(self, model): raise NotImplementedError
    def get_users(self): raise NotImplementedError
    def get_user(self, id): raise NotImplementedError
    def remove_user(self, id): raise NotImplementedError

    def add_list(self, board, model): raise NotImplementedError
    def get_lists(self): raise NotImplementedError
    def get_list(self, id): raise NotImplementedError
    def get_lists_by_board(self, board): raise NotImplementedError
    def remove_list(self, board, id): raise NotImplementedError

    def add_item(self, board_list, model): raise NotImplementedError
    def get_items(self, board_list): raise NotImplementedError
    def get_item(self, id): raise NotImplementedError
    def get_items_by_board(self, board): raise NotImplementedError
    def remove_item(self, board_list, id): raise NotImplementedError
