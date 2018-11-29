class SwagCollection(object):
    def __init__(self):
        self.items = {}

    def pick_up(self, item, location):
        self.items[location] = item

    def sort_items(self):
        pass

