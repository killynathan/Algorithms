def multiply(x, y):
	# if x and y single digit return
	if (x / 10 == 0) and (y / 10 == 0):
		return x * y
	
	# get length of x and y
	x_length = len(str(x))
	y_length = len(str(y))
		
	# get a,b,c,d
	a = x / 10 ** (x_length / 2)
	b = x % 10 ** (x_length / 2)
	c = y / 10 ** (y_length / 2)
	d = y % 10 ** (y_length / 2)

	#recurse
	ac = multiply(a, c)
	bd = multiply(b, d)
	ad = multiply(a, d)
	bc = multiply(b, c)

	# carry out equation
	return 10 ** (x_length / 2 + y_length / 2) * ac + 10 ** (x_length / 2) * ad + 10 ** (y_length / 2) * bc + bd

#testing
print(multiply(546845, 65151522))
