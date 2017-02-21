# implementing the classic, quicksort

# used to count number of compares depending on what pivot I choose
count = 0;

# results:
#	first element as pivot: 155432
#	last element: 157491
#	median of three: 137428

def quickSort(numbers, l, r):

	# base case
	if l >= r:
		return

	global count 
	count += (r - l) - 1

	# choose pivot
	pivotIndex = chooseMedianOfThreeAsPivot(numbers, l, r)

	# swap pivot with first element
	swap(numbers, pivotIndex, l);

	# partition around pivot
	pivotFinalIndex = partition(numbers, l, r)
	
	# recursively call on two halves
	quickSort(numbers, l, pivotFinalIndex - 1)
	quickSort(numbers, pivotFinalIndex + 1, r)


# assumes pivot is at first element (swap if not naturally so)
def partition(numbers, l, r):

	# get value of pivot
	pivot = numbers[l]

	# get index of the border between those smaller than pivot and bigger
	border = l + 1

	# loop through numbers swapping if necessary
	i = l + 1
	while i <= r:
		if numbers[i] < pivot:
			swap(numbers, border, i)
			border += 1
		i += 1

	# swap pivot to final position
	swap(numbers, border - 1, l)

	# return the correct position of the pivot so we can divide numbers into two around the pivot
	return (border - 1)


def swap(numbers, x, y):
	temp = numbers[x]
	numbers[x] = numbers[y]
	numbers[y] = temp

def chooseFirstElementAsPivot(numbers, l, r):
	return l

def chooseLastElementAsPivot(numbers, l, r):
	return r;

def chooseMedianOfThreeAsPivot(numbers, l, r):
	first = numbers[l]
	last = numbers[r]
	mid = numbers[(r - l) / 2]

	arr = [first, last, mid]
	arr.sort()
	if first is arr[1]:
		return l
	if last is arr[1]:
		return r
	if mid is arr[1]:
		return ((r - 1) / 2)

# TESTING --- TESING ---TESTING

numbers = open('integers1-10000.txt', 'r').read()
faketest = numbers.split('\n')

test = [int(x) for x in faketest]

quickSort(test, 0, len(test) - 1)
print(test[0:100])
print(count)