from Node import Node

class DoublyLinkedList :
	# Linked list Head
	# New elements will be added to start of linked list 
	head = None
	numberOfNodes = 0

	def __init__(self):
		# Apna Awome constructor
		print "NAACHE MERI JAAN \n\n"

	def addNode(self, nodeData):
		newNode = Node()
		newNode.data = nodeData
		newNode.right = None
		newNode.left = None
		if self.head is None:
			# Create first node in linked list
			self.head = newNode
		else :
			newNode.right = self.head
			self.head.left = newNode
			self.head = newNode

		# Aiwanyi
		self.numberOfNodes = self.numberOfNodes + 1

	def printList(self):
		tempHead = self.head
		while tempHead is not None and tempHead.data is not None:
			print ("node data : " + str(tempHead.data))
			if tempHead.left is not None:
				print ("node ka left : " + str(tempHead.left.data))
			else:
				print ("iska koi nahi hain peeche :P")

			if tempHead.right is not None:
				print ("node ka right : " + str(tempHead.right.data))
			else:
				print ("iska koi nahi hain aage :P")

			print ("\n")

			tempHead = tempHead.right

	def searchElement(self, element):
		if element is not None :
			tempHead = self.head
			while tempHead is not None and tempHead.data is not None:
				if tempHead.data == element:
					print("\n Yeh Elemen hamri list hain paya gaya hain \n" + str(tempHead.data))
					return tempHead
				tempHead = tempHead.right
			print("\n Kachooo nahi mila bhai")
		else :
			print("\n kuch nahi mila bhai \n")

	def deleteElement(self, element):
		foundNode = self.searchElement(element)
		if foundNode is not None:
			print foundNode.data
			print foundNode.left.data
		else :
			print "\n Abe kuch hain hi nahi delete karne ke liye hurrrrr \n"
			pass

linkedList = DoublyLinkedList()
linkedList.addNode(100)
linkedList.addNode(99)
linkedList.addNode(87)
linkedList.printList()


linkedList.searchElement(1)
linkedList.searchElement(100)

linkedList.deleteElement(100)


