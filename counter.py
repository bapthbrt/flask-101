# counter.py


class Counter:
    def __init__(self):
        self.id = 3

    def next(self):
        self.id += 1
        return self.id
