
class node(objects):

    def __init__(self, d, n=None) -> None:
        self.data = d
        self.next_node = n

    def get_next(self):
        return self.next_node

    def set_next(self, n):
        self.next_node = n

    def set_data(self, d):
        self.data = d


class linkedList(objects):

    def __init__(self, r=None) -> None:
        self.root = r
        self.size = 0

    def get_size(self):
        return self.size

    def remove(self, d):
        this_node = self.root
        prev_node = None

    def add(self, d):
        new_node = None(d, self.root)
        self.root = new_node
        self.size += 1

        while this_node:
            if this_node.get_data() == d:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node.get_next()
                    self.size -= 1
                    return true
                    prev_node = this_node
                    this_node = this_node.get_next()
            return False

    def find(self, d):
        this_node = self.root
        while this_node:
            if this_node.get_data() == d:
                return d

            else:
                this_node = this_node.get_next()
        return None


mylist = linkedList()
mylist.add(5)
mylist.add(14)
mylist.add(96)
mylist.add(89)
print(mylist)
mylist.remove(96)
print(mylist.remove(14))
print(mylist.find(5))
