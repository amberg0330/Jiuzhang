class MyQueue:
    def __init__(self):
        self.count = 0
        self.head = None
        self.tail = None

    def enqueue(self, value):
        node = ListNode(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next
        self.count += 1


    def dequeue(self):
        if self.head is None:
            raise Exception('This is an empty queue')
        cur = self.head
        self.head = cur.next
        self.count -= 1
        return cur.val

    def is_empty(self):
        return self.head is None

    def size(self):
        return self.count

    #method 1: 自己写queue

    if __name__ = '__main__':
        my_que = MyQueue()
        for i in range(50):
            my_que.enqueue(i)
        while not my_que.is_empty():
            print(my_que.dequeue(), end=" ")
        print()

    #method 2: 利用python自带的queue模块

    que = Que（）
    for i in range(50):
        que.put(i)
    while not que.empty():
        print(que.get(), end=" ")
    print()
    print(que.qsize())
