class LinkedListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class InterfaceQueue:
    def push(self, element):
        pass

    def pop(self):
        pass

    def top(self):
        pass


class MyQueue(InterfaceQueue):
    # you can declare your private attributes here
    def __init__(self):
        # do initialization if necessary
        self.head = None
        self.tail = None

    # implement the push method
    # write your code here
    def push(self, val):
        new_node = LinkedListNode(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = self.tail.next

    # implement the pop method
    # write your code here
    def pop(self):
        if self.head is not None:
            cur = self.head.val
            self.head = self.head.next
            return cur
        else:
            return -1

        # implement the top method

    # write your code here
    def top(self):
        if self.head:
            return (self.head.val)
        else:
            return -1

# Your MyQueue object will be instantiated and called as such:
# MyQueue queue = new MyQueue();
# queue.push(123);
# queue.top(); will return 123;
# queue.pop(); will return 123 and pop the first element in the queue