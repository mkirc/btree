from classes.node import *

class Tree(object):
	def __init__(self):
		self.root = None
		self.count = 0

	def getMax(self):
		if self.root:
			return self.root.getMax()
		else:
			print('Tree is empty (brought to you by getMax() (tm))')
			return None

	def getMin(self):
		if self.root:			
			return self.root.getMin()
		else:
			print('Tree is empty (brought to you by getMin() (tm))')
			return None

	def findNodeByKey(self, key):

		if self.root:
			return self.root.findNodeByKey(key)
		else:
			return None

	def deleteNodeByKey(self, key):

		if self.root:
			# le smart way
			x = None
			y = None
			n = self.root.findNodeByKey(key)
			if not n.leftChild or not n.rightChild:
				x = n
			else:
				x = n.getDescendant()
			if x.leftChild:
				y = x.leftChild
			else:
				y = x.rightChild
			if y:
				y.parent = x.parent
			if not x.parent:
				self.root = y
			elif x == x.parent.leftChild:
				x.parent.leftChild = y
			else:
				x.parent.rightChild = y
			n.key = x.key
			n.data = x.data
		else:
			return None		
		


	def insert(self, key, data):
		n = Node()
		n.key = key
		n.data = data
		if not self.root:
			self.root = n
			n.height = 0
			self.count += 1
		else:
			n.height = 1
			self.root.insert(n)
			self.count += 1

	def preOrder(self):
		if self.root:
			print(self.root)
			if self.root.leftChild:
				self.root.leftChild.preOrder()
			if self.root.rightChild:
				self.root.rightChild.preOrder()
		else:
			print('wtf? tree is empty, and u know it.')
