# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.


x, y = 0, 0
while x < 1000:
	if x % 3 == 0: y += x
	elif x % 5 == 0: y += x 
	x += 1	
print (x, y)
