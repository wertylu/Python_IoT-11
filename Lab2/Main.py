from Coordinates import Coordinate
from Coordinates import SingleLinkedList


def main():
    node1 = Coordinate([0, 0])
    node2 = Coordinate([1, 4])
    node3 = Coordinate([2, -3])
    linked_list = SingleLinkedList()
    linked_list.add_list_item(node1)
    linked_list.add_list_item(node2)
    linked_list.add_list_item(node3)
    print(linked_list.list_length())
    print(linked_list.output_list())
    print('%.3f' % linked_list.sum())


if __name__ == '__main__':
    main()
