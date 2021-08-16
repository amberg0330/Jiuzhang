class LinkedListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyQueue:
    def __init__(self):
            #初始时没有队列 两个指向同一个点
        self.before_head = LinkedListNode(-1)
        self.tail = self.before_head
    """
    @param: item: An integer
    @return: nothing
    """

    def enqueue(self, item):
        # write your code here
        # 把新的node插入到end后面
        self.tail.next = LinkedListNode(item)
        # 后移end指针
        self.tail = self.tail.next

    """
    @return: An integer
    """
    def dequeue(self):
        # write your code here
        if self.before_head.next is None:
            return -1
        # 记录队头数值
        head_val = self.before_head.next.val
        # 后移start指针
        self.before_head = self.before_head.next

        return head_val