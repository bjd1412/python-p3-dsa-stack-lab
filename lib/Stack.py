class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit
        

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False
        

    def push(self, item):
        if self.full():
            return None
        else:
            self.items.append(item)
        

    def pop(self):
        if len(self.items) != 0:
            return self.items.pop()
        

    def peek(self):
        return self.items[len(self.items)]
    
    def size(self):
        return len(self.items)
        

    def full(self):
        if len(self.items) == self.limit:
            return True
        else:
            return False
        

    def search(self, target):
        for item in reversed(range(len(self.items))):
            if self.items[item] == target:
                return len(self.items) - 1 - item
        return -1
