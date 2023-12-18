class History:
    def __init__(self):
        self.history = []
        self.query_id = 0

    def add_to_history(self, query, result):
        self.query_id += 1
        self.history.append((self.query_id, query, result))

    def view_history(self):
        for item in self.history:
            print(f"{item[0]}. Query: {item[1]}, Result: {item[2]}")