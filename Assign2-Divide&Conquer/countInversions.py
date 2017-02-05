def countInversions(numbers_list, l, r):
	count = 0
	m = (l + r) / 2

	#base case
	if l >= r:
		return 0

	#split to two halves
	count += countInversions(numbers_list, l, m)
	count += countInversions(numbers_list, m + 1, r)

	#merge
	count += mergeAndCount(numbers_list, l, r)
	return count

def mergeAndCount(numbers_list, l, r):
	#get size of each subarray and middle
	count = 0
	m = (l + r) / 2

	#get left and right subarrays
	L = numbers_list[l:m + 1]
	R = numbers_list[m + 1: r + 1]

	#create result array and init vars for merge step
	i = 0
	j = 0
	k = l
	L_length = m + 1- l
	R_length = r - m

	#merge together
	while i < L_length and j < R_length:
		if L[i] <= R[j]:
			numbers_list[k] = L[i]
			i += 1
		else:
			numbers_list[k] = R[j]
			j += 1
			count += (L_length - i)
		k += 1

	while i < L_length:
		numbers_list[k] = L[i]
		k += 1
		i += 1

	while j < R_length:
		numbers_list[k] = R[j]
		k += 1
		j += 1

	return count

def badCountInversions(numbers_list):
	count = 0
	for i in range(0, len(numbers_list)):
		for j in range(i + 1, len(numbers_list)):
			if numbers_list[i] > numbers_list[j]:
				count += 1
	return count

numbers = open('integers1-100000.txt', 'r').read()
test = numbers.split('\n')

print(countInversions(test, 0, len(test) - 1))