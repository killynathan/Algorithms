def setup(filename):
	f = open(filename, 'r')
	return set(int(line) for line in f)

def count2sumsInRange(filename, low, high):
	num_list = setup(filename)

	count = 0
	for i in range(low, high + 1):
		print(i)
		if any(i - n in num_list for n in num_list):
			count += 1
	return count
		
print(count2sumsInRange('LotsOfNumbers.txt', 3, 10))