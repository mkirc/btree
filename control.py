from classes.tree import *



def main():
	t = Tree()
	for i in range(10, 0, -1):
		t.insert(i, Data())
	t.preOrder()
	# m = t.getMin()
	# print(m)
	# print(t.findNodeByKey(5))
	t.deleteNodeByKey(5)
	t.preOrder()
main()
