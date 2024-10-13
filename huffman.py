import heapq

class MinHeapNode:
	def __init__(self, data, freq):
		self.data = data
		self.freq = freq
		self.left = None
		self.right = None

	def __lt__(self, other):
		return self.freq < other.freq

class HuffmanCoding:
	def print_codes(self, root, str_code):
		if root is None:
			return 
		if root.data != '$':
			print(f"{root.data}: {str_code}")
		self.print_codes(root.left, str_code + "0")
		self.print_codes(root.right, str_code + "1")

	def huffman_code(self, data, freq):
		min_heap = []
		for i in range(len(data)):
			heapq.heappush(min_heap, MinHeapNode(data[i], freq[i]))

		while len(min_heap) > 1:
			left = heapq.heappop(min_heap)
			right = heapq.heappop(min_heap)
			temp = MinHeapNode('$', left.freq + right.freq)
			temp.left = left
			temp.right = right
			heapq.heappush(min_heap, temp)

		self.print_codes(min_heap[0], "")

def main():
	data = ['A', 'B', 'C', 'D']
	freq = [23, 12, 34, 10]
	huffman = HuffmanCoding()  # Create an instance of HuffmanCoding
	huffman.huffman_code(data, freq)  # Call the method using the instance

if __name__ == "__main__":
	main()
