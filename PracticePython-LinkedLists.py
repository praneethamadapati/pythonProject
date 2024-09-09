class Node:
    def __init__(self, value=None):
        self.dataval = value
        self.nextval = None

class PLinkedList:
   def __init__(self):
      self.headval = None

   def printlist(self):
      printval = self.headval
      while printval is not None:
         print(printval.dataval)
         printval = printval.nextval
   def atBeginning(self, newData):
      lnew = Node(newData)

      lnew.nextval = self.headval
      self.headval = lnew

list1 = PLinkedList()
list1.headval = Node("Mon")
l2 = Node("Tue")
l3 = Node("Wed")

list1.headval.nextval = l2
l2.nextval = l3

list1.atBeginning("Sun")
list1.printlist()