import logging


class ClientIterator:
    def __init__(self, cur, query):
        self.cur = cur
        self.query = query

    def __iter__(self):
        self.cur.execute(self.query)
        self.results = self.cur.fetchall()
        self.current_idx = 0
        return self

    def __next__(self):
        if self.current_idx < len(self.results):
            client = self.results[self.current_idx]
            self.current_idx += 1
            return client
        else:
            logging.info("Запрос завершён")
            raise StopIteration
