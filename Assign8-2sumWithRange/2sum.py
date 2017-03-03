def setup(filename):
	f = open(filename, 'r')
	return set(int(line) for line in f)

def count2sumsInRange(filename):
	num_list = setup(filename)
	count = 0
	for i in range(-10000, 10001):
		if any(i - n in num_list for n in num_list):
			count += 1
	return count
		
	# return sum(
 #        1
 #        for n in range(-10000, 10001)
 #        if any(n - x in nums and 2 * x != n for x in nums)
 #    )
import platform
print platform.architecture()
# print(count2sumsInRange('LotsOfNumbers.txt'))