class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node  # here node becomes the head

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node

    def get_length(self):
        count = 0
        n = self.head
        while n is not None:
            n = n.next
            count += 1
        return count

    def insert_at_index(self, index, data):
        new_node = Node(data)

        if index == 0:
            self.insert_at_begining(data)

        if index < 0 or index > self.get_length():
            raise Exception('Index out of bound')

        n = self.head
        count = 0
        while n is not None:
            if count == index -1:
                new_node.next = n.next
                n.next = new_node

                break
            n = n.next
            count += 1

    def traverse_list(self):
        if self.head is None:
            print("Linked list is empty")
            return
        else:
            n = self.head
            llstring = ''
            while n is not None:
                llstring += str(n.data) + '->'
                n = n.next
            print(llstring)


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_begining(20)
    ll.insert_at_begining(13)
    ll.insert_at_end(12)
    ll.insert_at_begining(18)
    ll.insert_at_end(15)
    ll.insert_at_index(2, 77)
    ll.traverse_list()
    print('length of linked list : {}'.format(ll.get_length()))
