def minToFront(self):
        runner = self.head
        min = self.head.value

        while runner != None:
            if runner.value < min:
                min = runner.value
            runner = runner.next

        runner = self.head
        while runner.next != None:
            if runner.next.value == min:
                minNode = runner.next
                runner.next = minNode.next
                minNode.next = self.head
                self.head = minNode
                return self
            runner = runner.next
        return self
    
    def maxToBack(self):
        runner = self.head
        max = self.head.value

        while runner != None:
            if runner.value > max:
                max = runner.value
            runner = runner.next

        runner = self.head
        maxNode = runner
        while runner.next != None:
            if runner.next.value == max:
                maxNode = runner.next
                runner.next = maxNode.next
                maxNode.next = None
            runner = runner.next
        runner.next = maxNode
        
        return self