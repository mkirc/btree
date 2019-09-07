
class Data:
	def __init__(self):
		pass

class Node(object):
	def __init__(self, *args, **kwargs):
		self.parent = None
		self.leftChild = None
		self.rightChild = None
		self.key = None
		self.data = None
		self.height = None

	def __str__(self):
		if str(self.data):
			return 'Key: ' + str(self.key) + ' Data: ' + str(self.data)

	def getMax(self):
		if self.rightChild:
			return self.rightChild.getMax()
		else:
			return self

	def getMin(self):
		if self.leftChild:
			return self.leftChild.getMin()
		else:
			return self

	def insert(self, node):
		if type(node) == type(Node()):
			if self.key > node.key:
				if not self.leftChild:
					self.leftChild = node
					node.parent = self
				else:
					node.height += 1
					self.leftChild.insert(node)
			elif self.key < node.key:
				if not self.rightChild:
					self.rightChild = node
					node.parent = self
				else:
					node.height += 1
					self.rightChild.insert(node)
			else:
				self.data = node.data
		else:
			print('gimme no shit to eat!')

	def findNodeByKey(self, key):

		if self.key == key:
			return self
		elif self.key > key:
			if self.leftChild:
				return self.leftChild.findNodeByKey(key)
		else:
			if self.rightChild:
				return self.rightChild.findNodeByKey(key)

	def getDescendant(self):

		# black magic...keep eye on!
		if self.rightChild:
			return self.rightChild.getMin()
		y = self.parent

		while y and self == y.rightChild:
			self = y
			y = y.parent
		return y

	def preOrder(self):
		print(self)
		print(self.height)
		if self.leftChild:
			self.leftChild.preOrder()
		if self.rightChild:
			self.rightChild.preOrder()


