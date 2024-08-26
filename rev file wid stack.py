class Stack:

	def __init__(self):

		self._arr = []

	def push(self, val):
		self._arr.append(val)

	def is_empty(self):

		return len(self._arr) == 0

	def pop(self):

		if self.is_empty():
			print("Stack is empty")
			return

		return self._arr.pop()

'''Creating a function which will reverse
the lines of a file and Overwrites the
given file with its contents line-by-line
reversed'''


def reverse_file(filename):

	S = Stack()
	original = open(filename)

	for line in original:
		S.push(line.rstrip("\n"))

	original.close()

	output = open(filename, 'w')

	while not S.is_empty():
		output.write(S.pop()+";\n")

	output.close()


filename = "hello.txt"

reverse_file(filename)

with open(filename) as file:
	for f in file.readlines():
		print(f, end="")
