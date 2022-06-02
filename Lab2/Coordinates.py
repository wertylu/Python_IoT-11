import math


class Coordinate:
    def __init__(self, coordinate: list):
        self.coordinate = coordinate
        self.next = None

    def has_value(self, coordinate):
        if self.coordinate == coordinate:
            return True
        else:
            return False


class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def sum(self):
        return math.sqrt((self.head.coordinate[0]-self.tail.coordinate[0])**2 + (self.head.coordinate[1]-self.tail.coordinate[1])**2)

    def add_list_item(self, item):
        if not isinstance(item, Coordinate):
            item = Coordinate(item)
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item
        return

    def list_length(self):

        count = 0
        current_node = self.head

        while current_node is not None:
            count = count + 1
            current_node = current_node.next
        return count

    def output_list(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.coordinate)
            current_node = current_node.next
        return

    def unordered_search(self, value):
        current_node = self.head
        node_id = 1
        results = []

        while current_node is not None:
            if current_node.has_value(value):
                results.append(node_id)

            current_node = current_node.next
            node_id = node_id + 1

        return results
