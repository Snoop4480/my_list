class LinkedList:
    class Item:
        value = None
        next = None

        def __init__(self, value):
            self.value = value

    head:Item = None

    

    def __len__(self):
        current = self.head
        index = 0
        while current:
            current = current.next
            index+=1
        return index




    def append_begin(self, value):
        item = LinkedList.Item(value)
        item.next = self.head
        self.head = item

    def append_end(self, value):
        current = self.head
        if current is None:
            self.head = LinkedList.Item(value)
            return
        
        while current.next:
            current = current.next
        item = LinkedList.Item(value)
        current.next = item

    def append_by_index(self, value, index): 
        current=self.head 
        if index==0: 
            item = LinkedList.Item(value) 
            item.next = self.head 
            self.head = item 
        else: 
            for i in range(index-1): 
                current=current.next 
                 
            item = LinkedList.Item(value) 
            item.next=current.next 
            current.next=item

    def remove_first(self):
        if self.head is None:
            raise ValueError("Элементов нет, удалять нечего!")
        self.head = self.head.next

    def remove_last(self):
        if self.head is None:
            raise ValueError("Элементов нет, удалять нечего!")
        if self.head.next is None:
            self.head = None
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = None
        


    def remove_first_value(self, value):
        if self.head is None:
            raise ValueError("Элементов нет, удалять нечего!")
        if self.head.value == value:
            self.head = self.head.next
            return
        current=self.head
        perem = None
        while current:
                if current.value == value:
                    perem = current
                    current = current.next
                    break
                current = current.next
        if perem is not None:
            perem.next = current.next
        else:
            raise ValueError("ERROR")

    def remove_last_value(self, value):
        if self.head is None:
            raise ValueError("Элементов нет, удалять нечего!")

        current=self.head
        current1=None

        while current.next:
            if current.next.value==value:
                current1=current
            current=current.next

        if current1 is not None:
            current1.next=current1.next.next

        else:
            if self.head.value == value:
                self.head = self.head.next
                return
            else:
                raise ValueError("Ошибка!")
            
    def remove_at(self, index):
        if self.head is None:
            raise ValueError("Элементов нет, удалять нечего!")
        if index==0:
            self.head=self.head.next
        else:
            current=self.head
            for i in range(index-1):
                current=current.next
            if current.next is None:
                raise ValueError("Ошибка!")
            current.next=current.next.next