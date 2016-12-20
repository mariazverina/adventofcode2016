n_elf = 3012210
# n_elf = 31
# n_elf = 5
# n_elf = 300000

elves = range(1, n_elf + 1)

def part1(elves):
    start = 0
    while len(elves) > 1:
        next_start = (len(elves) + start) % 2
        elves = elves[start::2]
        start = next_start
    print(elves[0])


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def set_next(self, next_node):
        self.next = next_node
        return self

    def set_prev(self, prev_node):
        self.prev = prev_node
        return self

    def __repr__(self):
        return "Node " + repr(self.value)


class RingBuffer:
    def __init__(self, nodes):
        self.nodes = nodes
        self.origin = nodes[0]
        self.opposite = nodes[len(nodes) // 2]
        self.length = len(nodes)
        self.curpos = self.origin

    def delete_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def print_buffer(self):
        node = self.curpos
        while True:
            print(node, end=" ")
            node = node.next
            if node == self.curpos:
                break
        print(" end")

    def secret_santa(self):
        while self.length > 1:
            next_opposite = self.opposite.next
            if self.length % 2:
                next_opposite = next_opposite.next
            self.delete_node(self.opposite)
            self.curpos = self.curpos.next
            self.opposite = next_opposite
            # self.print_buffer()
            if not self.length % 100000:
                print(self.length)
            self.length -= 1


part1(elves)

nodes = [Node(i) for i in elves]
nodes = [n.set_next(next).set_prev(prev) for n, next, prev in zip(nodes, nodes[1:] + nodes[:1], nodes[-1:] + nodes[:-1])]

rb = RingBuffer(nodes)
rb.secret_santa()
print(rb.curpos)
